# Creating a Flask App for Life Expectancy Prediction:

import os
import joblib
import pandas as pd
from catboost import CatBoostRegressor
from flask import Flask, request, jsonify

app = Flask(__name__)

# Print the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Go back two levels (up to the project_name directory)
parent_directory = os.path.abspath(os.path.join(cwd))

# Define the path to the model
model_path = os.path.join(parent_directory, "models", "lePredictor2.pkl")
print(f"Resolved model path: {model_path}")

# Load the trained model
with open(model_path, 'rb') as model_file:
    model = joblib.load(model_file)

@app.route('/predict_life_expectancy', methods=['POST'])
def predict_life_expectancy():
    data = request.json
    required_fields = [
        'AdultM', 'HIV', 'BMI', 'Diph', 'GDP', 'Schooling', 'Thin5_9Yrs', 'Alcohol', 'Polio'
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    input_data = [[data[field] for field in required_fields]]  # Note the double brackets for predict_model

    try:
        prediction = model.predict(input_data)[0]
        return jsonify({"predicted_life_expectancy": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


