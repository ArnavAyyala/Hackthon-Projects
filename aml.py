import streamlit as st
import pandas as pd
import os
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

#from pycaret.regression import setup, compare_models, pull, save_model

with st.sidebar:
    st.image("https://matthewrenze.com/wp-content/uploads/2019/12/artificial-intelligence-the-big-picture.png")
    st.title("UrbanMindAnalytics")
    st.info("Welcome to Urban Mind Analytics - The Gateway to Data-Driven Success for Local Businesses!")
    choice = st.radio("Naviagation", ["Home","Upload", "Profiling", "ML", "Download"])
    #st.info("Welcome to Urban Mind Analytics - The Gateway to Data-Driven Success for Local Businesses!")
    #st.radio()
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col = None)

if choice == "Home":
    st.title("Urban Mind Analytics: Intelligent Profiling and Growth Solutions")
    st.image("https://www.salesforce.com/content/dam/web/en_ca/www/images/hub/business/small-business-machine-learning/why-small-businesses-need-to-pay-attention-to-what-machine-learning-is-header.jpg")
    st.title("Are you ready to take your business to the next level?")
    st.info("At Urban Mind Analytics, we empower local business owners with the tools they need to thrive in today's dynamic market. Our platform allows you to effortlessly input your business data, and in return, receive a personalized profile report that unveils hidden insights about your operations, customer behavior, and market trends. But we don't stop there. We're pioneering the fusion of data and intelligence through our cutting-edge machine learning models. With our custom-built algorithms, you'll gain access to a predictive powerhouse that forecasts trends, identifies growth opportunities, and guides you towards making informed and strategic decisions. Join us at Urban Mind Analytics and unlock the full potential of your local business. Elevate your decisions, amplify your impact, and navigate the future with confidence.")
if choice == "Upload":
    st.title("Upload Your Data for Modelling")
    file = st.file_uploader("Upload")
    if file:
        df = pd.read_csv(file, index_col = None)
        df.to_csv("sourcedata.csv", index = None)
        st.dataframe(df)
       

if choice == "Profiling":
    st.title("Exploaratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)

if choice == "ML":
    st.title("Machine Learning")
    selectionOption = ["Select Option", "CustomerID", "Destination", "Age", "VIP", "Name", "VRDeck", "Shopping Mall", "Food Court", "Inventory"]
    st.selectbox("Select Your Target", options = selectionOption)
    result = st.button("Create Model")
    if result:
        st.write("Model has been created! Navigate to the Download page to download your model for use!")

if choice == "Download":
    st.button("Download the Model")
     
  