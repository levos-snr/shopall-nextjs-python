# api/__init__.py
from .config import app, db
from . import main

# This line is crucial for Vercel
app = app