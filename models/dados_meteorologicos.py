from dataclasses import dataclass
from datetime import datetime

@dataclass
class DadosMeteorologicos:
    cidade: str
    temperatura_atual: float
    sensacao_termica: float
    descricao: str
    umidade: int
    temperatura_min: float
    temperatura_max: float
    velocidade_vento: float
    data_medicao: datetime
