import warnings
import streamlit as st
from PIL import Image
import os
import time
import glob
import pandas as pd

# Suppress warnings
warnings.filterwarnings("ignore")

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")

st.title("Carbon AIQ")
st.info("Our mission is to empower individuals and organizations with transformative data that drives actionable insights and fosters sustainability. By unifying and harmonizing data from diverse carbon offset registries into a single, accessible platform, we are leading the way in creating a more transparent and impactful path toward a sustainable future.")

df = pd.read_csv("data/Project_Tab.csv")
df_dates = pd.read_csv("data/Project_Tab_Pivoted.csv")

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

# Create a placeholder for the image
image_placeholder = st.empty()

# Function to display images
def display_images():
    if images:
        current_image, caption = images[st.session_state.index]
        image_placeholder.image(current_image, use_column_width=True, caption=caption)
    else:
        image_placeholder.write("No images found in the specified folder.")

# Display initial image
display_images()

# # Run a loop to update the image every 2 seconds
# while True:
#     time.sleep(2)
#     st.session_state.index = (st.session_state.index + 1) % len(images)
#     display_images()
#     st.experimental_rerun()

# Display subheaders
st.subheader("What is Carbon Offset?")
st.write("A carbon offset is a reduction in emissions of carbon dioxide or other greenhouse gases made in order to compensate for emissions produced elsewhere. By investing in carbon offset projects, such as reforestation or renewable energy, individuals and companies can balance out their own emissions.")

st.subheader("About the Carbon Offset Market")
st.write("In 2023, companies purchased and retired a record 164 million offsets, which was a 6% increase from 2022. The market is evolving rapidly, and some say it could grow to be worth $100 billion a year by 2030-35. However, others say that without regulation, no one would pay for carbon emissions, and that heavy-emitting companies could be criticized for having a right to pollute")
st.write("There are two types of carbon offset markets: voluntary and compliance:")
st.markdown(""" - **Voluntary markets** - These markets are not regulated, and organizations participate based on their own emissions reduction goals. Individuals, companies, and other organizations can participate in voluntary markets, and consumers can buy offsets to compensate for emissions from specific activities, like long flights.
- **Compliance markets** -These markets are created by government regulations to reduce emissions, and some of the most active compliance markets are in Europe and California.""")

st.subheader("Our Tool's Value")
st.write("Carbon AIQ provides immense value through the Berkeley Carbon Trading Project by unifying and harmonizing data from multiple carbon offset registries into a single, accessible database. This platform streamlines data processing through automated pipelines and advanced natural language processing (NL) and classification algorithms to empower environmental researchers with clean, accurate data for informed decision-making. This web interface enhances the value for current users of the Excel version of the database by offering robust visualization tools and comprehensive reports, facilitating advanced research and effective management of carbon offset initiatives. ")

st.subheader("Data Sources")
st.write("Also known as the PROJECT tab from the Current Registry's Excel tool, contains data on roughly 10,000 projects, useful for a project type classification problem and other potential research inquiries. The underlying data for the current registry includes raw data downloaded from American Carbon Registry (ACR), Climate Action Reserve (CAR), Gold Standard, and Verified Carbon Standard. More information on this data can be found in the About BCTP tab.")

st.subheader("Contributors")
st.write("Our team is made up of a team at BCTP as well as UC Berkeley Masters of Data Science (MIDS) candidates completing their Capstone. This team is comprised of knowledgeable Renewable Energy and Carbon offset SMEs, data scientists, data engineers, and front-end developers.")

# Create 4 columns for the team images
col1, col2, col3, col4 = st.columns(4)
with col2:
    st.image("images/team/Barbara.png", caption="Barbara Haya, PhD, Director, Berkeley Carbon Trading Project", use_column_width=True)
with col3:
    st.image("images/team/Aline.png", caption="Aline Abayo, Master’s student at Energy Resource Group at UC Berkeley", use_column_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("images/team/Kevin.png", caption="Kevin Hoang, UC Berkeley MIDS Student", use_column_width=True)
with col2:
    st.image("images/team/Roshni.png", caption="Roshni Tajnekar, UC Berkeley MIDS Student", use_column_width=True)
with col3:
    st.image("images/team/Maggie.png", caption="Maggie Corry, UC Berkeley MIDS Student", use_column_width=True)
with col4:
    st.image("images/team/Roxy.png", caption="Roxy Rong, UC Berkeley MIDS Student", use_column_width=True)

st.subheader("Latest News on the Carbon Offset ")
st.markdown("""
- https://www.nytimes.com/2024/05/28/climate/yellen-carbon-offset-market.html
- https://www.theguardian.com/environment/carbon-offset-projects
- https://www.theguardian.com/environment/article/2024/jul/11/finite-carbon-forest-offsets-analysis
- https://www.theguardian.com/environment/article/2024/jun/26/voluntary-carbon-market-offsetting-industry-reforms-cccg-climate-crisis-advisory-group-aoe
- https://www.theguardian.com/business/article/2024/jun/17/ai-profits-tax-green-levy-imf-carbon-emissions""")
