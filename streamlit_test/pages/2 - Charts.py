import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

custom_css = """
<style>
    .main .block-container {
        max-width: 95%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
</style>
"""

# Apply CSS styles
local_css("style.css")
# Check if the DataFrame exists in session state
if 'df' not in st.session_state or 'df_dates' not in st.session_state:
    st.error("Data not found. Please make sure to load the data on the Home page.")
else:
    df = st.session_state.df
    df_dates = st.session_state.df_dates
    
    st.title("Charts and Graphs")

    all_options = ["No Filter"]
    
    #st.subheader("Explore the projects based on R, ")

    col1, col2 = st.columns(2)
    with col1:
        selected_scopes = st.multiselect('Select Scopes', options=all_options + list(df['Scope'].unique()), default=all_options)
    with col2:
        selected_types = st.multiselect('Select Types', options=all_options + list(df['Type'].unique()), default=all_options)
    
    col3, col4, col5 = st.columns(3)
    with col3:
        selected_regions = st.multiselect('Select Regions', options=all_options + list(df['Region'].unique()), default=all_options)
    with col4:
        selected_countries = st.multiselect('Select Countries', options=all_options + list(df['Country'].unique()), default=all_options)
    with col5:
        selected_states = st.multiselect('Select States', options=all_options + list(df['State'].unique()), default=all_options)

    col6, col7 = st.columns(2)
    with col6:
        selected_registries = st.multiselect('Select Registries', options=all_options + list(df['Voluntary Registry'].unique()), default=all_options)
    with col7:
        selected_arbwa = st.multiselect('Select ARB vs WA', options=all_options + list(df['ARB/WA Project'].unique()), default=all_options)


    # Reset filters to "No Filter" if they are empty
    if not selected_scopes:
        selected_scopes = all_options
    if not selected_types:
        selected_types = all_options
    if not selected_regions:
        selected_regions = all_options
    if not selected_countries:
        selected_countries = all_options
    if not selected_states:
        selected_states = all_options
    if not selected_arbwa:
        selected_arbwa = all_options
    if not selected_registries:
        selected_registries = all_options
    
    # Filter the dataframe based on the selected filters
    if "No Filter" not in selected_scopes:
        df = df[df['Scope'].isin(selected_scopes)]
    
    if "No Filter" not in selected_types:
        df = df[df['Type'].isin(selected_types)]
    
    if "No Filter" not in selected_countries:
        df = df[df['Country'].isin(selected_countries)]

    if "No Filter" not in selected_regions:
        df = df[df['Region'].isin(selected_regions)]
    
    if "No Filter" not in selected_states:
        df = df[df['State'].isin(selected_states)]

    if "No Filter" not in selected_registries:
        df = df[df['Voluntary Registry'].isin(selected_registries)]

    if "No Filter" not in selected_arbwa:
        df = df[df['Registry/ARB/WA'].isin(selected_arbwa)]
    
    # Filter data based on features
    filtered_df = df.copy()
    filtered_df_dates = df_dates.copy()

    # First pie chart
    df_pie1 = filtered_df.groupby('Registry/ARB/WA').size().reset_index(name='Count')
    # First bar chart
    df_scopecred_bar = filtered_df.groupby('Scope')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
    # Second pie chart
    df_pie2 = filtered_df.groupby('Registry/ARB/WA')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
    # Second bar chart
    df_scopecred_reg = filtered_df.groupby('Region')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
    # Third bar chart
    df_bar1 = filtered_df.groupby('Scope').size().reset_index(name='Count')
    # Fourth bar chart
    df_typeScopeBar = filtered_df.groupby(['Registry/ARB/WA', 'Type'])['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
    # Fifth bar chart
    df_bar2 = filtered_df.groupby(['Scope', 'Region']).size().reset_index(name='Count')
    # Donut charts
    grouped_df_donut = filtered_df.groupby(['Scope', 'Type']).agg({'Total Credits Issued':'sum', 'Total Credits Retired':'sum'}).reset_index()
        
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
        
    ##############
    ## Row One ###
    ##############
            
    # Pie chart - Offset Projects by Standard
    fig1 = px.pie(df_pie1, values='Count', names='Registry/ARB/WA', title='Offset Projects by Standard', color='Registry/ARB/WA',
                  color_discrete_sequence=excel_colors)
            
    # Horizontal bar chart - Credits Issued by Scope
    fig2 = px.bar(df_scopecred_bar, y='Scope', x='Total Credits Issued', orientation='h', title='Credits Issued by Scope', text='Total Credits Issued',
                  color_discrete_sequence=excel_colors)
            
    ##############
    ## Row Two ###
    ##############
            
    # Pie chart - Offset Credits Issued by Standard
    fig3 = px.pie(df_pie2, values='Total Credits Issued', names='Registry/ARB/WA', title='Offset Credits Issued by Standard', color='Registry/ARB/WA',
                  color_discrete_sequence=excel_colors)
            
    # Horizontal bar chart - Credits Issued by Region
    fig4 = px.bar(df_scopecred_reg, y='Region', x='Total Credits Issued', orientation='h', title='Credits Issued by Region', text='Total Credits Issued',
                  color_discrete_sequence=excel_colors)
            
    ##############
    ## Row Three #
    ##############
            
    # Horizontal bar chart - Credits Issued by Type
    fig5 = px.bar(df_typeScopeBar, y='Type', x='Total Credits Issued', orientation='h', title='Credits Issued by Type', text='Total Credits Issued', color='Registry/ARB/WA',
                  color_discrete_sequence=excel_colors)
    fig5.update_layout(height=1200)
            
    ##############
    ## Row Four ##
    ##############
            
    # Pie chart - Projects by Scope
    fig6 = px.bar(df_bar1, y='Scope', x='Count', orientation='h', title='Projects by Scope', color='Scope', text='Count',
                  color_discrete_sequence=excel_colors)
            
    # Horizontal bar chart - Projects Distribution by Scope and Geographic Region
    fig7 = px.bar(df_bar2, y='Scope', x='Count', orientation='h', title='Projects Distribution by Scope and Geographic Region', color='Region', text='Count',
                  color_discrete_sequence=excel_colors)
            
    ##############
    ## Row Five ##
    ##############
            
    # Sunburst - Credit Issuances by Type
    fig_donut1 = px.sunburst(
        grouped_df_donut,
        path=['Scope', 'Type'],
        values='Total Credits Issued',
        title='Credit Issuances by Type',
        color_discrete_sequence=excel_colors
    )
    fig_donut1.update_traces(
        textinfo='label+percent entry',
        insidetextorientation='radial'
    )
    fig_donut1.update_layout(height=600)
            
    # Sunburst - Credits Retired by Type
    fig_donut2 = px.sunburst(
        grouped_df_donut,
        path=['Scope', 'Type'],
        values='Total Credits Retired',
        title='Credits Retired by Type',
        color_discrete_sequence=excel_colors
    )
    fig_donut2.update_traces(
        textinfo='label+percent entry',
        insidetextorientation='radial'
    )
    fig_donut2.update_layout(height=600)

    # Display the charts
    col1, col2 = st.columns([1, 2])
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("Pie chart displaying the total percentage of carbon offset projects for each registry, colored by registry.")
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Total credits issued by scope, where each bar is a different scope, and then length of the bar and corresponding number is the total credits issued for each scope.")

    col3, col4 = st.columns([1, 2])
    with col3:
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Pie chart displaying the total percentage of carbon offset credits issued for each registry, colored by standard.")  
    with col4:
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Total credits issued by region, where each bar is a different region, and then length of the bar and corresponding number is the total credits issued for each region.")

    st.plotly_chart(fig5, use_container_width=True)
    st.caption("Total credits issued by project type, where each bar aligns to a different type, and then length of the bar and corresponding number is the total credits issued for each type. The bars are colored by registry.")
    st.plotly_chart(fig6, use_container_width=True)
    st.caption("Total credits issued by scope, where each bar and its corresponding color is a different scope, and then length of the bar and corresponding number is the total number of projects aligned to each scope.")
    st.plotly_chart(fig7, use_container_width=True)
    st.caption("Total credits issued by scope, where each bar is a different scope, and then length of the bar and corresponding number is the total number of projects aligned to each scope. The bars are broken out and colored by region, where the size of the color slice indicates the number of projects for each region/scope pairing.")
    st.plotly_chart(fig_donut1, use_container_width=True)
    st.caption("The donut chart is sized by the number of credit issuances by scope and type. The inner slices are the count of credit issuances by scope, and the outer slices align to the count of issuances by project type that align under that scope.")
    st.plotly_chart(fig_donut2, use_container_width=True)
    st.caption("The donut chart is sized by the number of credits retired by scope and type. The inner slices are the count of credits retired by scope, and the outer slices align to the count of retirements by project type that align under that scope.")
