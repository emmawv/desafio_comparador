import streamlit as st
import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt

# Título de la página
st.title("Captura de Imagen y OCR con OpenCV y EasyOCR")

# Componente de Streamlit para usar la cámara web
img_file = st.camera_input("Toma una foto")

# Verificar si la imagen ha sido capturada
if img_file is not None:
    # Convertir la imagen capturada en bytes a un formato que OpenCV pueda utilizar
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # =============================
    # Algoritmo de OpenCV y EasyOCR (el que me pasaste)
    # =============================

    # Procesar la imagen con EasyOCR
    reader = easyocr.Reader(['es'], gpu=False)  # Cambiar a GPU=True si tienes una GPU disponible
    text_ = reader.readtext(img)

    # Dibujar las cajas delimitadoras y el texto en la imagen
    for t in text_:
        bbox, text, score = t
        cv2.rectangle(img, bbox[0], bbox[2], (255, 0, 0), 2)  # Dibujar rectángulo
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)  # Agregar texto

    # Mostrar la imagen procesada con los textos detectados
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Imagen procesada", use_column_width=True)

    # Mostrar el texto extraído en la aplicación
    extracted_text = "\n".join([t[1] for t in text_])
    st.text("Texto extraído:")
    st.write(extracted_text)

    # Si quieres mostrar la imagen en Matplotlib con los textos detectados
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Eliminar los ejes
    st.pyplot(fig)  # Mostrar la imagen procesada usando Matplotlib
