import mysql.connector
import pandas as pd
from config import DB_CONFIG

def export_csv(nome_arquivo="data/dados_climaticos.csv"):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        query = "SELECT * FROM DadosClimaticos"
        df = pd.read_sql(query, conn)
        df.to_csv(nome_arquivo, index=False, encoding='utf-8')
        print(f"Dados exportados com sucesso para {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao exportar os dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()