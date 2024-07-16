# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set the initial page configuration
st.set_page_config(
    page_title="Carbon AIQ",
    layout="wide",  # Use wide layout to expand the width of the dashboard
    initial_sidebar_state="expanded",
)
st.title('Carbon AIQ')

# Sample DataFrame
df = pd.read_csv("../EDA/streamlit_data.csv")
# FROM TABLE_X 
df_dates = pd.read_csv("../EDA/capstone_withDates.csv")

# Define options for filters, including "No Filter" option
all_options = ["No Filter"]

# Multi-selection filters with "No Filter" option
selected_regions = st.sidebar.multiselect('Select Regions', options=all_options + list(df['Region'].unique()), default=all_options)
selected_scopes = st.sidebar.multiselect('Select Scopes', options=all_options + list(df['Scope'].unique()), default=all_options)
selected_types = st.sidebar.multiselect('Select Types', options=all_options + list(df[' Type'].unique()), default=all_options)
selected_registries = st.sidebar.multiselect('Select Registries', options=all_options + list(df['Voluntary Registry'].unique()), default=all_options)

# Filter the dataframe based on the selected filters
if "No Filter" not in selected_regions:
    df = df[df['Region'].isin(selected_regions)]

if "No Filter" not in selected_scopes:
    df = df[df['Scope'].isin(selected_scopes)]

if "No Filter" not in selected_types:
    df = df[df[' Type'].isin(selected_types)]

if "No Filter" not in selected_registries:
    df = df[df['Voluntary Registry'].isin(selected_registries)]

# Filter data based on features
filtered_df = df.copy()
filtered_df_dates = df_dates.copy()

