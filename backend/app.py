from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, ma
from routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(task_bp, url_prefix='/api')
    
    with app.app_context():
        db.create_all()
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)