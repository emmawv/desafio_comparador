import streamlit as st

about_page = st.Page(
    page = "views/about_page.py",
    title = "Entiende tu factura",
    icon = ":material/account_circle:",
    default= True
)

sit_mercado = st.Page(
    page = "views/mercado.py",
    title = 'Situación del mercado',
    icon = ":material/bar_chart:",
)

graf = st.Page(
    page = "views/g.py",
    title = "Gráfico",
    
    icon = ":material/smart_toy:"
)

carga_factura = st.Page(

    page = "views/carga.py",
    title = 'Carga tu factura',
    icon = ":material/add_link:"
)

formulario = st.Page(

    page = "views/formulario.py",
    title = 'Rellena el formulario',
    icon = ":material/mode:"
)

camara = st.Page(

    page = "views/camara.py",
    title = 'Utiliza tu cámara',
    icon = ":material/photo_camera:"
)




pg = st.navigation(pages=[about_page, sit_mercado, carga_factura, formulario , camara, graf ])

import streamlit as st

# Configuración de la página principal
st.set_page_config(page_title="Compara tu Luz", layout="wide")

# Contenido principal de la página


# Agregar el pie de página al final de la página

pg.run()

st.markdown("""
    <style>
    .footer {
        position: fixed; /* Fija el pie de página en la parte inferior de la página */
        bottom: 0; /* Coloca el pie de página en la parte inferior */
        left: 0;
        width: 100%; /* Asegura que el pie de página ocupe todo el ancho disponible */
        background-color: #5D5F67;
        text-align: center;
        padding: 10px; /* Añade espacio alrededor del texto del pie de página */
        font-size: 12px; /* Ajusta el tamaño de la fuente */
        color: #C5C7C7;
    }
    .footer .heart {
        color: red; /* Color del corazón en rojo */
    }
    </style>
    <div class="footer">
        <p>Hecho con <span class="heart">❤️</span> por Helena, Emma, Jorge y Álvaro.</p>
    </div>
    """, unsafe_allow_html=True)
