import streamlit as st
import numpy as np
import joblib


model = joblib.load('model.pkl')

st.title('Predict Profits From Spending')

st.divider()

st.write('Please enter the following details to predict the Profit:')
st.divider()

MarketingSpend = st.number_input('Marketing Spend', value=0, step=100)

X = [MarketingSpend]

st.divider()

prediction = st.button('Profit Prediction Button')

st.divider()

if prediction:
    x1 = np.array(X)
    prediction = model.predict([x1])[0]
    st.write(f'The predicted profits is: ${prediction[0]:.2f}')
else:
    st.write('Please fill in the details and click the button to get the profit prediction.')
    
