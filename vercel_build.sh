#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
flask --app main.py db migrate
flask --app main.py db upgrade