import streamlit as st

def main():
    df = st.session_state.df
    
    st.title("Download Data")
    st.write("Full Data:")
    st.write(df)
    
    st.download_button(label='Download CSV', data=df.to_csv(index=False), file_name='data.csv', mime='text/csv')
