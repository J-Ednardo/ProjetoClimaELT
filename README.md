# 🌦️ ProjetoClimaELT

Este projeto coleta dados climáticos de todas as cidades do estado do Ceará utilizando a API do OpenWeather, e os armazena em um banco de dados MySQL. Ele segue uma arquitetura organizada em camadas com separação de responsabilidades, facilitando a manutenção e escalabilidade.

---

## 🚀 Funcionalidades

- Busca a lista de cidades do Ceará via [API do IBGE](https://servicodados.ibge.gov.br/api).
- Obtém dados meteorológicos atuais e previsão via [OpenWeather API](https://openweathermap.org/api).
- Extrai temperatura, umidade, sensação térmica, vento, descrição do tempo, etc.
- Salva os dados no banco de dados MySQL.
- Atualiza automaticamente os dados existentes.
- Arquitetura separada por camadas (model, service, main).

---

## ⚙️ Tecnologias Usadas

- Python 3.10+
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
