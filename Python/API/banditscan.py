import os

class Bandit(object):

    def BanditScan():

        # Executando o Bandit Scan
        print("Executando Bandit Scan...")
        os.system('bandit -r <GIT_PROJECT_DIR> -f json -o ./bandit.json')
        print("Bandit Scan executado com sucesso!")