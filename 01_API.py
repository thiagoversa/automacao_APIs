import requests

url_nasa =  "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "DEMO_KEY"
}

#
resposta = requests.get("url_nasa")

if resposta.status_code == 200:
    print(f"Sucesso! {resposta.status_code}")
else:
    print(f"Erro! {resposta.status_code}")

# adicionando um cometário    
