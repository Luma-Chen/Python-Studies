import requests
import json
import base64 
import time

BASE_URL = "https://api.github.com/search/repositories"
QUERY = f"topic:data-science language:python forks:>=8 archived:false" 
GITHUB_TOKEN = "SEU_TOKEN" 

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def obter_conteudo_readme(owner, repo):
    readme_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    time.sleep(0.5) 
    
    try:
        response = requests.get(readme_url, headers=headers)
        response.raise_for_status() 
        
        readme_data = response.json()
        
        if 'content' in readme_data:
            content_encoded = readme_data['content'].encode('utf-8')
            content_decoded = base64.b64decode(content_encoded).decode('utf-8')
            return content_decoded
        
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            return "README NOT FOUND"
        return "API ERROR"
    except Exception:
        return "DECODING ERROR"   
    return None


def coletar_todos_repositorios():
    params = {
        "q": QUERY,
        "sort": "forks",
        "order": "desc",
        "per_page": 100
    }

    todos_repos = []
    MAX_PAGES = 10
    print(f"Iniciando coleta com a query: {QUERY}")

    for page_num in range(1, MAX_PAGES + 1):
        params['page'] = page_num
        print(f"| Buscando Página {page_num}...")
        
        try:
            response = requests.get(BASE_URL, params=params, headers=headers)
            response.raise_for_status()
            dados_json = response.json()
            repos_na_pagina = dados_json.get('items', [])
            
            if not repos_na_pagina:
                print("| Fim da busca: Nenhuma página a mais encontrada.")
                break

            todos_repos.extend(repos_na_pagina)

            if len(repos_na_pagina) < 100:
                print("| Fim da busca: Última página alcançada.")
                break              
        except requests.exceptions.RequestException as e:
            print(f"| ERRO DE PAGINAÇÃO na página {page_num}: {e}")
            break   
    return todos_repos


def buscar_repositorios_data_science (lista_repos):
    lista_de_readmes= {}
    total_coletados= 0
    print("\n--- Iniciando Coleta de READMEs ---")
    
    for repo in lista_repos:
        owner= repo['owner']['login']
        repo_name= repo['name']
        readme_content= obter_conteudo_readme(owner, repo_name)
        
        if readme_content and "API ERROR" not in readme_content:
            lista_de_readmes[repo['html_url']] = readme_content
            total_coletados += 1
            print(f"| OK: {owner}/{repo_name}")
        else:
            print(f"| FALHA: {owner}/{repo_name}")
            pass

    print(f"\nColeta de READMEs finalizada. Total de arquivos obtidos: {total_coletados}")
    return lista_de_readmes


if __name__ == "__main__":
    lista_completa_repos = coletar_todos_repositorios()
    
    if lista_completa_repos:
        readmes_coletados = buscar_repositorios_data_science(lista_completa_repos)
        nome_arquivo = "readmes_coletados.json"
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(readmes_coletados, f, ensure_ascii=False, indent=4)
            
            print(f"\n--- COLETA FINALIZADA ---")
            print(f"O conteúdo de todos os {len(readmes_coletados)} READMEs foi salvo no arquivo:")
            print(f"Caminho do arquivo: ./{nome_arquivo}")
            
        except Exception as e:
            print(f"Erro ao salvar o arquivo JSON: {e}")