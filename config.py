import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    DEBUG = os.getenv('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///data.db')
    NIST_API_KEY = os.getenv('NIST_API_KEY')
    ML_MODEL_PATH = os.getenv('ML_MODEL_PATH', 'ml/model.pkl')
