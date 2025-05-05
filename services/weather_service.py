import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from config import API_KEY
from models.dados_meteorologicos import DadosMeteorologicos

def get_weather_data(cidade: str) -> tuple[DadosMeteorologicos | None, str | None]:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None, response.json().get('message')
    
    data = response.json()
    try:
        dados_meteorologicos = DadosMeteorologicos(
            cidade = cidade,
            temperatura_atual = data['main']['temp'],
            sensacao_termica = data['main']['feels_like'],
            descricao = data['weather'][0]['description'],
            umidade = data['main']['humidity'],
            temperatura_min = data['main']['temp_min'],
            temperatura_max = data['main']['temp_max'],
            velocidade_vento = data['wind']['speed'],
            data_medicao=datetime.fromtimestamp(data["dt"], tz=ZoneInfo("America/Sao_Paulo"))
        )
        return dados_meteorologicos, None
    except (KeyError, TypeError) as e:
        return None, str(e)
