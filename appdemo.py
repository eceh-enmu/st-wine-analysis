import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

logo = Image.open("images/wine.jpg")
st.set_page_config(page_title='Wine Analysis',page_icon=logo, # Does not show in Safari
                   #initial_sidebar_state="collapsed")
                   )
# Page setup
main_page = st.Page(
    page="views/main.py",
    title="Main",
    default=True,
)

wine_analysis = st.Page(
    page="views/wine_dashboard.py",
    title="Wine Dashboard",
)

navigation = st.navigation(pages=[main_page, wine_analysis])

def main():
    navigation.run()


if __name__ == "__main__":
    main()