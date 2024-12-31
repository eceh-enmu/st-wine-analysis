import streamlit as st
from PIL import Image

logo = Image.open("images/wine.jpg")


# Load CSS
css_path = "css/styles.css"
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1>My Streamlit App</h1>", unsafe_allow_html=True)

container1 = st.container()
with container1:
    left_column, right_column = st.columns(2)
    text = """This app is a Wine Analysis Dashboard designed to provide wine enthusiasts, 
    sommeliers, and data analysts with a comprehensive tool to explore and visualize wine datasets. 
    Built using Streamlit, the app allows users to upload a CSV file containing wine-related data, 
    such as quality ratings, chemical properties, and flavor profiles. 
    Once the dataset is uploaded, the app dynamically generates interactive visualizations, 
    including pie charts to display wine quality distributions and scatter plots to analyze relationships 
    between different attributes like acidity, alcohol content, and pH levels. Users can filter the data by 
    specific quality levels and select custom axes for plotting, enabling deeper insights into the factors 
    that influence wine quality. The dashboard is designed to be intuitive and user-friendly, with a clean 
    interface and responsive design. \n\nWhether you're a wine producer looking to optimize your processes or a 
    connoisseur exploring trends, this app provides a powerful yet accessible platform for data-driven wine 
    analysis."""

    with left_column:
        st.title("Wine Analysis")
        st.html(f"<p>{text}</p>")


    with right_column:
        st.image(logo)