#!/bin/sh

# Create a virtual environment
python3 -m venv ./venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install the required packages
if [ -f "environment/requirements.txt" ]; then
    pip install -r environment/requirements.txt
fi

# Change directory to the app directory
cd app/api

# Run the Streamlit app
streamlit run streamlit_app.py
