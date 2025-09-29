import requests

BASE_URL= "https://api.github.com/search/repositories"
QUERY= f"topic:data-science language:python forks:>=8 archived:false" 
GITHUB_TOKEN= "SEU_TOKEN"
headers= {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def buscar_repositorios_data_science():
    params= {
        "q": QUERY,
        "sort": "forks",
        "order": "desc",
        "per_page": 100
    }
    print(f"Fazendo busca por: {QUERY}")

    if GITHUB_TOKEN == "SEU_TOKEN":
        response= requests.get(BASE_URL, params=params)
    else:
        response= requests.get(BASE_URL, params=params, headers=headers)
    
    if response.status_code == 200:
        dados_json= response.json()
        print("--- Resultado JSON (Apenas os primeiros 6) ---")
        for i, repo in enumerate(dados_json.get('items', [])):
            if i >= 6:
                break
            print(f"URL: {repo['html_url']}")
            print(f"Estrelas: {repo['stargazers_count']}")
            print(f"Forks: {repo['forks_count']}")
            print(f"Linguagem: {repo['language']}")
            print("-" * 20)           
        print(f"\nTotal de repositórios encontrados: {dados_json.get('total_count', 0)}")
        return dados_json
    else:
        print(f"Erro na requisição. Status Code: {response.status_code}")
        print(f"Resposta da API: {response.text}")
        return None

if __name__ == "__main__":
    buscar_repositorios_data_science()
