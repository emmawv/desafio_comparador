import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px


df = pd.read_csv('../Datos/tarifas.csv', sep=';')
potencia = (df['tp_punta_euros/kwh/dia'] + df['tp_valle_euros/kwh/dia'])*365  
consumo_2t = df[['tc_8h_euros/kwh/hora', 'tc_16h_euros/kwh/hora']].mean(axis=1)                                    #consumo medio para df 8 y 16
consumo_2t = consumo_2t[consumo_2t > 0]
consumo_3t = df[['tc_valle_euros/kwh/hora','tc_llano_euros/kwh/hora','tc_punta_euros/kwh/hora']].mean(axis=1)           #tienen que salir 48 Consumo medio para tarifa 3 tramos
consumo_3t = consumo_3t[consumo_3t > 0]
consumo_tp = df['termino_consumo_euros/kwh/hora']
consumo_tp = consumo_tp[consumo_tp > 0]
consumo = pd.concat([consumo_2t, consumo_3t,consumo_tp], ignore_index=True)
df['consumo'] = consumo
df['potencia'] = potencia
fecha_actual = date.today().strftime('%d-%m-%Y')


st.title(f'Comparativa de mercado a día {fecha_actual}')
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

mercado = st.selectbox('Selecciona la tarifa que quieres consultar: ', options=['Todas'] + df['mercado'].unique().tolist())

#consumo = datos_formulario['Consumo total (kWh)'].iloc[-1]
if mercado != 'Todas':
    df = df[df['mercado'] == mercado]


compania = st.selectbox('Selecciona la compañia que quieres consultar: ', options=['Todas'] + df['compania'].unique().tolist())

if compania != 'Todas':
    df = df[df['compania'] == compania]




st.title(f'Comparativa de mercado: término de energía.')

col1, = st.columns(1)  

with col1:
    fig2 = px.scatter(df, 
                      x="tarifa", 
                      y="consumo", 
                      color_continuous_scale='sunset',
                      color="consumo", 
                      hover_data=['tarifa', 'compania', 'consumo'], 
                      custom_data=['compania'], 
                      labels={"tarifa": "Tarifa", "consumo": "Precio medio kWh"})

    fig2.update_layout(

        coloraxis_showscale=False, 
        title={
            'text': "Comparativa compañias. Peajes, impuestos y demás conceptos no incluidos",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    # Personalizar las trazas y el estilo de los ejes
    fig2.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Precio medio kWh:</b> %{y:.3f}')
    fig2.update_xaxes(tickangle=45)

    st.plotly_chart(fig2, use_container_width=True)  

st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)



st.title(f'Comparativa de mercado: término de potencia.')
col1, = st.columns(1)  

with col1:
    fig2 = px.scatter(df, 
                      x="tarifa", 
                      y="potencia", 
                      color_continuous_scale='sunset',
                      color="potencia", 
                      hover_data=['tarifa', 'compania', 'potencia'], 
                      custom_data=['compania'], 
                      labels={"tarifa": "Tarifa", "potencia": "Precio anual kWh"})

    fig2.update_layout(

        coloraxis_showscale=False, 
        title={
            'text': "Comparativa compañias. Peajes, impuestos y demás conceptos no incluidos",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    # Personalizar las trazas y el estilo de los ejes
    fig2.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Potencia:</b> %{y:.3f}')
    fig2.update_xaxes(tickangle=45)

    st.plotly_chart(fig2, use_container_width=True)  