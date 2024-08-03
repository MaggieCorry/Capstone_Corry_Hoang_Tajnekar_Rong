import streamlit as st
import plotly.express as px
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
# Check if the DataFrame exists in session state
if 'df' not in st.session_state:
    st.error("Data not found. Please make sure to load the data on the Home page.")
else:
    df = st.session_state.df
    
    st.title("Carbon Offset Around the World")
    
    # Aggregate credits by region
    region_credits = df.groupby('Country').agg({
        'Total Credits Issued': 'sum',
        'Total Credits Retired': 'sum'
    }).reset_index()
    
    # Calculate the count of projects by country
    project_count = df['Country'].value_counts().reset_index()
    project_count.columns = ['Country', 'Project Count']
    
    # Merge the project count with the region credits data
    region_credits = pd.merge(region_credits, project_count, on='Country')
    # Initialize the selection state
    if 'credit_type' not in st.session_state:
        st.session_state.credit_type = 'Total Credits Issued'
    
     # Create three columns for layout, using the middle one for buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        button_issued = st.button('Total Credits Issued')
    with col2:
        button_retired = st.button('Total Credits Retired')
    with col3:
        button_count = st.button('Project Count')
        
    if button_issued:
        st.session_state.credit_type = 'Total Credits Issued'
    elif button_retired:
        st.session_state.credit_type = 'Total Credits Retired'
    elif button_count:
        st.session_state.credit_type = 'Project Count'
    
    option = st.session_state.credit_type
    
    # Create heatmap based on selection
    fig = px.choropleth(
        region_credits,
        locations='Country',
        locationmode='country names',
        color=option,
        hover_name='Country',
        color_continuous_scale='Blues',
        title=f'{option} by Country'
    )
    fig.update_geos(projection_type="natural earth")
    fig.update_geos(
        showcoastlines=False,
        showland=True,
        showcountries=False,
        showocean=False,
        landcolor="white",
        oceancolor="white"
    )
    fig.update_layout(margin={"r":0,"t":21,"l":0,"b":0})  # Remove the border and padding

    # Display the heatmap
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)  # Use full container width
    st.markdown('</div>', unsafe_allow_html=True)
    st.caption(f"{option} by country, where the darker the country, the more {option}.")
