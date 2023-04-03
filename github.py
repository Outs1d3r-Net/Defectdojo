from git import Repo
import os

class Github(object):

    def GithubClone():

        # Endereço do Repositório
        repo_url = 'https://github.com/Contrast-Security-OSS/vulnpy.git'

        # Diretório onde o projeto será clonado
        local_dir = '/home/mgchahad/Documents/Defectdojo/automation-reports/vulnpy'

        # Clonando o repositório
        print("Clonando repositório...")
        Repo.clone_from(repo_url, local_dir)
        print("Clone aplicado com sucesso!")