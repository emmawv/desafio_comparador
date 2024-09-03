import streamlit as st
import pandas as pd
import os

#seteo rutas
file_path = '../Datos/datos_tarifas.csv'   # ruta del archivo
if not os.path.exists(os.path.exists(file_path)):         # crea la carpeta
    os.makedirs(os.path.exists(file_path))




#Streamlit

st.title('Introduce tus datos manualmente')

disc_horar = st.selectbox('¿Tienes una tarifa con discriminación horaria?',('Sí','No'),)
st.write('Discriminación horaria:', disc_horar)


potencia_punta = st.selectbox('¿Cuál es tu término de potencia en período punta?', ('3,3','4,6','5,5' , '6,9'))
st.write('Potencia, período punta:', potencia_punta)


potencia_valle = st.selectbox('¿Cuál es tu término de potencia en período valle?', ('3,3','4,6','5,5' , '6,9'))
st.write('Potencia, período punta:', potencia_valle)

consumo = st.number_input('¿Cuál es tu término de consumo? En kW/h')
st.write('Consumo total:', consumo)

#faltan más datos de factura: precios, peajes...


if st.button('Calcula la mejor tarifa'):            # Calcular la tarifa y guardar los valores
    nuevo_df = pd.DataFrame({
        'Discriminacion horaria': [disc_horar],
        'Termino de potencia en valle': [potencia_valle],
        'Termino de potencia en punta': [potencia_punta],
        'Termino de consumo': [consumo]
    })
    
    if os.path.exists(file_path):
        df_existente = pd.read_csv(file_path)
        df_actualizado = pd.concat([df_existente, nuevo_df], ignore_index=True)
    else:
        df_actualizado = nuevo_df
    
    df_actualizado.to_csv(file_path, index=False)
    
    st.success('Datos guardados correctamente. Calculando la mejor tarifa para ti.')
