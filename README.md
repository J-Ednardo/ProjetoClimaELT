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

## 🏁 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/ProjetoClimaELT.git](https://github.com/seu-usuario/ProjetoClimaELT.git)
    cd ProjetoClimaELT
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
   

4.  **Configure as variáveis de ambiente:**
    * Renomeie o arquivo `.env.example` para `.env`.
    * Preencha as variáveis com suas credenciais do MySQL e a chave da API do OpenWeather.

    ```ini
    # .env
    DB_HOST='localhost'
    DB_USER='seu_usuario'
    DB_PASSWORD='sua_senha'
    DB_NAME='clima_ceara'
    OPENWEATHER_API_KEY='sua_chave_api_aqui'
    ```

5.  **Execute o script de coleta de dados:**
    ```bash
    python main.py
    ```

6.  **Inicie o dashboard interativo:**
    ```bash
    streamlit run dashboard.py
    ```
