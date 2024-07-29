import streamlit as st
from PIL import Image
import os

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
#st.title("About Us")

# Define the path to your local images
image_folder = "images/team"
    
# List of images with descriptions
# images_info = [
#         {"file": "pexels-chrisleboutillier-929385.jpg", "caption": "Feature 1", "description": "Description for feature 1."},
#         {"file": "pexels-loic-manegarium-3855962.jpg", "caption": "Feature 2", "description": "Description for feature 2."},
#         {"file": "pexels-sarimphotos-1033729.jpg", "caption": "Feature 3", "description": "Description for feature 3."}
#     ]
    
# # Display images with captions and descriptions
# for image_info in images_info:
#     image_path = os.path.join(image_folder, image_info["file"])
#     st.image(image_path, caption=image_info["caption"], use_column_width=True)
#     st.write(image_info["description"])
st.title("Who we are")

st.header("Our Data Product")
st.write("Carbon AIQ Database contains all carbon offset projects listed globally by four major voluntary offset project registries: American Carbon Registry (ACR), Climate Action Reserve (CAR), Gold Standard, and Verra (VCS). These four registries generate almost all of the world's voluntary market offsets and include projects eligible for use under the California, Quebec, and Washington lcap-and-trade programs as well as UN Clean Development Mechanism projects that transitioned into one of the voluntary registries.")

st.header("Our Data Sources")

st.write("American Carbon Registry (ACR)")

# Display bullet points using Markdown
st.markdown("""
- [Registry](https://acrcarbon.org/)
- [Registered Projects](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=111)
- [Credits Issued](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=112)
- [Credits Retired](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=206)
- [Credits Cancelled](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=206)
- [Buffer Pool](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=209)
- [Credit Status](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=309)
- [Methodologies/Protocols](https://acrcarbon.org/methodologies/approved-methodologies/)
""")

st.write("Climate Action Reserve (CAR)")
st.markdown("""
- [Registry](https://www.climateactionreserve.org/)")
- [Registered Projects](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=111)")
- [Credits Issue](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=112)")
- [Credits Retired](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=206)")
- [Credits Cancelled](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=308)")
- [Buffer Pool](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=706)")
- [Methodologies/Protocols](https://www.climateactionreserve.org/how/protocols/)
""")

st.write("Gold Standard (GS)")
st.markdown("""
- [Registry](https://www.goldstandard.org/)")
- [Registered Projects](https://registry.goldstandard.org/projects?q=&page=1)")
- [Credits Issue & Retired](https://registry.goldstandard.org/credit-blocks?q=&page=1)")
- [Methodologies/Protocols](https://globalgoals.goldstandard.org/)
""")

st.write("Verified Carbon Standard (VCS)")
st.markdown("""
- [Registry & Projects](https://registry.verra.org/)")
- [Credits Issue & Retired](https://registry.verra.org/app/search/VCS)")
- [Buffer Pool](https://registry.verra.org/app/search/VCS/All%20Projects)")
- [VCS Methodologies](https://verra.org/methodologies-main/)")
- [CDM Methodologies](https://cdm.unfccc.int/methodologies/index.html)
""")

st.write("California Air Resources Board (ARB)")
st.markdown("""
- [Registry](https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program)")
- [Credits Issue & Retired](https://ww2.arb.ca.gov/resources/documents/arb-offset-credit-issuance-table)")
- [Protocols](https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program/compliance-offset-protocols)
""")

st.write("Washington State Climate Commitment Act (WA)")
st.markdown("""
- [Registry](https://ecology.wa.gov/Air-Climate/Climate-Commitment-Act/Cap-and-invest/Offsets)")
- [Credits Issue](https://apps.ecology.wa.gov/publications/documents/2314026.pdf)
""")
st.header("Our Website")
st.subheader("Project Type Classification")
st.write("The 'Project Type Classification' page is used to evaluate test data for project classification. Users need to upload a CSV file containing specific columns such as project name, methodology, registry type, developer name, region, and more. After uploading, users can download the classification results and view the model's performance in the 'Model Evaluation' tab.")


st.subheader("Data Database")
st.write("All information for Carbon AIQ is stored in the 'Data Download' tab. This lists all projects in all registries and can be filtered/sorted using drop-down menus. Each offset credit nominally represents one metric tonne of CO2-equivalent reduced or removed from the atmosphere.")

st.subheader("Charts and Graphs")
st.write("Various charts that break down projects by features can be found in the Charts and Graphs tab. The entire dashboard can be filtered by the filters at the top of the tab. If a category in a legend is clicked, it will be removed. If it is double clicked, it will be the only category shown.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")

st.subheader("Time Series")
st.write("Various graphics that show project information over time can be found in the Time Series tab. The entire dashboard can be filtered by the time slider filter at the top of the tab.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")

st.subheader("Geospacial Maps")
st.write("Two maps are shown to show greater information of projects across regions.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")


st.header("Appendix")
st.write("Detailed Description of Calculations: https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf")
st.write("Change Log: https://gspp.berkeley.edu/assets/uploads/page/Change-Log--Voluntary-Registry-Offsets-Database.pdf")
st.write("Project Scopes & Type Descriptions: https://gspp.berkeley.edu/assets/uploads/page/VROD-ScopesTypes-v11.pdf")
st.write("Voluntary Registry Offsets Database webpage: https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database")
st.write("Berkeley Carbon Trading Project: https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project")
