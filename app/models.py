# models.py
from app import db
import hashlib  # Add hashlib for SHA-256
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hash the password using SHA-256."""
        self.password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        """Verify the password against the stored hash."""
        return self.password_hash == hashlib.sha256(password.encode('utf-8')).hexdigest()

class Log(db.Model):
    __tablename__ = 'logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ip_address = db.Column(db.String(50))
    browser = db.Column(db.Text)
    country = db.Column(db.String(100))
    region = db.Column(db.String(100))
    city = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    path = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)