import os
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix

# Function to read CSS file and apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styles
local_css("style.css")
# Load the pre-trained model and preprocessor
model = joblib.load('../Models/models/logistic_regression_model_59types.pkl')
preprocessor = joblib.load('../Models/models/tfidf_onehotencoding_59types.pkl')

# List of text features and categorical features
categorical_features = ['region', 'voluntary_registry', 'arborwa_project']
text_features = ['project_name','fully_harmonized_methodologyorprotocol','type_from_registry', 'project_developer']

 # Streamlit app
st.title('Project Type Classification')
# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Type Classification", "Model Evaluation"])

with tab1:
    # Upload a file
    st.info("""
        Please upload a CSV file containing the following columns:
        - **project_name**: Name of the project (text)
        - **fully_harmonized_methodologyorprotocol**: Methodology or protocol (text)
        - **type_from_registry**: Type from the registry (text)
        - **project_developer**: Name of the developer (text)
        - **region**: Region of the project (categorical)
        - **voluntary_registry**: Voluntary registry (categorical)
        - **arborwa_project**: ArborWA project (categorical)
        - **type**: Project type (target variable for prediction)
        
        The file should have a header row with these exact column names. Missing columns will result in errors during processing.
    """)
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        X_test = df.drop(columns=['type'])
        Y_test = df['type']
        X_test_transformed = preprocessor.transform(X_test)
        y_pred = model.predict(X_test_transformed)
        
        # Get the predicted probabilities for each class
        y_pred_proba = model.predict_proba(X_test_transformed)
        # Create a DataFrame for predictions and confidence
        predictions = pd.DataFrame(y_pred_proba, columns=model.classes_)
        
        # Get the predicted class and the confidence for the predicted class
        df['model_prediction'] = y_pred
        df['confidence'] = predictions.max(axis=1)  # Get the max probability

        # Add column for correct/incorrect predictions
        df['result'] = df.apply(lambda row: '✔️' if row['model_prediction'] == row['type'] else '❌', axis=1)
        
        # Select relevant columns for display
        #display_df = df[['project_name', 'type', 'model_prediction', 'result']]
        st.write(df)

        # Create a download button for the predictions
        st.download_button(
            label="Download Predictions",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='project_type_predictions.csv',
            mime='text/csv',
        )

with tab2:
    # Model Evaluation
    if uploaded_file:
        st.subheader("Model Evaluation")
        # Confusion matrix
        cm = confusion_matrix(Y_test, y_pred)

        # Get unique labels in the test set and the predictions
        unique_labels = np.unique(np.concatenate([Y_test]))
        cm_filtered = confusion_matrix(Y_test, y_pred, labels=unique_labels)
        
        # Plotting the confusion matrix using a heatmap
        st.write("Confusion Matrix:")
        plt.figure(figsize=(10, 7))
        sns.heatmap(cm_filtered, annot=True, fmt='d', cmap='Blues', xticklabels=unique_labels, yticklabels=unique_labels)
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')
        st.pyplot(plt)

        # # Bar chart for label distribution
        # label_counts = df['type'].value_counts()
        
        # plt.figure(figsize=(10, 5))
        # plt.bar(label_counts.index, label_counts.values, color='#5B9BD5')  # Using one of the Excel colors
        # plt.xlabel('Project Type')
        # plt.ylabel('Count')
        # plt.title('Distribution of Project Types')
        # plt.xticks(rotation=90)
        # st.pyplot(plt)
    else:
        st.info("Please upload and classify data using the 'Type Classification' tab first.")