import streamlit as st
import pandas as pd
import os

# Seteo de rutas
file_path = '../Datos/datos_tarifas.csv'  # Ruta del archivo
directory = os.path.dirname(file_path)  # Carpeta de los datos

# Crear la carpeta si no existe
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)

# Streamlit
st.title('Introduce tus datos manualmente')

disc_horar = st.selectbox('¿Tienes una tarifa con discriminación horaria?', ('No', 'Sí'))
st.write('Discriminación horaria:', disc_horar)

potencia_punta = st.selectbox('¿Cuál es tu término de potencia en período punta?', ('3.3', '4.6', '5.5', '6.9'))
st.write('Potencia, período punta:', potencia_punta)

potencia_valle = st.selectbox('¿Cuál es tu término de potencia en período valle?', ('3.3', '4.6', '5.5', '6.9'))
st.write('Potencia, período valle:', potencia_valle)


total = st.number_input('¿Cuál ha sido el total de la factura? En €')
st.write('Total factura:', total)



# Campo de consumo general (solo se habilita si no hay discriminación horaria)
if disc_horar == 'Sí':
    st.warning("Tu consumo está dividido en varios periodos, por lo que no puedes introducir un consumo total.")
    consumo_punta = st.number_input('¿Cuál es tu consumo en período punta? En kWh', min_value=0.0)
    consumo_llano = st.number_input('¿Cuál es tu consumo en período llano? En kWh', min_value=0.0)
    consumo_valle = st.number_input('¿Cuál es tu consumo en período valle? En kWh', min_value=0.0)
    consumo_total = None
else:
    consumo_total = st.number_input('¿Cuál es tu término de consumo total? En kWh', min_value=0.0)
    consumo_punta = None
    consumo_llano = None
    consumo_valle = None

# Botón para calcular la mejor tarifa
if st.button('Calcula la mejor tarifa'):
    # Verificar que los datos estén disponibles
    if consumo_punta is None: consumo_punta = None
    if consumo_llano is None: consumo_llano = None
    if consumo_valle is None: consumo_valle = None
    if consumo_total is None: consumo_total = None

    # Crear DataFrame con discriminación horaria o sin ella
    datos_tarifas = pd.DataFrame({
        'Termino de potencia en valle': [potencia_valle],
        'Termino de potencia en punta': [potencia_punta],
        'Consumo en punta (kWh)': [consumo_punta],
        'Consumo en llano (kWh)': [consumo_llano],
        'Consumo en valle (kWh)': [consumo_valle],
        'Consumo total (kWh)': [consumo_total],
        'Bono social':[bono],
        'Total factura':[total]
    })


    # Comprobar si el archivo ya existe para actualizar o crear uno nuevo
    if os.path.exists(file_path):
        df_existente = pd.read_csv(file_path)
        df_actualizado = pd.concat([df_existente, datos_tarifas], ignore_index=True)
    else:
        df_actualizado = datos_tarifas

    # Guardar el DataFrame actualizado
    df_actualizado.to_csv(file_path, index=False)
    st.success("Datos guardados correctamente.")


#min dataframa
resultados = pd.read_csv("../Datos/resultados.csv")
minimo = resultados[resultados['total_factura'] == resultados['total_factura'].min()].iloc[0]


datos_formulario = pd.read_csv(r'../Datos/datos_tarifas.csv')

consumo_usuario = datos_formulario['Total factura'].tail(1) 
consumo_usuario
st.write(f'Hemos encontrado esta tarifa: {minimo["tarifa"]} de {minimo["compania"]}') #min tarifa para datos dados) 


dif_tarifa = minimo['total_actual'] - minimo['total_factura']

st.write(f'Mejoraría tu tarifa en {dif_tarifa:.2f}€')
