import cv2
import numpy as np

# Cargar la imagen en la que se realizará la detección de texto
image = cv2.imread(r'../images/asig.jpg')


# Dimensiones originales de la imagen
orig = image.copy()
(H, W) = image.shape[:2]

# Establecer la nueva altura y anchura para la imagen
(newW, newH) = (320, 320)  # El modelo EAST requiere que las dimensiones sean múltiplos de 32
rW = W / float(newW)
rH = H / float(newH)

# Redimensionar la imagen
image = cv2.resize(image, (newW, newH))

# Cargar el modelo preentrenado EAST
net = cv2.dnn.readNet('frozen_east_text_detection.pb')

# Crear un blob a partir de la imagen redimensionada
blob = cv2.dnn.blobFromImage(image, 1.0, (newW, newH), (123.68, 116.78, 103.94), swapRB=True, crop=False)

# Configurar la red para utilizar el blob como entrada
net.setInput(blob)

# Definir las dos capas de salida que necesitamos del modelo EAST
layerNames = [
    "feature_fusion/Conv_7/Sigmoid",  # Puntaje de la detección
    "feature_fusion/concat_3"         # Coordenadas del cuadro delimitador
]

# Realizar la detección
(scores, geometry) = net.forward(layerNames)

# Función para extraer las cajas delimitadoras de las predicciones
def decode_predictions(scores, geometry, min_confidence=0.5):
    (numRows, numCols) = scores.shape[2:4]
    boxes = []
    confidences = []

    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        for x in range(0, numCols):
            if scoresData[x] < min_confidence:
                continue

            # Calcular el offset desde el centro de la caja
            (offsetX, offsetY) = (x * 4.0, y * 4.0)

            # El ángulo de rotación y calcular las dimensiones del rectángulo
            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            # Calcular las coordenadas de la caja delimitadora
            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)

            boxes.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])

    return (boxes, confidences)

# Extraer las cajas delimitadoras y sus respectivas confianzas
(boxes, confidences) = decode_predictions(scores, geometry)

# Aplicar supresión de no máximos para suprimir las cajas más débiles
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Redimensionar las cajas de vuelta al tamaño original de la imagen
if len(indices) > 0:
    for i in indices.flatten():
        (startX, startY, endX, endY) = boxes[i]

        # Redimensionar las coordenadas
        startX = int(startX * rW)
        startY = int(startY * rH)
        endX = int(endX * rW)
        endY = int(endY * rH)

        # Dibujar la caja delimitadora en la imagen original
        cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Mostrar la imagen final con las detecciones de texto
cv2.imshow("Text Detection", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()
