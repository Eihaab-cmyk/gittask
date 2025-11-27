from flask import Flask
from config import Config
from extensions import db, ma
from routes.job_routes import job_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    app.register_blueprint(job_bp)
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)