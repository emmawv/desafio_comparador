import streamlit as st
import plotly.express as px

iris_df = px.data.iris()


st.title('Ejemplo de gráficos: iris dataset')
basic_scatter_fig = px.scatter(iris_df, x='sepal_width', y='sepal_length', color = 'species', size='petal_length', symbol='species')




st.plotly_chart(basic_scatter_fig)
