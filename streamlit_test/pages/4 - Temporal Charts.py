import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
# Check if the DataFrame exists in session state
if 'df' not in st.session_state or 'df_dates' not in st.session_state:
    st.error("Data not found. Please make sure to load the data on the Home page.")
else:
    df = st.session_state.df
    df_dates = st.session_state.df_dates
    
    st.title("Time Series Collection")

    # Define filters
    all_options = ["No Filter"]

    # Subsection before the slider
    #st.subheader("Select Date Range")

    # # Add custom CSS to change slider color to gray
    # st.markdown("""
    # <style>
    # .stSlider > div {
    #     background-color: white !important;
    # }
    # </style>
    # """, unsafe_allow_html=True)

    # Define year range
    min_year = int(df_dates['Year'].min())
    max_year = int(df_dates['Year'].max())

    # Date range slider
    selected_years = st.slider(
        'Select Year Range',
        min_value=min_year, 
        max_value=max_year, 
        value=(min_year, max_year)
    )
        # selected_reductions = st.multiselect('Select Reduction / Removal', options=all_options + list(df_dates['Reduction / Removal'].unique()), default=all_options)

    # Filter the dataframe based on the selected filters
    filtered_df_dates = df_dates.copy()

    # Apply time slider filter
    filtered_df_dates = filtered_df_dates[
        (filtered_df_dates['Year'] >= selected_years[0]) &
        (filtered_df_dates['Year'] <= selected_years[1])
    ]

    # if "No Filter" not in selected_reductions:
    #     filtered_df_dates = filtered_df_dates[filtered_df_dates['Reduction / Removal'].isin(selected_reductions)]

    ###############
    ## Aesthetics##
    ###############
    
    # Excel color palette
    excel_colors = [
        '#5B9BD5',  # Blue
        '#ED7D31',  # Orange
        '#A5A5A5',  # Gray
        '#FFC000',  # Gold
        '#4472C4',  # Dark Blue
        '#70AD47',  # Green
        '#255E91',  # Darker Blue
        '#9E480E',  # Darker Orange
        '#636363',  # Darker Gray
        '#BF8F00',  # Darker Gold
        '#264478',  # Even Darker Blue
        '#43682B',  # Even Darker Green
        '#BFBFBF',  # Lighter Gray
        '#92D050',  # Light Green
        '#00B0F0',  # Light Blue
        '#7030A0',  # Purple
        '#C65911',  # Rust
        '#F4B084',  # Peach
        '#FFD966',  # Light Yellow
        '#548235'   # Olive Green
    ]

    ###############
    ## Over Times##
    ###############
    
    # Dual Line Chart
    @st.cache_data
    def get_grouped_data(filtered_df_dates):
        return filtered_df_dates.groupby('Year').sum().reset_index()
    
    grouped_df_lines = get_grouped_data(filtered_df_dates)

    fig_lines = go.Figure()
    
    # Issuances line
    fig_lines.add_trace(go.Scatter(
        x=grouped_df_lines['Year'], 
        y=grouped_df_lines['Credits issued by issuance year'], 
        mode='lines+markers', 
        name='Issuances'
    ))
    
    # Retirements line
    fig_lines.add_trace(go.Scatter(
        x=grouped_df_lines['Year'], 
        y=grouped_df_lines['Credits retired or cancelled'], 
        mode='lines+markers', 
        name='Retirements'
    ))
    
    fig_lines.update_layout(
        title='Credits Issued and Retired Over Time',
        xaxis_title='Year',
        yaxis_title='Credits (in Millions)',
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02
        )
    )
    
    # Prepare data for area charts
    @st.cache_data
    def prepare_area_data(filtered_df_dates):
        grouped_df_arealines = filtered_df_dates.groupby(['Year','Reduction / Removal']).sum().reset_index()
        total_per_year = filtered_df_dates.groupby('Year').agg({'Credits issued by issuance year':'sum','Credits retired or cancelled':'sum'}).reset_index()
        total_per_year.columns = ['Year', 'Total Issuances', 'Total Retirements']
        grouped_df_arealines = pd.merge(grouped_df_arealines, total_per_year, on='Year')
        grouped_df_arealines['Issue_perc'] = round((grouped_df_arealines['Credits issued by issuance year']/grouped_df_arealines['Total Issuances'])*100, 0)
        grouped_df_arealines['Retire_perc'] = round((grouped_df_arealines['Credits retired or cancelled']/grouped_df_arealines['Total Retirements'])*100, 0)
        return grouped_df_arealines
    
    grouped_df_arealines = prepare_area_data(filtered_df_dates)
    
    # Area line - Issuances by Reduction / Removal Over Time
    area_fig1 = px.area(
        grouped_df_arealines,
        x='Year',
        y='Credits issued by issuance year',
        text='Issue_perc',
        color='Reduction / Removal',
        title='Issuances by Reduction / Removal Over Time',
        color_discrete_sequence=excel_colors
    )
    
    # Area line - Retirements by Reduction / Removal Over Time
    area_fig2 = px.area(
        grouped_df_arealines,
        x='Year',
        y='Credits retired or cancelled',
        text='Retire_perc',
        color='Reduction / Removal',
        title='Retirements by Reduction / Removal Over Time',
        color_discrete_sequence=excel_colors
    )

    # Display charts
    st.plotly_chart(fig_lines, use_container_width=True)
    st.caption("Line chart showing total credits issued and credits retired for each year")
    st.plotly_chart(area_fig1, use_container_width=True)
    st.caption("Total credits issued for each year, colored by a reduction or removal type")
    st.plotly_chart(area_fig2, use_container_width=True)
    st.caption("Total credits retired for each year, colored by a reduction or removal type")
