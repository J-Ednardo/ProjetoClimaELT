import requests
import os
from dotenv import load_dotenv 
import mysql.connector # type: ignore
from datetime import datetime, timezone

load_dotenv()

api_key = os.getenv("API_KEY")
urlIBGE = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios"
responseIBGE = requests.get(urlIBGE)
data = responseIBGE.json()
cidades_ceara = [cidade["nome"] for cidade in data][:45]

conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

cursor = conn.cursor()

for cidade in cidades_ceara:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"   
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        desc = data['weather'][0]['description']
        umidade = data['main']['humidity']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        vento = data['wind']['speed']
        data_hora = datetime.fromtimestamp(data["dt"], tz = timezone.utc)

        cursor.execute("""
            INSERT INTO DadosClimaticos (
                cidade, temperatura_atual, sensacao_termica, descricao, umidade, temperatura_min,
                temperatura_max, velocidade_vento, data_medicao           
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                temperatura_atual = VALUES(temperatura_atual),
                sensacao_termica = VALUES(sensacao_termica),
                descricao = VALUES(descricao),
                umidade = VALUES(umidade),
                temperatura_min = VALUES(temperatura_min),
                temperatura_max = VALUES(temperatura_max),
                velocidade_vento = VALUES(velocidade_vento),
                data_medicao = VALUES(data_medicao)
            """, (cidade, temp, feels_like, desc, umidade, temp_min, temp_max, vento, data_hora))
        
        conn.commit()
        print(f"Dados da {cidade} inseridos com sucesso")
    else:
        print(f"Erro ao buscar dados de {cidade} : {data.get('message')}")

cursor.close()
conn.close()
