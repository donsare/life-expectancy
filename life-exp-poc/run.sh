#!/bin/sh

python3 -m venv ./venv

source venv/bin/activate

python3 -m pip install --upgrade pip

if [ -f "environment/requirements.txt" ]; then
    pip install -r environment/requirements.txt
fi

# Change directory to the app directory
cd app/api

# Run Flask app
export FLASK_APP=app
flask run
