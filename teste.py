import requests # type: ignore
import json

async def Cat(self, message):
    linkAPI =  'https://api.thecatapi.com/v1/images/search'
    response = requests.get(linkAPI)

    if response.status_code == 200:
        data = response.json()
        with open('dataCatAPI.json', 'w') as f:
            json.dump(data, f, indent=4)
            print("Dados salvos com sucesso em 'dados.json'")
        
        with open('dados.json', 'r') as f:  # Substitua 'dados.json' pelo nome do seu arquivo
            data = json.load(f)
            print(json.dumps(data, indent=2))
    else:
        print(f"Erro ao fazer request: {response.status_code}")