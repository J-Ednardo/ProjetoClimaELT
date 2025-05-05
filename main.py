from services.ibge_service import get_cidades_ceara
from services.weather_service import get_weather_data
from services.database_service import connect_db, insert_dados_meteorologicos

def main():
    conn = connect_db()
    cidades = get_cidades_ceara()

    for cidade in cidades:
        data, error = get_weather_data(cidade)
        if data:
            insert_dados_meteorologicos(conn, data)
            print(f"Dados de {cidade} inseridos com sucesso")
        else:
            print(f"Erro ao buscar dados de {cidade}: {error}")

    conn.close()

if __name__ == "__main__":
    main()