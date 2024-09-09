import streamlit as st
import plotly.express as px
import pandas as pd

# Cargar el conjunto de datos Iris
iris_df = px.data.iris()

# Configurar la aplicación Streamlit
st.title('Gráfico del mercado: Iris Dataset')

# Crear un selector para filtrar por tipo de flor
tarifas = st.selectbox(
    'Selecciona el tipo de flor:',
    options=['Todas'] + iris_df['species'].unique().tolist()
)

# Filtrar el DataFrame según la tarifas seleccionada
if tarifas != 'Todas':
    iris_df = iris_df[iris_df['species'] == tarifas]

# Crear el gráfico de dispersión
basic_scatter_fig = px.scatter(
    iris_df, 
    x='sepal_width', 
    y='sepal_length', 
    color='species', 
    size='petal_length', 
    symbol='species',
    title="Gráfico de Dispersión del Dataset Iris"
)

# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(basic_scatter_fig)


file_path = pd.read_csv('../Datos/database_desafio.csv' )
database_desafio = pd.read_csv(file_path)

# Eliminar espacios en blanco de los nombres de las columnas
database_desafio.columns = database_desafio.columns.str.strip()

# Configurar la aplicación Streamlit
st.title('Gráfico del mercado: Tarifas')

# Verificar las columnas disponibles
st.write("Columnas disponibles en el DataFrame:")
st.write(database_desafio.columns)

# Crear un selector para filtrar por compañia
compania = st.selectbox(
    'Selecciona la compañía:',
    options=['Todas'] + database_desafio['compania'].unique().tolist()
)

# Filtrar el DataFrame según la compañía seleccionada
if compania != 'Todas':
    filtered_df = database_desafio[database_desafio['compania'] == compania]
else:
    filtered_df = database_desafio

# Crear el gráfico de dispersión
basic_scatter_fig = px.scatter(
    filtered_df,
    x='tp_punta_euros/kwh/dia',  # Ajusta las columnas según tus datos
    y='tp_valle_euros/kwh/dia',   # Ajusta las columnas según tus datos
    color='compania',  # Color por compañía
    size='peaje_ener_punta_tdc',  # Ajusta según tus datos
    symbol='compania',  # Símbolo por compañía
    title="Gráfico de Dispersión de Tarifas"
)

# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(basic_scatter_fig)