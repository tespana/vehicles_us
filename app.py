import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv('notebooks/vehicles_us.csv') 
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
Scatter_button = st.button('Construir grafico de dispersion')
 
if Scatter_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig2 = px.scatter(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
built_scatter = st.checkbox('Construir grafico de dispersion')

if built_scatter:
    st.write('Construir un grafico de dispersion para la columna odómetro')