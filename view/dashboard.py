import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Climático do Ceará",
    page_icon="🌦️",
    layout="wide",
)

@st.cache_data
def carregar_dados_climaticos():
    try:
        df = pd.read_csv("data\dados_climaticos.csv")
        df['data_medicao'] = pd.to_datetime(df['data_medicao'])
        return df
    except FileNotFoundError:
        st.error("Arquivo 'dados_climaticos.csv' não encontrado. Execute o projeto principal (main.py) primeiro.")
        return pd.DataFrame()

@st.cache_data
def carregar_coordenadas():
    try:
        df_coords = pd.read_csv("data\coordenadas_ceara.csv")
        return df_coords
    except FileNotFoundError:
        st.warning("Arquivo 'coordenadas_ceara.csv' não encontrado. O mapa não será exibido.")
        return None

df_clima = carregar_dados_climaticos()
df_coords = carregar_coordenadas()

if not df_clima.empty and df_coords is not None:
    df_completo = pd.merge(df_clima, df_coords, on="cidade", how="left")
else:
    df_completo = df_clima

st.sidebar.header("Filtros Interativos")

if not df_completo.empty:
    cidades_unicas = sorted(df_completo['cidade'].unique())
    cidades_selecionadas = st.sidebar.multiselect(
        "Selecione a(s) Cidade(s):",
        options=cidades_unicas,
        default=cidades_unicas
    )

    temp_min_val = float(df_completo['temperatura_atual'].min())
    temp_max_val = float(df_completo['temperatura_atual'].max())
    temp_selecionada = st.sidebar.slider(
        'Filtrar por Temperatura (°C):',
        min_value=temp_min_val,
        max_value=temp_max_val,
        value=(temp_min_val, temp_max_val)
    )

    df_filtrado = df_completo[
        (df_completo['cidade'].isin(cidades_selecionadas)) &
        (df_completo['temperatura_atual'].between(temp_selecionada[0], temp_selecionada[1]))
    ]
else:
    df_filtrado = pd.DataFrame()

st.title("🌦️ Dashboard de Dados Climáticos - Ceará")
st.markdown("---")

if df_filtrado.empty:
    st.warning("Nenhum dado disponível para os filtros selecionados.")
else:
    col1, col2, col3, col4 = st.columns(4)
    temperatura_media = df_filtrado['temperatura_atual'].mean()
    umidade_media = df_filtrado['umidade'].mean()
    cidade_mais_quente = df_filtrado.loc[df_filtrado['temperatura_atual'].idxmax()]
    cidade_mais_fria = df_filtrado.loc[df_filtrado['temperatura_atual'].idxmin()]

    col1.metric("Temperatura Média", f"{temperatura_media:.1f} °C")
    col2.metric("Umidade Média", f"{umidade_media:.0f}%")
    col3.metric("Cidade Mais Quente", f"{cidade_mais_quente['cidade']} ({cidade_mais_quente['temperatura_atual']}°C)")
    col4.metric("Cidade Mais Fria", f"{cidade_mais_fria['cidade']} ({cidade_mais_fria['temperatura_atual']}°C)")

    tab1, tab2, tab3 = st.tabs(["🗺️ Visão Geográfica", "📊 Análise Detalhada", "📋 Dados Brutos"])

    with tab1:
        st.header("Mapa de Temperaturas no Estado")
        if 'latitude' in df_filtrado.columns and 'longitude' in df_filtrado.columns:
            df_mapa = df_filtrado.dropna(subset=['latitude', 'longitude'])
            
            fig_map = px.scatter_mapbox(
                df_mapa,
                lat="latitude",
                lon="longitude",
                size="temperatura_atual",
                color="temperatura_atual",
                hover_name="cidade",
                hover_data={"sensacao_termica": True, "umidade": True, "latitude": False, "longitude": False},
                color_continuous_scale=px.colors.sequential.Plasma,
                size_max=15,
                zoom=6,
                mapbox_style="open-street-map",
                title="Distribuição de Temperatura nas Cidades do Ceará"
            )
            fig_map.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.warning("Dados de coordenadas não disponíveis para gerar o mapa.")

    with tab2:
        st.header("Análise Comparativa entre Cidades")
        
        col_graf1, col_graf2 = st.columns(2)
        
        with col_graf1:
            st.subheader("Temperatura Atual")
            fig_temp = px.bar(
                df_filtrado.sort_values("temperatura_atual", ascending=False),
                x="cidade",
                y="temperatura_atual",
                color="temperatura_atual",
                labels={"cidade": "Cidade", "temperatura_atual": "Temperatura (°C)"}
            )
            st.plotly_chart(fig_temp, use_container_width=True)
            
            st.subheader("Distribuição da Sensação Térmica")
            fig_box = px.box(
                df_filtrado,
                x="cidade",
                y="sensacao_termica",
                color="cidade",
                labels={"cidade": "Cidade", "sensacao_termica": "Sensação Térmica (°C)"}
            )
            st.plotly_chart(fig_box, use_container_width=True)

        with col_graf2:
            st.subheader("Condições Climáticas Gerais")
            descricao_counts = df_filtrado['descricao'].value_counts()
            fig_pie = px.pie(
                values=descricao_counts.values,
                names=descricao_counts.index,
                title="Proporção das Condições Climáticas"
            )
            st.plotly_chart(fig_pie, use_container_width=True)

            st.subheader("Umidade vs. Sensação Térmica")
            fig_scatter = px.scatter(
                df_filtrado,
                x="sensacao_termica",
                y="umidade",
                color="cidade",
                size="velocidade_vento",
                hover_name="cidade",
                labels={
                    "sensacao_termica": "Sensação Térmica (°C)",
                    "umidade": "Umidade (%)"
                }
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

    with tab3:
        st.header("Dados Climáticos Detalhados")
        st.dataframe(df_filtrado)