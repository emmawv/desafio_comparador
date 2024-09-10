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

    page = "views/formulariocopy.py",
    title = 'Rellena el formulario',
    icon = ":material/mode:"
)

camara = st.Page(

    page = "views/camara.py",
    title = 'Utiliza tu cámara',
    icon = ":material/photo_camera:"
)

pg = st.navigation(pages=[about_page, sit_mercado, carga_factura, formulario , camara, graf ])

pg.run()