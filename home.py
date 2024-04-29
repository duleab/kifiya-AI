import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to upload CSV file and display DataFrame
def upload_and_display_data():
    st.subheader("Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("DataFrame")
        st.write(data)
        return data

# Function to display slider
def display_slider(data):
    st.subheader("Slider")
    if data is not None:
        numeric_columns = data.select_dtypes(include=['int', 'float']).columns
        if len(numeric_columns) == 0:
            st.write("No numeric columns found in the DataFrame.")
        else:
            column_name = st.selectbox("Select a numeric column", numeric_columns)
            min_val = data[column_name].min()
            max_val = data[column_name].max()
            default_val = (min_val + max_val) // 2 if min_val != max_val else min_val
            val = st.slider("Select a value", min_val, max_val, default_val)
            st.write("Selected value:", val)

# Function to display plot
def display_plot(data):
    st.subheader("Plot")
    if data is not None:
        numeric_columns = data.select_dtypes(include=['int', 'float']).columns
        if len(numeric_columns) == 0:
            st.write("No numeric columns found in the DataFrame.")
        else:
            column_name = st.selectbox("Select a numeric column for x-axis", numeric_columns)
            plt.figure(figsize=(6, 4))
            sns.histplot(data[column_name], kde=True)
            st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable warning
            st.pyplot()  # Display plot

# Set page configuration
st.set_page_config(
    page_title="Streamlit Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "Data", "Visualization"])

# Display selected page
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Streamlit Dashboard!")

elif page == "Data":
    st.title("Data Page")
    data = upload_and_display_data()
    display_slider(data)

elif page == "Visualization":
    st.title("Visualization Page")
    data = upload_and_display_data()
    display_plot(data)
