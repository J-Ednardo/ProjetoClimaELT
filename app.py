import requests
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("API_KEY")
urlIBGE = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios"
responseIBGE = requests.get(urlIBGE)
data = responseIBGE.json()
cidades_ceara = [cidade["nome"] for cidade in data]


for cidade in cidades_ceara:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"   
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperatura = data['main']['temp']
        descricao = data['weather'][0]['description']
        umidade = data['main']['humidity']
        print(f"{cidade}: {temperatura}°, {descricao}, Umidade: {umidade}%")
    else:
        print(f"{cidade}: Erro ao buscar dados ({data.get('message')})")
