import requests

def get_cidades_ceara():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/23/municipios"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [cidade['nome'] for cidade in data]
