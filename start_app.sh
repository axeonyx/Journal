#!/bin/bash

# Navigate to the application directory
cd /Users/axie/Journal

# Activate the virtual environment
source myenv/bin/activate

# Start the Flask app
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
