#!/usr/bin/python3

import requests
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')

# Definindo nomes do Tipo de Produto, Produto e Engagement
product_type_name = "Development Team"
product_name = "Python Product"
engagement_name = "Python Engagement"

class DefectdojoResources(object):

    def ResourcesCreation():

        # URL do DefectDojo para API
        url = "http://192.168.1.108:8080/api/v2"

        # API Key
        api_key = "654fb7c6af41b9c43b18ede8c90645cba1f71003"

        # Configuração de Headers
        headers = {
            "Authorization": f"Token {api_key}",
            "Accept": "application/json",
        }

        # Criando o tipo de Produto
        product_type_payload = {
            "name": product_type_name,
            "description": "Tipo de Produto",
            "critical_product": True,
            "key_product": True,
        }
        print("Criando Tipo de Produto...")
        product_type_response = requests.post(
            f"{url}/product_types/", headers=headers, json=product_type_payload
        )
        product_type_id = product_type_response.json()["id"]
        print("Product Type ID = " + str(product_type_id))

        # Criando o Produto
        product_payload = {
            "name": product_name,
            "description": "Descrição do Produto",
            "prod_type": product_type_id,
            "business_criticality": "very high",
            "platform": "web service",
            "lifecycle": "construction",
            "origin": "third party library",
            "external_audience": True,
            "internet_accessible": True,
            "enable_simple_risk_acceptance": False,
            "enable_full_risk_acceptance": True,
            "technical_contact": "2",
            "team_manager": "2",
        }
        print("Criando Produto...")
        product_response = requests.post(
            f"{url}/products/", headers=headers, json=product_payload
        )
        product_id = product_response.json()["id"]
        print("Product ID = " + str(product_id))

        # Criando o Engagement
        engagement_payload = {
            "name": engagement_name,
            "description": "Descrição do Engagement",
            "target_start": date,
            "target_end": date,
            "product": product_id,
            "environment": "Pre-prod",
            "engagement_type": "CI/CD",
            "lead": "2",
            "deduplication_on_engagement": True,
            "close_old_findings": True,
        }
        print("Criando Engagement...")
        engagement_response = requests.post(
            f"{url}/engagements/", headers=headers, json=engagement_payload
        )

        engagement_json = engagement_response.json()
        engagement_id = engagement_json.get("id")
        print("Engagement ID = " + str(engagement_id))

        # Configurações de envio para o Engagement
        print("Importando relatório de vulnerabilidades...")
        url_import_scan = "http://192.168.1.108:8080/api/v2/import-scan/"
        scan_payload = {
            "headers": {"Authorization": f"Token {api_key}"},
                "json": {
                    "scan_type": "Bandit Scan",
                    "engagement": engagement_id,
                    "minimum_severity": "Info",
                    "active": True,
                    "verified": True,
                },
                "files": {"file": open("bandit.json")}
            }

        # Aplicando o import para o Defectdojo
        print("Relatório importado com sucesso!")
        return requests.post(url_import_scan, files=scan_payload['files'], data=scan_payload['json'], headers=scan_payload['headers'], verify=False)