import warnings
import streamlit as st
from PIL import Image
import os
import time
import glob
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Suppress warnings
warnings.filterwarnings("ignore")

# Set the initial page configuration
# st.set_page_config(
#     page_title="Carbon AIQ",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
st.title("Carbon AIQ")
st.info("Mission Statement")

df = pd.read_csv("data/streamlit_data.csv")
    # FROM TABLE_X 
df_dates = pd.read_csv("data/capstone_withDates.csv")

# Initialize session state with the DataFrame
if 'df' not in st.session_state:
    st.session_state.df = df

if 'df_dates' not in st.session_state:
    st.session_state.df_dates = df_dates

# Define the path to your local images
image_folder = "images"
        
# Function to load images from a directory
def load_images(image_folder):
    image_paths = glob.glob(f"{image_folder}/*.jpg")  # You can change the extension based on your images
    images = [(Image.open(image_path), os.path.splitext(os.path.basename(image_path))[0]) for image_path in image_paths]
    return images

# Load images
images = load_images(image_folder)

# Initialize session state
if 'index' not in st.session_state:
    st.session_state.index = 0

# Display the current image
if images:
    current_image, caption = images[st.session_state.index]
    st.image(current_image, use_column_width=True, caption=caption)
   
else:
    st.write("No images found in the specified folder.")

# Update the index for the next image
st.session_state.index = (st.session_state.index + 1) % len(images)
# Add CSS to make the image take the full height
st.markdown(
    """
    <style>
    .fullScreenFrame > img {
        object-fit: cover;
        width: 100%;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display subheaders
st.subheader("What is Carbon Offset")
st.write("A carbon offset is a reduction in emissions of carbon dioxide or other greenhouse gases made in order to compensate for emissions produced elsewhere. By investing in carbon offset projects, such as reforestation or renewable energy, individuals and companies can balance out their own emissions.")

st.subheader("What do we do")
st.write("A paragraph about the problem and solution")

st.subheader("Our data source")
st.write("The data source comes from renowned registries....")

st.subheader("Our Customers")
st.write("About the customers and their usecases")

# Auto-refresh every 3 seconds
time.sleep(3)
st.experimental_rerun()  # Refresh the app to update the displayed image

