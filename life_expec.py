import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# Load the saved model and scaler
with open(r"C:\Users\dell\Desktop\streamlit apps\life_expectancy_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# with open(r"C:\Users\dell\Desktop\Jup\scaler.pkl", "rb") as scaler_file:
#     scaler = pickle.load(scaler_file)

# List of all possible countries 
countries = [
    'Albania', 'Algeria', 'Argentina', 'Armenia', 'Austria',
       'Azerbaijan', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria',
       'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Chile',
       'Colombia', 'Comoros', 'Costa Rica', 'Cyprus', 'Djibouti',
       'Dominican Republic', 'Ecuador', 'El Salvador',
       'Equatorial Guinea', 'Estonia', 'Fiji', 'Gabon', 'Georgia',
       'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Honduras',
       'Iraq', 'Israel', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kiribati',
       'Latvia', 'Lebanon', 'Liberia', 'Lithuania', 'Luxembourg',
       'Madagascar', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Mauritania', 'Mauritius', 'Mexico', 'Mongolia', 'Montenegro',
       'Morocco', 'Myanmar', 'Namibia', 'Nepal', 'Nicaragua', 'Niger',
       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Poland',
       'Portugal', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa',
       'Sao Tome and Principe', 'Senegal', 'Serbia', 'Seychelles',
       'Solomon Islands', 'Sri Lanka', 'Suriname', 'Syrian Arab Republic',
       'Tajikistan', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
       'Ukraine', 'Uruguay', 'Uzbekistan', 'Vanuatu'
]


# Streamlit UI
st.title("Life Expectancy Prediction App")

# User input
country = st.selectbox("Select Country", countries)
year = st.slider("Select Year", 2000, 2025, 2015)  # Adjust range if needed
status = st.selectbox("Status", ["Developed", "Developing"])
adult_mortality = st.number_input("Adult Mortality Rate", min_value=0)
infant_deaths = st.number_input("Infant Deaths", min_value=0)
alcohol = st.number_input("Alcohol Consumption")
percentage_expenditure = st.number_input("Percentage Expenditure")
hepatitis_b = st.number_input("Hepatitis B Immunization (%)", min_value=0, max_value=100)
measles = st.number_input("Measles Cases", min_value=0)
bmi = st.number_input("BMI")
under_five_deaths = st.number_input("Under-five Deaths", min_value=0)
polio = st.number_input("Polio Immunization (%)", min_value=0, max_value=100)
total_expenditure = st.number_input("Total Health Expenditure")
diphtheria = st.number_input("Diphtheria Immunization (%)", min_value=0, max_value=100)
hiv_aids = st.number_input("HIV/AIDS Death Rate")
gdp = st.number_input("GDP per Capita")
population = st.number_input("Population")
thinness_1_19 = st.number_input("Thinness 1-19 years (%)")
thinness_5_9 = st.number_input("Thinness 5-9 years (%)")
income_composition = st.number_input("Income Composition of Resources")
schooling = st.number_input("Schooling Years")

# Encode categorical variables
country_encoded = countries.index(country)  # Convert country to numerical index
status_encoded = 1 if status == "Developing" else 0  # Encode status (Developed=1, Developing=0)

# Create input array
input_data = np.array([
    country_encoded, year, status_encoded, adult_mortality, infant_deaths, alcohol,
    percentage_expenditure, hepatitis_b, measles, bmi, under_five_deaths, polio,
    total_expenditure, diphtheria, hiv_aids, gdp, population, thinness_1_19,
    thinness_5_9, income_composition, schooling
]).reshape(1, -1)

# Scale the input
# input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Life Expectancy"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Life Expectancy: {prediction[0]:.2f} years")
