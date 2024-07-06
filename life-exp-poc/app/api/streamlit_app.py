
# Creating the Streamlit App for the Life Expectancy Predictor:

import streamlit as st
from datetime import datetime
import pytz
import requests

# Set the timezone to UTC+03
tz = pytz.timezone('Etc/GMT-3')

# Get the current time in the specified timezone
current_time = datetime.now(tz)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .header {
        color: #ff4b4b;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .subheader {
        color: #4b4bff;
        font-size: 24px;
        text-align: center;
    }
    .input-label {
        color: #800080;  # Purple color
        font-size: 18px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stAlert {
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Streamlit App Interface (Header)
    st.markdown("<div class='header'>Life Expectancy Predictor</div>", unsafe_allow_html=True)
    
    # Display the current time with timezone in Streamlit
    st.markdown(f"<div class='subheader'>{current_time.strftime('%Y-%m-%d %H:%M:%S UTC+03')}</div>", unsafe_allow_html=True)

    st.markdown("<div class='input-label'>Number of people dying between 15-60 years per 1000 population</div>", unsafe_allow_html=True)
    AdultM = st.number_input("", min_value=1, key="AdultM")
    
    st.markdown("<div class='input-label'>HIV/AIDS deaths per 1000 population</div>", unsafe_allow_html=True)
    HIV = st.number_input("", min_value=1, key="HIV")
    
    st.markdown("<div class='input-label'>Average body mass index (BMI) of the entire population</div>", unsafe_allow_html=True)
    BMI = st.number_input("", min_value=0.01, key="BMI")
    
    st.markdown("<div class='input-label'>Percent of diphtheria immunization coverage among one year olds</div>", unsafe_allow_html=True)
    Diph = st.number_input("", min_value=0.01, key="Diph")
    
    st.markdown("<div class='input-label'>Gross domestic product (GDP) per capita in dollars</div>", unsafe_allow_html=True)
    GDP = st.number_input("", min_value=0.01, key="GDP")
    
    st.markdown("<div class='input-label'>Number of years spent in school</div>", unsafe_allow_html=True)
    Schooling = st.number_input("", min_value=0.01, key="Schooling")
    
    st.markdown("<div class='input-label'>Percent (%) of thinness among children from age 5-9</div>", unsafe_allow_html=True)
    Thin5_9Yrs = st.number_input("", min_value=0.01, key="Thin5_9Yrs")
    
    st.markdown("<div class='input-label'>Recorded per capita alcohol consumption (in litres)</div>", unsafe_allow_html=True)
    Alcohol = st.number_input("", min_value=0.01, key="Alcohol")
    
    st.markdown("<div class='input-label'>Percent of polio immunization coverage among one year olds</div>", unsafe_allow_html=True)
    Polio = st.number_input("", min_value=0.01, key="Polio")

    if st.button("Predict Life Expectancy"):
        # Check if any input is zero
        if (AdultM <= 0 or HIV <= 0 or BMI <= 0 or Diph <= 0 or GDP <= 0 or Schooling <= 0 or Thin5_9Yrs <= 0 or Alcohol <= 0 or Polio <= 0):
            st.error("All input values must be greater than zero.")
        else:
            url = "https://leprediction.onrender.com/predict_life_expectancy"
            data = {
                "AdultM": AdultM,
                "HIV": HIV,
                "BMI": BMI,
                "Diph": Diph,
                "GDP": GDP,
                "Schooling": Schooling,
                "Thin5_9Yrs": Thin5_9Yrs,
                "Alcohol": Alcohol,
                "Polio": Polio
            }
            
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json()
                predicted_life_expectancy = int(result['predicted_life_expectancy'])
                st.success(f"Predicted Life Expectancy (in years): {predicted_life_expectancy}")
            else:
                st.error(f"Error: {response.json()['error']}")

if __name__ == "__main__":
    main()

