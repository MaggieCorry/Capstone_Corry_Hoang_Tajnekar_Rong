import streamlit as st
from PIL import Image
import os

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
st.title("More Information")

st.header("The Voluntary Registry Offset Database")
st.write("Berkeley Carbon Trading Project's Voluntary Registry Offsets Database contains all carbon offset projects listed globally by four major voluntary offset project registries: American Carbon Registry (ACR), Climate Action Reserve (CAR), Gold Standard, and Verra (VCS). These four registries generate almost all of the world's voluntary market offsets and include projects eligible for use under the California, Quebec, and Washington lcap-and-trade programs as well as UN Clean Development Mechanism projects that transitioned into one of the voluntary registries.")
st.write("Released under Creative Commons Attribution (CC BY-SA 4.0) license.  If you wish to use, adapt, or reference this material, please cite as:")
st.write("Barbara K. Haya, Aline Abayo, Ivy S. So, Micah Elias. (2024, May). Voluntary Registry Offsets Database v11, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from: https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database")
st.write("")
st.write("To download the database, sign up to receive update notices, provide suggestions, and let us know about data corrections, please visit:")
st.write("https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database")
st.write("")

st.header("Tabs")
st.subheader("Download/Database Information")
st.write("All information for Carbon AIQ is stored in the 'Download Data' tab. This lists all projects in all registries and can be filtered/sorted using drop-down menus. Each offset credit nominally represents one metric tonne of CO2-equivalent reduced or removed from the atmosphere.")
st.write("More information on calculations can be found here: https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf")

st.subheader("Charts and Graphs")
st.write("Various charts that break down projects by features can be found in the Charts and Graphs tab. The entire dashboard can be filtered by the filters at the top of the tab. If a category in a legend is clicked, it will be removed. If it is double clicked, it will be the only category shown.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")
st.subheader("Time Series")
st.write("Various graphics that show project information over time can be found in the Time Series tab. The entire dashboard can be filtered by the time slider filter at the top of the tab.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")

st.subheader("Global Trends")
st.write("Two maps are shown to show greater information of projects across regions.")
st.write("When hovered over, there will be multiple additional chart options in the top right that will appear. A useful component is the expansion option, which will bring the chart to full page mode. Furthermore, the image of the chart can be downloaded.")

st.header("Registry Data")
st.subheader("American Carbon Registry (ACR)")
st.markdown("""
- [Registry](https://acrcarbon.org/)
- [Registered Projects](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=111)
- [Credits Issued](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=112)
- [Credits Retired](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=206)
- [Credits Cancelled](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=206)
- [Buffer Pool](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=209)
- [Credit Status](https://acr2.apx.com/myModule/rpt/myrpt.asp?r=309)
- [Methodologies/Protocols](https://acrcarbon.org/methodologies/approved-methodologies/)""")

st.subheader("Climate Action Reserve (CAR)")
st.markdown("""
- [Registry](https://www.climateactionreserve.org/)
- [Registered Projects](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=111)
- [Credits Issue](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=112)
- [Credits Retired](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=206)
- [Credits Cancelled](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=308)
- [Buffer Pool](https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=706)
- [Methodologies/Protocols](https://www.climateactionreserve.org/how/protocols/)
""")

st.subheader("Gold Standard (GS)")
st.markdown("""
- [Registry](https://www.goldstandard.org/)
- [Registered Projects](https://registry.goldstandard.org/projects?q=&page=1)
- [Credits Issue & Retired](https://registry.goldstandard.org/credit-blocks?q=&page=1)
- [Methodologies/Protocols](https://globalgoals.goldstandard.org/)
""")

st.subheader("Verified Carbon Standard (VCS)")
st.markdown("""
- [Registry & Projects](https://registry.verra.org/)
- [Credits Issue & Retired](https://registry.verra.org/app/search/VCS)
- [Buffer Pool](https://registry.verra.org/app/search/VCS/All%20Projects)
- [VCS Methodologies](https://verra.org/methodologies-main/)
- [CDM Methodologies](https://cdm.unfccc.int/methodologies/index.html)""")

st.subheader("California Air Resources Board (ARB)")
st.markdown("""
- [Registry](https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program)
- [Credits Issue & Retired](https://ww2.arb.ca.gov/resources/documents/arb-offset-credit-issuance-table)
- [Protocols](https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program/compliance-offset-protocols)""")

st.subheader("Washington State Climate Commitment Act (WA)")
st.markdown("""
- [Registry](https://ecology.wa.gov/Air-Climate/Climate-Commitment-Act/Cap-and-invest/Offsets)
- [Credits Issue](https://apps.ecology.wa.gov/publications/documents/2314026.pdf)""")

st.header("Appendix")
st.write("Detailed Description of Calculations: https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf")
st.write("Change Log: https://gspp.berkeley.edu/assets/uploads/page/Change-Log--Voluntary-Registry-Offsets-Database.pdf")
st.write("Project Scopes & Type Descriptions: https://gspp.berkeley.edu/assets/uploads/page/VROD-ScopesTypes-v11.pdf")
st.write("Voluntary Registry Offsets Database webpage: https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database")
st.write("Berkeley Carbon Trading Project: https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project")
