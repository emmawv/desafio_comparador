import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import time
from datetime import date


# Cargar el conjunto de datos Iris
df = pd.read_csv('../Datos/resultados.csv')
df = df.drop_duplicates(subset=['tarifa'])
datos_formulario = pd.read_csv(r'../Datos/datos_tarifas.csv')

datos_formulario['Consumo total (kWh)'] = datos_formulario['Consumo en punta (kWh)'] + datos_formulario['Consumo en llano (kWh)'] + datos_formulario['Consumo en valle (kWh)']
ultimo_consumo_total = datos_formulario['Consumo total (kWh)'].iloc[-1]


# Configurar la aplicación Streamlit

fecha_actual = date.today().strftime('%d-%m-%Y')
st.title(f'Comparativa compañías más baratas a {fecha_actual}')




#RELLENAR
st.write (f'Estas son las tarifas deConsiderando tu consumo de {ultimo_consumo_total} kW/h.')

# Crear un selector para filtrar por tipo de flor
tarifas = st.selectbox(
    'Selecciona la compañía:',
    options=['Todas'] + df['compania'].unique().tolist()
)

# Filtrar el DataFrame según la tarifas seleccionada
if tarifas != 'Todas':
    df = df[df['compania'] == tarifas]

trf_grf = df.sort_values('total_factura').head(5)

# Crear el gráfico de dispersión

fig = px.bar(
  trf_grf, 
  x="tarifa", 
  y=["coste_valle", "coste_llano", "coste_punta"], 
  color_discrete_map={
    'coste_valle': '#F29D52',
    'coste_llano': '#F2C572',
    'coste_punta': '#F2EAC2'
    },
  labels={"compania": "Compañía", "value": "Coste por tramos"},
  custom_data=['total_factura','compania']
)
fig.update_traces(hovertemplate=('<b>Compañia:</b> %{customdata[1]} <br><b>Tarifa:</b> %{x} <br><b>Coste en tramo:</b> %{y:.2f} <br><b>Total factura:</b> %{customdata[0]:.2f}')+"<extra></extra>")
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.96,
    xanchor="left",
    x=0.005,
    title="Rango"
),
title={
        'text': "Comparativa compañias más baratas",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces({'name': 'Coste Valle'}, selector={'name': 'coste_valle'})
fig.update_traces({'name': 'Coste Llano'}, selector={'name': 'coste_llano'})
fig.update_traces({'name': 'Coste Punta'}, selector={'name': 'coste_punta'})


fig1 = px.bar(
  trf_grf, 
  x="tarifa", 
  y="total_factura", 
  color_continuous_scale='sunset',
  color="total_factura",
  custom_data=['compania'],
  labels={"tarifa": "Tarifas", "total_factura": "Precio factura"},
)

fig1.update_layout(
  coloraxis_showscale=False, 
  yaxis_range=[round(trf_grf["total_factura"].min() - 1, 0), round(trf_grf["total_factura"].max() + 1)],
  title={
        'text': "Comparativa compañias más baratas",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
  )
fig1.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Precio factura:</b> %{y:.2f}')


fig2 = px.scatter(df, x="tarifa", 
  y="total_factura", color_continuous_scale='sunset',
  color="total_factura", hover_data=['tarifa', 'compania', 'total_factura'], custom_data=['compania'], labels={"tarifa": "Tarifa", "total_factura": "Precio factura"})
fig2.update_layout(coloraxis_showscale=False, title={
        'text': "Comparativa compañias",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig2.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Precio factura:</b> %{y:.2f}')
fig2.update_xaxes(tickangle=45)


# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(fig)
st.plotly_chart(fig1)

st.plotly_chart(fig2)





import streamlit as st
import pandas as pd
from datetime import time
from datetime import date
import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import time
from datetime import date



# Cargar el conjunto de datos Iris
df = pd.read_csv('../Datos/resultados.csv')
df =df.drop_duplicates(subset=['tarifa'])
# Configurar la aplicación Streamlit

fecha_actual = date.today().strftime('%d-%m-%Y')
st.title(f'Comparativa de mercado {fecha_actual}')




fig2 = px.scatter(df, x="tarifa", 
  y="total_factura", color_continuous_scale='sunset',
  color="total_factura", hover_data=['tarifa', 'compania', 'total_factura'], custom_data=['compania'], labels={"tarifa": "Tarifa", "total_factura": "Precio factura"})
fig2.update_layout(width=1500, height=1200,
    
    
    coloraxis_showscale=False, title={
        'text': "Comparativa compañias",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig2.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Precio factura:</b> %{y:.2f}')
fig2.update_xaxes(tickangle=45)


st.plotly_chart(fig2)