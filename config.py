# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    MYSQL_HOST = 'localhost'  # Ensure this matches XAMPP's MySQL host
    MYSQL_USER = 'root'       # Default XAMPP MySQL username
    MYSQL_PASSWORD = ''       # Default XAMPP MySQL password (empty)
    MYSQL_DB = 'flask_logs'   # Ensure this database exists in XAMPP
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/flask_logs"  # Use pymysql
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True