from app import app
from flask import render_template
from content.recent_judgments import recent_judgments
from content.service_wide import service

@app.route('/')
def home():
    return render_template('home.html', service=service, recent_judgments=recent_judgments)