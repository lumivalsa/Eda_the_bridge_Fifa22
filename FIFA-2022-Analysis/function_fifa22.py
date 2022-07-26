 # importar librerías
from doctest import DocFileSuite
from tabnanny import check
from turtle import color, width
from matplotlib import interactive
import streamlit.components.v1 as components
import streamlit as st # !pip install Streamlit
from PIL import Image # !pip install Pillow
import pandas as pd
import texto as te
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# configurar la página
def config_page():
    st.set_page_config(
        page_title = 'EDA FIFA 22',
        page_icon = ':soccer:',
        layout = 'wide'
    )

# caché
st.cache(suppress_st_warning=True)

# cargar los datos
def cargar_datos(path):
    df = pd.read_csv(path)
    return df

def jugadores(path2):
    df2 = pd.read_csv(path2)
    return df2

# Introduccion
def Introduccion():
    st.write("<h1 style='text-align: center; color: red;'>EDA FIFA22</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: black;'>The Bridge Tech </h2>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center; color: red;'>Luis Valverde </h2>", unsafe_allow_html=True)
    img = Image.open('fifa22.jpg')
    st.image(img,use_column_width='FIFA22')
    
    with st.expander('Introducción'):
        st.write(te.text_analisis)
    with st.expander('Sobre FIFA22'):
        st.write(te.texto_about)
        video1 = open('clip_fifa22.mp4','rb')
        st.video(video1)
    with st.expander('Acerca de la Base de Datos'):
        st.write(te.text_datos)
pass

# DATOS
def datos(df):
    st.title("Analizando Base de Datos de FIFA 22")
    st.write(df)
    st.subheader("Hipotesis 1:")
    st.text(te.Hipo1)
    hipo=pd.DataFrame(df.query(('Potential>75') and ('Overall>71')))
    gru= hipo.groupby('Nationality')['ID'].count().head(30)
    st.bar_chart(gru)
    img3 = Image.open('pai_jug.jpg')
    st.image(img3,use_column_width='pai_jug',width= 500)
    st.text(te.Resul1)
    st.subheader("Hipotesis 2:")
    st.text(te.Hipo2)
    Hipo2=df['Nationality'].value_counts().head(80)
    st.bar_chart(Hipo2)
     
def Jugadores(df,df2):   
    st.title("Análisis por jugadores")
    st.write(df2)
    img = Image.open('positionsmap.jpg')
    st.image(img,use_column_width='Positions',width= 1000)
    st.header("Hipotesis 3:")
    st.text(te.Hipo3)
    best_player=df2.iloc[df2.groupby(df2['Position'])['media_puntaje'].idxmax()][['Position', 'Name', 'Age', 'Club', 'Nationality']]
    st.write(best_player)
    st.header("Hipotesis 4:")
    st.text(te.Hipo4)
    total_salarios= df.groupby('Nationality')['Wage'].max()
    st.bar_chart(total_salarios)

def Otros_cuadros(df):
    fig, ax = plt.subplots()
    plt.figure(figsize=(20,10))
    st.write(fig)
    mapa = sns.heatmap(df[['Age', 'Overall', 'Potential', 'Value', 'Wage',
                    'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl', 
                    'Composure', 'Crossing','Dribbling', 'FKAccuracy', 'Finishing', 
                    'HeadingAccuracy', 'Interceptions','International Reputation',
                    'Jumping', 'LongPassing', 'LongShots',
                    'Marking', 'Penalties', 'Position', 'Positioning',
                    'ShortPassing', 'ShotPower','SlidingTackle',
                    'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',
                    'Volleys']].corr(), annot=True, cmap='Blues')
    
    sns.heatmap(df.corr(), ax=ax)





