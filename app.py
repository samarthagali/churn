import streamlit as st
import classify
import pickle
import pandas as pd
from random import  randint
import numpy as np



if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False

# Function to handle form submission
def submit_form():
    st.session_state["form_submitted"] = True

# Conditionally display the form
if not st.session_state["form_submitted"]:
    with st.form("churn_form"):
        st.title("Churn Data Input Form")

        # Demographic Information
        st.header("Demographic Information")
        senior_citizen = st.selectbox("Senior Citizen:", options=["No", "Yes"])
        gender = st.selectbox("Gender:", options=["Male", "Female"])
        partner = st.selectbox("Partner:", options=["No", "Yes"])
        dependents = st.selectbox("Dependents:", options=["No", "Yes"])

        # Account Information
        st.header("Account Information")
        tenure = st.number_input("Tenure (months):", min_value=0, value=0, step=1)
        contract = st.selectbox("Contract:", options=["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing:", options=["No", "Yes"])
        payment_method = st.selectbox(
            "Payment Method:", 
            options=["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"]
        )

        # Service Information
        st.header("Service Information")
        phone_service = st.selectbox("Phone Service:", options=["No", "Yes"])
        multiple_lines = st.selectbox("Multiple Lines:", options=["No", "Yes", "No phone service"])
        internet_service = st.selectbox("Internet Service:", options=["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security:", options=["No", "Yes", "No internet service"])
        online_backup = st.selectbox("Online Backup:", options=["No", "Yes", "No internet service"])
        device_protection = st.selectbox("Device Protection:", options=["No", "Yes", "No internet service"])
        tech_support = st.selectbox("Tech Support:", options=["No", "Yes", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV:", options=["No", "Yes", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies:", options=["No", "Yes", "No internet service"])

        # Financial Information
        st.header("Financial Information")
        monthly_charges = st.number_input("Monthly Charges:", min_value=0.0, value=0.0, step=0.01)
        total_charges = st.number_input("Total Charges:", min_value=0.0, value=0.0, step=0.01)

        # Submit Button
        submit_button = st.form_submit_button(label="Submit", on_click=submit_form)

else:
    # Once form is submitted, display a success message and processed data
    st.success("Form submitted successfully!")
    
    # Access form data after submission
    senior_citizen = st.session_state.get('senior_citizen', "No")
    gender = st.session_state.get('gender', "Male")
    partner = st.session_state.get('partner', "No")
    dependents = st.session_state.get('dependents', "No")
    tenure = st.session_state.get('tenure', 0)
    contract = st.session_state.get('contract', "Month-to-month")
    paperless_billing = st.session_state.get('paperless_billing', "No")
    payment_method = st.session_state.get('payment_method', "Bank transfer (automatic)")
    phone_service = st.session_state.get('phone_service', "No")
    multiple_lines = st.session_state.get('multiple_lines', "No phone service")
    internet_service = st.session_state.get('internet_service', "DSL")
    online_security = st.session_state.get('online_security', "No")
    online_backup = st.session_state.get('online_backup', "No")
    device_protection = st.session_state.get('device_protection', "No")
    tech_support = st.session_state.get('tech_support', "No")
    streaming_tv = st.session_state.get('streaming_tv', "No")
    streaming_movies = st.session_state.get('streaming_movies', "No")
    monthly_charges = st.session_state.get('monthly_charges', 0.0)
    total_charges = st.session_state.get('total_charges', 0.0)

    # Process and display the data
    processed_data = {
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": 1 if gender == "Male" else 0,
        "Partner_Yes": 1 if partner == "Yes" else 0,
        "Dependents_Yes": 1 if dependents == "Yes" else 0,
        "PhoneService_Yes": 1 if phone_service == "Yes" else 0,
        "MultipleLines_No phone service": 1 if multiple_lines == "No phone service" else 0,
        "MultipleLines_Yes": 1 if multiple_lines == "Yes" else 0,
        "InternetService_Fiber optic": 1 if internet_service == "Fiber optic" else 0,
        "InternetService_No": 1 if internet_service == "No" else 0,
        "OnlineSecurity_No internet service": 1 if online_security == "No internet service" else 0,
        "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,
        "OnlineBackup_No internet service": 1 if online_backup == "No internet service" else 0,
        "OnlineBackup_Yes": 1 if online_backup == "Yes" else 0,
        "DeviceProtection_No internet service": 1 if device_protection == "No internet service" else 0,
        "DeviceProtection_Yes": 1 if device_protection == "Yes" else 0,
        "TechSupport_No internet service": 1 if tech_support == "No internet service" else 0,
        "TechSupport_Yes": 1 if tech_support == "Yes" else 0,
        "StreamingTV_No internet service": 1 if streaming_tv == "No internet service" else 0,
        "StreamingTV_Yes": 1 if streaming_tv == "Yes" else 0,
        "StreamingMovies_No internet service": 1 if streaming_movies == "No internet service" else 0,
        "StreamingMovies_Yes": 1 if streaming_movies == "Yes" else 0,
        "Contract_One year": 1 if contract == "One year" else 0,
        "Contract_Two year": 1 if contract == "Two year" else 0,
        "PaperlessBilling_Yes": 1 if paperless_billing == "Yes" else 0,
        "PaymentMethod_Credit card (automatic)": 1 if payment_method == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic check": 1 if payment_method == "Electronic check" else 0,
        "PaymentMethod_Mailed check": 1 if payment_method == "Mailed check" else 0,
    }
    df=pd.DataFrame(processed_data,index=[0])
    with open("rfc.pkl", "rb") as f:
        model = pickle.load(f)
    val=classify.predict(model,df)
    if val==True:
        st.write("Dear Customer, please contact us at churning_set@gmail.com if you need any help or information or would like to lodge a complaint")
    else:
        st.write("Dear Customer, we are so grateful for your help ") 
