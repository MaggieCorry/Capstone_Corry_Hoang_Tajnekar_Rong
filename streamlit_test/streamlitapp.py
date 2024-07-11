# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title('Carbon AIQ')

# Sample DataFrame
df = pd.read_csv("../EDA/clustered_out.csv")
df_dates = pd.read_csv("../EDA/capstone_withDates.csv")

# Sidebar filters
selected_registry = st.sidebar.selectbox('Select Registry', ['No Filter'] + list(df['Voluntary Registry'].unique()))
selected_scope = st.sidebar.selectbox('Select Scope', ['No Filter'] + list(df['Scope'].unique()))
selected_type = st.sidebar.selectbox('Select Type', ['No Filter'] + list(df[' Type'].unique()))
selected_region = st.sidebar.selectbox('Select Region', ['No Filter'] + list(df['Region'].unique()))

# Filter data based on features
filtered_df = df.copy()
filtered_df_dates = df_dates.copy()
if selected_registry != 'No Filter':
    filtered_df = filtered_df[filtered_df['Voluntary Registry'] == selected_registry]
    filtered_df_dates = filtered_df_dates[filtered_df_dates['Voluntary Registry'] == selected_registry]
if selected_scope != 'No Filter':
    filtered_df = filtered_df[filtered_df['Scope'] == selected_scope]
    filtered_df_dates = filtered_df_dates[filtered_df_dates['Scope'] == selected_scope]
if selected_type != 'No Filter':
    filtered_df = filtered_df[filtered_df[' Type'] == selected_scope]
    filtered_df_dates = filtered_df_dates[filtered_df_dates[' Type'] == selected_scope]
if selected_region != 'No Filter':
    filtered_df = filtered_df[filtered_df['Region'] == selected_scope]
    filtered_df_dates = filtered_df_dates[filtered_df_dates['Region'] == selected_scope]


##############
## Row One ###
##############

# First Pie Chart
df_pie1 = filtered_df.groupby('Registry / ARB / WA').size().reset_index(name='Count')
# Create the pie chart
fig1 = px.pie(df_pie1, values='Count', names='Registry / ARB / WA', title='Offset Projects by Standard', color='Registry / ARB / WA')

# Create the horizontal bar chart
df_scopecred_bar = filtered_df.groupby('Scope')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
fig2 = px.bar(df_scopecred_bar, y='Scope', x='Total Credits Issued', orientation='h', title='Credits Issued by Scope', text='Total Credits Issued')


##############
## Row Two ###
##############

# Second Pie Chart
df_pie2 = filtered_df.groupby('Registry / ARB / WA')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
# Create the pie chart
fig3 = px.pie(df_pie2, values='Total Credits Issued', names='Registry / ARB / WA', title='Offset Credits Issued by Standard', color='Registry / ARB / WA')

# Create the horizontal bar chart
df_scopecred_reg = filtered_df.groupby('Region')['Total Credits Issued'].sum().reset_index(name='Total Credits Issued')
fig4 = px.bar(df_scopecred_reg, y='Region', x='Total Credits Issued', orientation='h', title='Credits Issued by Region', text='Total Credits Issued')

##############
## Row Three #
##############

# Create the horizontal bar chart
fig5 = px.bar(filtered_df, y=' Type', x='Total Credits Issued', orientation='h', title='Credits Issued by Type', text='Total Credits Issued', color='Registry / ARB / WA')
fig5.update_layout(height=1000)

##############
## Row Four ##
##############

# Additional bar
df_bar1 = filtered_df.groupby('Scope').size().reset_index(name='Count')
# Create the pie chart
fig6 = px.bar(df_bar1, y='Scope', x='Count', orientation='h', title='Projects by Scope', color='Scope', text='Count')


#Line Chart
# Create the line chart
fig_lines = go.Figure()
grouped_df_lines = filtered_df_dates.groupby('Year').sum().reset_index()
# Add Issuances line
fig_lines.add_trace(go.Scatter(
    x=grouped_df_lines['Year'], 
    y=grouped_df_lines['Credits issued by issuance year'], 
    mode='lines+markers', 
    name='Issuances'
))

# Add Retirements line
fig_lines.add_trace(go.Scatter(
    x=grouped_df_lines['Year'], 
    y=grouped_df_lines['Credits retired or cancelled'], 
    mode='lines+markers', 
    name='Retirements'
))

# Customize the layout
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


# Additional bar
df_bar2 = filtered_df.groupby(['Scope', 'Region']).size().reset_index(name='Count')
# Create the bar chart
fig7 = px.bar(df_bar2, y='Scope', x='Count', orientation='h', title='Projects Distribution by Scope and Geographic Region', color='Region', text='Count')


##############
## Row Five ##
##############

# Group by Scope and Type to get the count
grouped_df_donut = filtered_df.groupby(['Scope', ' Type'])['Total Credits Issued'].sum().reset_index()

# Create the sunburst chart
fig_donut1 = px.sunburst(
    grouped_df_donut,
    path=['Scope', ' Type'],
    values='Total Credits Issued',
    title='Credit Issuances by Type',
)

fig_donut1.update_traces(
    textinfo='label+percent entry',  # Show label and percentage in the labels
    insidetextorientation='radial'   # Make the text orientation radial
)

fig_donut1.update_layout(height=600)



# Create tabs
tab1, tab2 = st.tabs(["Charts and Graphs", "Download Data"])

with tab1:
    #set up display
    col1, col2 = st.columns([1, 2])

    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    #set up display
    col1, col2 = st.columns([1, 2])
    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.plotly_chart(fig4, use_container_width=True)

    st.plotly_chart(fig5, use_container_width=True)
    st.plotly_chart(fig6, use_container_width=True)
    st.plotly_chart(fig_lines, use_container_width=True)
    st.plotly_chart(fig7, use_container_width=True)
    st.plotly_chart(fig_donut1, use_container_width=True)

with tab2:
    st.title('VROD vXXX Data')
    # Display the DataFrame
    st.write('Full Data:')
    st.write(df)
    # Add a download button
    st.download_button(label='Download CSV', data=df, file_name='data.csv', mime='text/csv')