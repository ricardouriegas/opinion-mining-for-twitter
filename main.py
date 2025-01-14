import streamlit as st
import matplotlib.pyplot as plt

# app title
st.title("Twitter Analyzer")

# description
st.write("Given a topic, this app will analyze the sentiment of tweets about it and will return a graph about it.")

# Entrada de texto
textField = st.text_input("Topic to analyze: ", "Python")

# static data (just for simulation)
data = {
    "Positive": 45,
    "Negative": 30,
    "Neutral": 25
}

# Mostrar los datos en una gráfica
if textField:
    st.subheader(f"Result for the topic: {textField}")
    
    # Crear la gráfica
    labels = data.keys()
    values = data.values()
    # fig, ax = plt.subplots()
    # ax.bar(labels, values, color=['green', 'red', 'gray'])
    # ax.set_title("Nivel de aceptación social")
    # ax.set_ylabel("Cantidad de Tweets")
    
    # # Mostrar la gráfica
    # st.pyplot(fig)

    # grafica de pastel
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(f"Social Acceptance Level for {textField}")
    st.pyplot(fig)


    # Mostrar datos
    # st.write("**Distribución:**")
    # st.json(datos)

