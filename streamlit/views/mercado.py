import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px


df = pd.read_csv('../Datos/resultados.csv')
df = df.drop_duplicates(subset=['tarifa'])

fecha_actual = date.today().strftime('%d-%m-%Y')
st.title(f'Comparativa de mercado a día {fecha_actual}')

col1, = st.columns(1)  

with col1:
    fig2 = px.scatter(df, 
                      x="tarifa", 
                      y="total_factura", 
                      color_continuous_scale='sunset',
                      color="total_factura", 
                      hover_data=['tarifa', 'compania', 'total_factura'], 
                      custom_data=['compania'], 
                      labels={"tarifa": "Tarifa", "total_factura": "Precio factura"})

    fig2.update_layout(

        coloraxis_showscale=False, 
        title={
            'text': "Comparativa compañias",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    # Personalizar las trazas y el estilo de los ejes
    fig2.update_traces(hovertemplate='<b>Compañia:</b> %{customdata[0]} <br><b>Tarifa:</b> %{x} <br><b>Precio factura:</b> %{y:.2f}')
    fig2.update_xaxes(tickangle=45)

    st.plotly_chart(fig2, use_container_width=True)  
