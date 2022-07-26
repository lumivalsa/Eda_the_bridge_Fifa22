# importar librerías
from tkinter import CENTER
import streamlit as st
import function_fifa22 as ft
from PIL import Image


# configurar la página
ft.config_page()


# menú
st.sidebar.image('logo.png',width=100)
menu = st.sidebar.selectbox('Selecciona la página',['Introduccion','Datos','Jugadores', 'Otros Cuadros'])

# cargas los datos
path = 'Data_Fifa.csv'
df = ft.cargar_datos(path)

path2= 'players.csv'
df2= ft.jugadores(path2)

#Contenido
if menu == 'Introduccion':
    ft.Introduccion()
elif menu == 'Datos':
    ft.datos(df)
elif menu=='Jugadores': 
    ft.Jugadores(df,df2)
else:
    ft.Otros_cuadros()
