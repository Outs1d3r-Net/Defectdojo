from git import Repo
import os

class Github(object):

    def GithubClone():

        # Endereço do Repositório
        repo_url = '<GIT_PROJECT_URL>'

        # Diretório onde o projeto será clonado
        local_dir = '<LOCAL_DIRECTORY>'

        # Clonando o repositório
        print("Clonando repositório...")
        Repo.clone_from(repo_url, local_dir)
        print("Clone aplicado com sucesso!")