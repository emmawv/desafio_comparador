import streamlit as st
import os
import re
import PyPDF2

st.title('Aquí puedes cargar tu factura')

# Subir archivo PDF
uploaded_file = st.file_uploader('Sube tu factura en formato PDF', type='pdf')

# Si el archivo ha sido subido
if uploaded_file is not None:
    
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
    
    st.write(f"Archivo guardado en correctamente.")
    
    # Función para extraer texto del PDF
    def extraer_datos(pdf_file_path):
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            texto = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto += page.extract_text()
        return texto  # Retorna el texto extraído

    # Extraer el texto del archivo subido
    texto_extraido = extraer_datos(file_path)

    # Mostrar el texto extraído en la aplicación
    st.write("Texto extraído del PDF correctamente.")

    # Función para extraer el número de "Total a pagar"
    def extraer_total_a_pagar(texto):
        # Usar expresión regular para encontrar patrones de "Total a pagar" seguido de un número
        patron = r"(Total( a pagar)?:?\s?€?\s?)(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))"
        coincidencias = re.search(patron, texto, re.IGNORECASE)
        
        if coincidencias:
            return coincidencias.group(3)  # Retornar solo el número del total
        else:
            return "No se encontró el total a pagar."

    # Extraer el total a pagar del texto
    total_a_pagar = extraer_total_a_pagar(texto_extraido)

    # Mostrar el total a pagar en la aplicación
    
    st.subheader("Datos importantes de la factura")

    
    st.write("Total a pagar encontrado:")
    st.write(total_a_pagar)
