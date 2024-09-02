import streamlit as st
import os
from PIL import Image

st.title('Aquí puedes cargar tu factura')

uploaded_file = st.file_uploader('Sube tu factura', type=['jpeg','jpg','png','pdf'])

if uploaded_file is not None:
    st.write(f"Nombre del archivo: {uploaded_file.name}")
    save_directory = "facturas_subidas"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    file_path = os.path.join(save_directory, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write(f"Archivo guardado en: {file_path}")
