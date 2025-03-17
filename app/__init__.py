# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    csrf.init_app(app)
    
    # Security headers middleware
    @app.after_request
    def add_security_headers(response):
        # XSS protection
        response.headers['X-XSS-Protection'] = '1; mode=block'
        # Prevent MIME sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response
    
    from app.auth import auth_bp
    from app.routes import routes_bp
    
    # Register Blueprints with URL prefix
    app.register_blueprint(auth_bp, url_prefix='/flaskdemo')
    app.register_blueprint(routes_bp, url_prefix='/flaskdemo')
    
    return app