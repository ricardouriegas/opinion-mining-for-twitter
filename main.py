import streamlit as st
import matplotlib.pyplot as plt

# app title
st.title("Twitter Analyzer")

# description
st.write("Given a topic, this app will analyze the sentiment of tweets about it and will return a graph about it.")

# text input
textField = st.text_input("Topic to analyze: ", "Python")

# static data (just for simulation)
data = {
    "Positive": 45,
    "Negative": 30,
    "Neutral": 25
}

# show the result in a pie chart
if textField:
    # header in page
    st.subheader(f"Result for the topic: {textField}")
    
    # plot creation 
    labels = data.keys()
    values = data.values()
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(f"Social Acceptance Level for {textField}") # title of the plot

    # show the plot
    st.pyplot(fig)

