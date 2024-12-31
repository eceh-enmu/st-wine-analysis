"""
Streamlit apps are designed to reload whenever there is a change in the script or user interaction.
This behavior is inherent to Streamlit's architecture, which is built around a reactive programming model.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSS
css_path = "css/styles.css"
with open(css_path) as f:
    st.html(f"<style>{f.read()}</style>")

# Initialize session state to prevent reexecuting
if "dataset" not in st.session_state:
    st.session_state.dataset = None
if "df" not in st.session_state:
    st.session_state.df = None
if "qual" not in st.session_state:
    st.session_state.qual = None
if "column_x" not in st.session_state:
    st.session_state.column_x = None
if "column_y" not in st.session_state:
    st.session_state.column_y = None

st.header("Select your dataset")

# File uploader
dataset = st.file_uploader("Select dataset", type=['csv'])

# If a new dataset is uploaded, store it in session state
if dataset is not None:
    st.session_state.dataset = dataset
    st.session_state.df = pd.read_csv(dataset, sep=None)

# If a dataset is already loaded, use it
if st.session_state.dataset is not None:
    details = {
        "filename": st.session_state.dataset.name,
        "type": st.session_state.dataset.type,
        "size": st.session_state.dataset.size
    }
    st.json(details)

    # Display the dataframe
    st.dataframe(st.session_state.df.head())

    # Plots
    st.header("Plots")
    counts = st.session_state.df.groupby('quality').count().reset_index()
    fig = px.pie(st.session_state.df, names='quality', title='Wine Quality Distribution')
    st.plotly_chart(fig)

    # Select a quality
    qual_levels = sorted(st.session_state.df['quality'].unique().tolist())
    st.session_state.qual = st.select_slider(
        'Select the quality',
        qual_levels,
        value=st.session_state.qual if st.session_state.qual else qual_levels[0]
    )
    filtered_df = st.session_state.df[st.session_state.df['quality'] == st.session_state.qual]

    # Select columns
    columns = st.session_state.df.columns
    st.session_state.column_x = st.selectbox(
        'Select a column for x-axis',
        columns[:-1],
        index=columns[:-1].tolist().index(st.session_state.column_x) if st.session_state.column_x else 0
    )
    st.text(f"You selected {st.session_state.column_x}")

    st.session_state.column_y = st.selectbox(
        'Select a column for y-axis',
        columns[:-1],
        index=columns[:-1].tolist().index(st.session_state.column_y) if st.session_state.column_y else 0
    )
    st.text(f"You selected {st.session_state.column_y}")

    # Plot
    fig = px.scatter(
        filtered_df,
        x=st.session_state.column_x,
        y=st.session_state.column_y,
        title=f'Plot of {st.session_state.column_x} vs {st.session_state.column_y}'
    )
    st.plotly_chart(fig)