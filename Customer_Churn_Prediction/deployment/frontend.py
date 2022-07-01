import streamlit as st
import requests

st.title('Prediction of Telecommunication Customer Churn')

st.subheader('tenure')
tenure = st.number_input('How long has the customer used the service?')

st.subheader('MonthlyCharges')
MonthlyCharges = st.number_input('How much do you charge monthly?')

st.subheader('TotalCharges')
TotalCharges = st.number_input('How much is the total charges for the customer?')

st.subheader('gender')
gender = st.selectbox('What is the customers sex?', ['Female', 'Male'])

st.subheader('SeniorCitizen')
SeniorCitizen = st.selectbox('Is the customer a Senior Citizen?', ['No', 'Yes'])

st.subheader('Partner')
Partner = st.selectbox('Does the customer have a Partner?', ['No', 'Yes'])

st.subheader('Dependents')
Dependents = st.selectbox('Is the customer on Dependents?', ['No', 'Yes'])

st.subheader('MultipleLines')
MultipleLines = st.selectbox('Does the customer have Multiple Lines?', ['No', 'Yes'])

st.subheader('InternetService')
InternetService = st.selectbox('Does the customer have Internet Service, if so what type?', ['DSL',
                             'Fiber optic', 'No'])

st.subheader('OnlineSecurity')
OnlineSecurity = st.selectbox('Does the customer have Online Security?', ['No', 'Yes'])

st.subheader('OnlineBackup')
OnlineBackup = st.selectbox('Does the customer have Online Backup?', ['No', 'Yes'])

st.subheader('DeviceProtection')
DeviceProtection = st.selectbox('Does the customer have Device Protection?', ['No', 'Yes'])

st.subheader('TechSupport')
TechSupport = st.selectbox('Does the customer have/use Tech Support?', ['No', 'Yes'])

st.subheader('StreamingTV')
StreamingTV = st.selectbox('Does the customer do some TV Streaming?', ['No', 'Yes'])

st.subheader('StreamingMovies')
StreamingMovies = st.selectbox('Does the customer Stream Movies?', ['No', 'Yes'])

st.subheader('Contract')
Contract = st.selectbox('How long is the customers Contract?', ['Month-to-month', 'One year', 'Two year'])

st.subheader('PaperlessBilling')
PaperlessBilling = st.selectbox('Does the customer use Paperless Billing?', ['No', 'Yes'])

st.subheader('PaymentMethod')
PaymentMethod = st.selectbox('What type of Payment Method do they use?',['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

data = {'tenure':tenure,
        'MonthlyCharges':MonthlyCharges,
        'TotalCharges': TotalCharges,
        'gender':gender,
        'SeniorCitizen':SeniorCitizen,
        'Partner':Partner,
        'Dependents':Dependents,
        'MultipleLines':MultipleLines,
        'InternetService':InternetService,
        'OnlineSecurity':OnlineSecurity,
        'OnlineBackup':OnlineBackup,
        'DeviceProtection':DeviceProtection,
        'TechSupport':TechSupport,
        'StreamingTV':StreamingTV,
        'StreamingMovies':StreamingMovies,
        'Contract':Contract,
        'PaperlessBilling':PaperlessBilling,
        'PaymentMethod':PaymentMethod}

URL = 'http://127.0.0.1:5000/predict' #Works on local 
#URL = 'actual-link' Since the backend was too large with a size of 660,6M (max being 500M) I am unable to push to heroku

r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['class_name'])
elif r.status_code == 400:
    st.title("ERROR")
    st.write(res['message'])