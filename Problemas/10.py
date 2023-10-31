import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.title('Visualização de Atendimentos Médicos')
file = st.file_uploader('Carregue o arquivo de atendimentos médicos', type='csv')

if file is not None:
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['just_date'] = df['Date'].dt.date
    df['just_time'] = df['Date'].dt.strftime('%H')

    date_count = df["just_date"].value_counts()
    time_count = df["just_time"].value_counts()

    fig1 = go.Figure(data=go.Bar(x=date_count.index, y=date_count))

    fig1.update_layout(title = 'Quantidade de atendimentos por dia',
                       xaxis_title='Data',
                       yaxis_title='Contagem')
    st.plotly_chart(fig1)

    fig2 = go.Figure(data=go.Bar(x=time_count.index, y=time_count))

    fig2.update_layout(title = 'Quantidade de atendimentos por horário',
                       xaxis_title='Horário',
                       yaxis_title='Contagem')
    st.plotly_chart(fig2)


else:
    st.warning('Por favor, carregue o arquivo de atendimentos médicos.')