import streamlit as st
import plotly.express as px
import pandas as pd

# Check if the DataFrame exists in session state
if 'df' not in st.session_state:
    st.error("Data not found. Please make sure to load the data on the Home page.")
else:
    df = st.session_state.df
    
    st.title("Global Trends")

    # Define a mapping from custom regions to country names
    region_to_country = {
        'Central Asia': ['Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan'],
        'Eastern Asia': ['China', 'Japan', 'South Korea', 'North Korea', 'Taiwan'],
        'Eastern Europe': ['Poland', 'Ukraine', 'Czech Republic', 'Hungary', 'Romania'],
        'Europe': ['Germany', 'France', 'United Kingdom', 'Italy', 'Spain', 'Netherlands'],
        'International': [],  # No specific countries
        'Latin America and the Caribbean': ['Brazil', 'Argentina', 'Colombia', 'Chile', 'Peru'],
        'North America': ['United States', 'Canada', 'Mexico'],
        'Northern Africa': ['Egypt', 'Libya', 'Morocco', 'Algeria', 'Tunisia'],
        'Oceania': ['Australia', 'New Zealand'],
        'South-Eastern Asia': ['Thailand', 'Vietnam', 'Malaysia', 'Indonesia', 'Philippines'],
        'Southern Asia': ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal'],
        'Sub-Saharan Africa': ['Nigeria', 'South Africa', 'Kenya', 'Ethiopia', 'Ghana'],
        'Western Asia': ['Saudi Arabia', 'Turkey', 'Iran', 'United Arab Emirates', 'Israel']
    }
    
    # Aggregate credits by region for Total Credits Issued
region_credits_issued = df.groupby('Region')['Total Credits Issued'].sum().reset_index()

# Aggregate credits by region for Total Credits Retired
region_credits_retired = df.groupby('Region')['Total Credits Retired'].sum().reset_index()

# Map the regions in the dataset to countries
def expand_region_data(region_credits, total_column):
    expanded_rows = []
    for region, countries in region_to_country.items():
        region_df = region_credits[region_credits['Region'] == region]
        for country in countries:
            if region_df.empty:
                continue
            expanded_rows.append({'Region': region, 'Country': country, total_column: region_df[total_column].sum()})

    # Handle 'International' region separately
    international_count = region_credits[region_credits['Region'] == 'International'][total_column].sum()
    expanded_rows.append({'Region': 'International', 'Country': 'Global', total_column: international_count})

    return pd.DataFrame(expanded_rows)

# Create dataframes for plotting
expanded_df_issued = expand_region_data(region_credits_issued, 'Total Credits Issued')
expanded_df_retired = expand_region_data(region_credits_retired, 'Total Credits Retired')

# Create heatmaps
fig_issued = px.choropleth(
    expanded_df_issued,
    locations='Country',
    locationmode='country names',
    color='Total Credits Issued',
    hover_name='Country',
    color_continuous_scale='Blues',
    title='Total Credits Issued by Country'
)

fig_retired = px.choropleth(
    expanded_df_retired,
    locations='Country',
    locationmode='country names',
    color='Total Credits Retired',
    hover_name='Country',
    color_continuous_scale='Blues',
    title='Total Credits Retired by Country'
)

# Display the heatmaps
st.plotly_chart(fig_issued, use_container_width=True)
st.plotly_chart(fig_retired, use_container_width=True)

    
