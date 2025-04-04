import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
from dataset import df

st.set_page_config(layout="wide")	# Configuração da página
st.title("Analise de vendas")	# Título da página 

aba1, aba2, aba3 = st.tabs(['Dataset', 'Gráficos', 'Mapa'])	# Abas
with aba1:	# Primeira aba
    st.dataframe(df.head(1000))	# Mostra o dataset

with aba2:	# Segunda aba
    # Contar número de reclamações por empresa
    top_empresas = df['empresa'].value_counts().head(10)

    # Plotar gráfico de barras verticais
    plt.figure(figsize=(12, 6))
    top_empresas.plot(kind='bar')
    plt.title('Top 10 Empresas com Mais Reclamações')
    plt.xlabel('Empresa')
    plt.ylabel('Quantidade de Reclamações')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

    # Plotar gráfico de barras horizontais

    top_empresas_resolucoes = pd.DataFrame({
        'empresa': df['empresa'],
        'status': df['status']  # Corrigido aqui também!
    })

    contagem = df.groupby(['empresa', 'status']).size().reset_index(name='frequencia')
    total = contagem['frequencia'].sum()
    contagem['probabilidade'] = contagem['frequencia'] / total

    top10 = contagem.sort_values(by='probabilidade', ascending=False).head(10)
    top10['par'] = top10['empresa'] + ' - ' + top10['status']

    plt.figure(figsize=(10, 6))
    plt.barh(top10['par'], top10['probabilidade'])
    plt.xlabel('Probabilidade')
    plt.title('Top 10 Interseções entre Empresa e Status')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    st.pyplot(plt)