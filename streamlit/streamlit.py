import streamlit as st


about_page = st.Page(
    page = "views/about_page.py",
    title = "Introducción: Entiende tu factura",
    icon = ":material/account_circle:",
    default= True
)

project_1_page = st.Page(
    page = "views/mercado.py",
    title = 'Situación del mercado',
    icon = ":material/bar_chart:",
)

project_2_page = st.Page(
    page = "views/grafica.py",
    title = "Gráfico",
    
    icon = ":material/smart_toy:"
)
carga_factura = st.Page(


    page = "views/carga.py",
    title = 'Carga tu factura',
    icon = ":material/add_link:"
)

formulario_factura = st.Page(

    page = "views/formulario.py",
    title = 'Rellena el formulario',
    icon = ":material/add_link:"
)
camara = st.Page(

    page = "views/camara.py",
    title = 'Utiliza tu cámara',
    icon = ":material/add_link:"
)

pg = st.navigation(pages=[about_page, project_1_page, project_2_page, carga_factura, formulario_factura, camara])

pg.run()