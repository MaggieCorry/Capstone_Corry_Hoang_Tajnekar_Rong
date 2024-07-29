import streamlit as st

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
if 'df' not in st.session_state:
    st.error("Data not found. Please make sure to load the data on the Home page.")
else:
    df = st.session_state.df   
    st.title("Download Data")
    st.write("Full Data:")
    st.write(df)
        
    st.download_button(label='Download CSV', data=df.to_csv(index=False), file_name='data.csv', mime='text/csv')
