from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, ma
from routes.task_routes import task_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    frontend_url = os.environ.get('FRONTEND_URL', 'http://localhost:3000')

    CORS(app, resources={r"/api/*": {"origins": [frontend_url, "http://localhost:3000"]}})
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(task_bp, url_prefix='/api')
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.create_all()
        
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)