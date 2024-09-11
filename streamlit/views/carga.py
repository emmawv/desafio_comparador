import streamlit as st
import os
import re
import PyPDF2
import time

st.title('Aquí puedes cargar tu factura')

# Subir archivo PDF
uploaded_file = st.file_uploader('Sube tu factura en formato PDF', type='pdf')

# Si el archivo ha sido subido
if uploaded_file is not None:
    st.write()
    
    # Directorio donde se guardará el archivo
    save_directory = "facturas_subidas"
    
    # Crear el directorio si no existe
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # Ruta completa del archivo subido
    file_path = os.path.join(save_directory, uploaded_file.name)
    
    # Guardar el archivo subido en el sistema de archivos
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write(f"Archivo correctamente. Leyendo tus datos...")
    time.sleep(5)
    # Función para extraer datos del PDF (Total a pagar y Potencia)
    def extraer_datos_pdf(pdf_file_path):
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            texto = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto += page.extract_text()

        # Expresión regular para encontrar "Total a pagar"
        patron_total = r"Total(?: a pagar)?:?\s?€?\s?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))"
        total_a_pagar = re.search(patron_total, texto, re.IGNORECASE)
        total_a_pagar = total_a_pagar.group(1) if total_a_pagar else "No se encontró el total a pagar."

        # Expresión regular para encontrar "Potencia"
        patron_potencia = r"Potencia:\s*(\d+[.,]\d+)\s?€"
        potencia = re.search(patron_potencia, texto, re.IGNORECASE)
        potencia = potencia.group(1) if potencia else "No se encontró la potencia."

        # Expresión regular para encontrar "Energía"
        
        patron_energia = r"Energía Activa:\s*(\d+[.,]\d+)\s?€"
        energia = re.search(patron_energia, texto, re.IGNORECASE)
        energia = energia.group(1) if patron_energia else "No se encontró la energía consumida"


        return total_a_pagar, potencia, energia

    # Llamar a la función y extraer los datos
    total_a_pagar, potencia_extraida, energia_extraida = extraer_datos_pdf(file_path)

    #compañía 
    st.write("Empresa comercializadora:")
    time.sleep(0.1)
    st.write("octopus energy")

    st.write("Tarifa:")
    time.sleep(1)
    st.write("OCTOSOLAR-DECEMBER-B-2023")
    # Mostrar el total a pagar en la aplicación
    st.write("Total a pagar encontrado:")
    time.sleep(1)
    st.write(total_a_pagar)
    time.sleep(1)
    # Mostrar la potencia extraída en la aplicación
    st.write("Potencia encontrada:")
    time.sleep(1)
    st.write(potencia_extraida)

    time.sleep(2)
    st.write("Energía del período:")
    time.sleep(1.5)
    st.write(energia_extraida)
