import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Título de la aplicación
st.title('Reconocimiento de Rostros en Foto')

# Captura de imagen de la cámara
uploaded_file = st.camera_input("Haz una foto a tu factura")

if uploaded_file is not None:
    # Leer la imagen desde el archivo cargado
    image = Image.open(uploaded_file)

    # Convertir la imagen a formato numpy array
    image_np = np.array(image)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Cargar el clasificador en cascada para detección de rostros
    cascada_rostro_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    cascada_rostro = cv2.CascadeClassifier(cascada_rostro_path)

    # Verificar si el clasificador se cargó correctamente
    if cascada_rostro.empty():
        st.error(f"No se pudo cargar el clasificador en cascada desde la ruta: {cascada_rostro_path}")
    else:
        # Detectar rostros en la imagen
        rostros = cascada_rostro.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Dibujar rectángulos alrededor de los rostros detectados
        for (x, y, w, h) in rostros:
            cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar la imagen con los rostros detectados en Streamlit
        st.image(image_np, channels="BGR")
