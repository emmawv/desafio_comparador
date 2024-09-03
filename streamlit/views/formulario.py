import streamlit as st
import pandas as pd
import os

#seteo rutas
file_path = '../Datos/datos_tarifas.csv'   # ruta del archivo
if not os.path.exists(os.path.exists(file_path)):         # crea la carpeta
    os.makedirs(os.path.exists(file_path))




#Streamlit

st.title('Introduce tus datos manualmente')

potencia = st.number_input('¿Cuál es tu término de potencia?')
st.write('Has introducido:', potencia)

consumo = st.number_input('¿Cuál es tu consumo para este período?')
st.write('Has introducido:', consumo)

#faltan más datos de factura: precios, peajes...


if st.button('Calcula la mejor tarifa'):            # Calcular la tarifa y guardar los valores
    nuevo_df = pd.DataFrame({
        'Termino de potencia': [potencia],
        'Termino de consumo': [consumo]
    })
    
    if os.path.exists(file_path):
        df_existente = pd.read_csv(file_path)
        df_actualizado = pd.concat([df_existente, nuevo_df], ignore_index=True)
    else:
        df_actualizado = nuevo_df
    
    df_actualizado.to_csv(file_path, index=False)
    
    st.success('Datos guardados correctamente en el archivo. Calculando la mejor tarifa para ti.')