#grouped
# First pie chart
df_pie1 = filtered_df.groupby('Registry / ARB / WA').size().reset_index(name='Count')
#First bar chart
df_scopecred_bar = filtered_df.groupby('Scope')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
# Second pie chart
df_pie2 = filtered_df.groupby('Registry / ARB / WA')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
#Second bar char
df_scopecred_reg = filtered_df.groupby('Region')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
#Third bar chart
df_bar1 = filtered_df.groupby('Scope').size().reset_index(name='Count')
#Fourth bar chart
df_typeScopeBar = filtered_df.groupby(['Registry / ARB / WA', ' Type'])['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
#Fifth bar
df_bar2 = filtered_df.groupby(['Scope', 'Region']).size().reset_index(name='Count')
#Donut charts
grouped_df_donut = filtered_df.groupby(['Scope', ' Type']).agg({'Total Credits Issued':'sum', 'Total Credits Retired':'sum'}).reset_index()

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

#Pie chart - Offset Projects by Standard
fig1 = px.pie(df_pie1, values='Count', names='Registry / ARB / WA', title='Offset Projects by Standard', color='Registry / ARB / WA',
    color_discrete_sequence=excel_colors)

#Horizontal bar chart - Credits Issued by Scope
fig2 = px.bar(df_scopecred_bar, y='Scope', x='Total Credits Issued', orientation='h', title='Credits Issued by Scope', text='Total Credits Issued',
    color_discrete_sequence=excel_colors)

##############
## Row Two ###
##############

#Pie chart - Offset Credits Issued by Standard
fig3 = px.pie(df_pie2, values='Total Credits Issued', names='Registry / ARB / WA', title='Offset Credits Issued by Standard', color='Registry / ARB / WA',
    color_discrete_sequence=excel_colors)

#Horizontal bar chart - Credits Issued by Region
fig4 = px.bar(df_scopecred_reg, y='Region', x='Total Credits Issued', orientation='h', title='Credits Issued by Region', text='Total Credits Issued',
    color_discrete_sequence=excel_colors)

##############
## Row Three #
##############

#Horizontal bar chart - Credits Issued by Type
fig5 = px.bar(df_typeScopeBar, y=' Type', x='Total Credits Issued', orientation='h', title='Credits Issued by Type', text='Total Credits Issued', color='Registry / ARB / WA',
    color_discrete_sequence=excel_colors)
fig5.update_layout(height=1200)

##############
## Row Four ##
##############

#Pie chart - Projects by Scope'
fig6 = px.bar(df_bar1, y='Scope', x='Count', orientation='h', title='Projects by Scope', color='Scope', text='Count',
    color_discrete_sequence=excel_colors)

#Horizontal bar chart - Projects Distribution by Scope and Geographic Region
fig7 = px.bar(df_bar2, y='Scope', x='Count', orientation='h', title='Projects Distribution by Scope and Geographic Region', color='Region', text='Count',
    color_discrete_sequence=excel_colors)


##############
## Row Five ##
##############

#Sunburst - Credit Issuances by Type
fig_donut1 = px.sunburst(
    grouped_df_donut,
    path=['Scope', ' Type'],
    values='Total Credits Issued',
    title='Credit Issuances by Type',
    color_discrete_sequence=excel_colors
)
fig_donut1.update_traces(
    textinfo='label+percent entry',
    insidetextorientation='radial'
)
fig_donut1.update_layout(height=600)

#Sunburst - Credits Retired by Type
fig_donut2 = px.sunburst(
    grouped_df_donut,
    path=['Scope', ' Type'],
    values='Total Credits Retired',
    title='Credits Retired by Type',
    color_discrete_sequence=excel_colors
)
fig_donut2.update_traces(
    textinfo='label+percent entry',
    insidetextorientation='radial'
)
fig_donut2.update_layout(height=600)

###############
## Over Times##
###############

# Dual Line Chart
fig_lines = go.Figure()
grouped_df_lines = filtered_df_dates.groupby('Year').sum().reset_index()
#Issuances line
fig_lines.add_trace(go.Scatter(
    x=grouped_df_lines['Year'], 
    y=grouped_df_lines['Credits issued by issuance year'], 
    mode='lines+markers', 
    name='Issuances'
))
#Retirements line
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
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

#Prepare data for area charts
grouped_df_arealines = filtered_df_dates.groupby(['Year','Reduction / Removal']).sum().reset_index()
total_per_year = filtered_df_dates.groupby('Year').agg({'Credits issued by issuance year':'sum','Credits retired or cancelled':'sum'}).reset_index()
total_per_year.columns = ['Year', 'Total Issuances', 'Total Retirements']
grouped_df_arealines = pd.merge(grouped_df_arealines, total_per_year, on='Year')
grouped_df_arealines['Issue_perc'] = round((grouped_df_arealines['Credits issued by issuance year']/grouped_df_arealines['Total Issuances'])*100, 0)
grouped_df_arealines['Retire_perc'] = round((grouped_df_arealines['Credits retired or cancelled']/grouped_df_arealines['Total Retirements'])*100, 0)

#Area line - Issuances by Reduction / Removal Over Time
area_fig1 = px.area(
    grouped_df_arealines,
    x='Year',
    y='Credits issued by issuance year',
    text='Issue_perc',
    color='Reduction / Removal',
    title='Issuances by Reduction / Removal Over Time',
    color_discrete_sequence=excel_colors
)

#Area line - Retirements by Reduction / Removal Over Time
area_fig2 = px.area(
    grouped_df_arealines,
    x='Year',
    y='Credits retired or cancelled',
    text='Retire_perc',
    color='Reduction / Removal',
    title='Retirements by Reduction / Removal Over Time',
    color_discrete_sequence=excel_colors
)

#3D Area line
grouped_df_3D = filtered_df_dates.groupby(['Year','Scope'])['Credits retired or cancelled'].sum().reset_index()
fig_3D = go.Figure()
#create each z axis group
scopes = grouped_df_3D['Scope'].unique()
colors = {scope: color for scope, color in zip(scopes, excel_colors)}
for scope in scopes:
    df_scope = grouped_df_3D[grouped_df_3D['Scope'] == scope]
    fig_3D.add_trace(go.Scatter3d(
        x=df_scope['Year'],
        z=df_scope['Credits retired or cancelled'],
        y=[scope]*len(df_scope),  # Z-axis is categorical, so we use the same value for each point
        mode='lines+markers',
        line=dict(color=colors[scope]),
        marker=dict(size=5),
        name=scope
    ))
fig_3D.update_layout(
    title='3D Area Line Graph',
    scene=dict(
        xaxis_title='Year',
        zaxis_title='Credits Retired',
        yaxis_title='Scope',
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        zaxis=dict(showgrid=True)
    )
)

##########
## TABS ##
##########

#Create tabs
tab1, tab2, tab3 = st.tabs(["Charts and Graphs", "Time-Series Graphics", "Download Data"])

#Charts and graphs
with tab1:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.plotly_chart(fig4, use_container_width=True)

    st.plotly_chart(fig5, use_container_width=True)
    st.plotly_chart(fig6, use_container_width=True)
    st.plotly_chart(fig7, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig_donut1, use_container_width=True)
    with col4:
        st.plotly_chart(fig_donut2, use_container_width=True)
#Time series
with tab2:
    st.plotly_chart(fig_lines, use_container_width=True)
    st.plotly_chart(area_fig1, use_container_width=True)
    st.plotly_chart(area_fig2, use_container_width=True)
    st.plotly_chart(fig_3D, use_container_width=True)
#Data tab
with tab3:
    st.title('VROD vX Data')
    st.write('Full Data:')
    st.write(df)
    # Add a download button
    st.download_button(label='Download CSV', data=df, file_name='data.csv', mime='text/csv')