import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_PJuvXKi7Dp3m@ep-quiet-moon-a88xys0b-pooler.eastus2.azure.neon.tech:5432/neondb?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads') 