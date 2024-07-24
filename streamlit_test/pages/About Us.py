import streamlit as st
from PIL import Image
import os

def main():
    st.title("Home")
    
    # Define the path to your local images
    image_folder = "images/team"
        
    # List of images with descriptions
    images_info = [
            {"file": "pexels-chrisleboutillier-929385.jpg", "caption": "Feature 1", "description": "Description for feature 1."},
            {"file": "pexels-loic-manegarium-3855962.jpg", "caption": "Feature 2", "description": "Description for feature 2."},
            {"file": "pexels-sarimphotos-1033729.jpg", "caption": "Feature 3", "description": "Description for feature 3."}
        ]
        
    # Display images with captions and descriptions
    for image_info in images_info:
        image_path = os.path.join(image_folder, image_info["file"])
        st.image(image_path, caption=image_info["caption"], use_column_width=True)
        st.write(image_info["description"])
