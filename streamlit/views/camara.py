import streamlit as st
import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt

# Título de la página
st.title("¡Haz una foto a tu factura!")

# Componente de Streamlit para usar la cámara web
img_file = st.camera_input("")

# Verificar si la imagen ha sido capturada
if img_file is not None:
    # Convertir la imagen capturada en bytes a un formato que OpenCV pueda utilizar
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    reader = easyocr.Reader(['es'], gpu=False, )  
    text_ = reader.readtext(img)

   
    for t in text_:
        bbox, text, score = t
        cv2.rectangle(img, bbox[0], bbox[2], (240, 50, 0), 2)  # Dibujar rectángulo
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (0, 10, 250), 2)  # Agregar texto

   
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Imagen procesada", use_column_width=True)

    
    extracted_text = "\n".join([t[1] for t in text_])
    st.text("Texto extraído:")
    st.write(extracted_text)

    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  
    st.pyplot(fig)  
