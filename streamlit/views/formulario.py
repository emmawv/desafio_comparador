import streamlit as st

st.title('Introduce tus datos manualmente')

potencia = st.number_input(
'¿Cuál es tu término de potencia?',
)

st.write('Has introducido:', potencia)
consumo = st.number_input(
'¿Cuál es tu consumo para este período?',
)

st.write('Has introducido:', consumo)


st.button('Calcula la mejor tarifa')


#https://kopuru.com/desarrollo-y-despliegue-de-modelo-de-reconocimiento-de-digitos-con-streamlit/#:~:text=Para%20mostrar%20un%20bot%C3%B3n%20en,en%20caso%20contrario%20devuelve%20False.
