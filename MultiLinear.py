import streamlit as st
import numpy as np
import joblib


model1 = joblib.load('multilinear.pkl')

st.title('Predict Profits From Spending')

st.divider()

st.write('Please enter the following details to predict the Profit:')
st.divider()

RDSpend = st.number_input('R&D Spend', value=0, step=100)
MarketingSpend = st.number_input('Marketing Spend', value=0, step=100)

X = [RDSpend , MarketingSpend]

st.divider()

prediction = st.button('Profit Prediction Button')

st.divider()

if prediction:
    x1 = np.array(X)
    prediction = model1.predict([x1])[0]
    st.write('The predicted price of the laptop is: ${:.2f}'.format(prediction))
else:
    st.write('Please fill in the details and click the button to get the profit prediction.')