# 🌦️ ProjetoClimaELT

Este projeto coleta dados climáticos de todas as cidades do estado do Ceará utilizando a API do OpenWeather, e os armazena em um banco de dados MySQL. Ele segue uma arquitetura organizada em camadas com separação de responsabilidades, facilitando a manutenção e escalabilidade.

---

## 📊 Dashboard Interativo

- **Visualização Geográfica:** Mapa interativo com a localização das estações meteorológicas e dados climáticos.
- **Filtros Dinâmicos:** Filtre os dados por cidade, intervalo de datas ou condições do tempo.
- **Gráficos Detalhados:** Análise de variações de temperatura, umidade, velocidade do vento e outras métricas ao longo do tempo.

---

## 🚀 Funcionalidades

- **Coleta de Cidades:** Busca a lista de cidades do Ceará via [API do IBGE](https://servicodados.ibge.gov.br/api).
- **Dados Abrangentes:** Obtém dados meteorológicos atuais e previsão via [OpenWeather API](https://openweathermap.org/api).
- **Extração Detalhada:** Extrai temperatura, umidade, sensação térmica, vento, descrição do tempo, etc.
- **Armazenamento Robusto:** Salva os dados no banco de dados MySQL.
- **Atualização Inteligente:** Atualiza automaticamente os dados existentes.
- **Visualização Interativa:** Dashboard completo para análise e exploração dos dados climáticos. 

---

## ⚙️ Tecnologias Usadas

- Python 3.10+
- Streamlit
- OpenWeather API
- MySQL
- Requests
- dotenv
- zoneinfo (fuso horário)
- [IBGE Localidades API](https://servicodados.ibge.gov.br/api)

---

## 🛠️ Pré-requisitos

- Python 3.10+
- MySQL Server
- Conta e chave de API no [OpenWeather](https://home.openweathermap.org/api_keys)

---
