import mysql.connector
from models.dados_meteorologicos import DadosMeteorologicos
from config import DB_CONFIG

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

def insert_dados_meteorologicos(conn, data: DadosMeteorologicos):
    cursor = conn.cursor()
    query = """
        INSERT INTO DadosClimaticos (
            cidade, temperatura_atual, sensacao_termica, descricao, umidade,
            temperatura_min, temperatura_max, velocidade_vento, data_medicao
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
    """
    values = (
        data.cidade, data.temperatura_atual, data.sensacao_termica,
        data.descricao, data.umidade, data.temperatura_min,
        data.temperatura_max, data.velocidade_vento, data.data_medicao
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
