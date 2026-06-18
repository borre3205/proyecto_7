import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header('Análisis Exploratorio de Datos (EDA) - Anuncios de coches')

car_data = pd.read_csv('vehicles_us.csv')

# Inicializamos el estado si no existe
if 'hist_check' not in st.session_state:
    st.session_state['hist_check'] = False
if 'scatter_check' not in st.session_state:
    st.session_state['scatter_check'] = False

# Callbacks: cuando se activa uno, desactivan el otro
def activar_hist():
    if st.session_state['hist_check']:
        st.session_state['scatter_check'] = False

def activar_scatter():
    if st.session_state['scatter_check']:
        st.session_state['hist_check'] = False

st.checkbox('Mostrar histograma', key='hist_check', on_change=activar_hist)
st.checkbox('Mostrar scatter plot', key='scatter_check', on_change=activar_scatter)

if st.session_state['hist_check']:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

if st.session_state['scatter_check']:
    st.write('Creación de un scatter plot para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Precio vs Kilometraje')
    st.plotly_chart(fig, use_container_width=True)