from flask import Flask, render_template
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_data():
    # Add data processing logic here
    return "Data upload endpoint"

@app.route('/analysis')
def vulnerability_analysis():
    # Add analysis logic here
    return render_template('analysis.html')

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '0.0.0.0'), 
            port=os.getenv('FLASK_PORT', 5000))
