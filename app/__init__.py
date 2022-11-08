from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

<<<<<<< HEAD
    from app.Models.planets import Planet
=======
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    
    from app.models.planets import Planet
>>>>>>> f9096b15a0041b6a85297f2395e5ba37b8db28c1

    db.init_app(app)
    migrate.init_app(app, db)

    from app.planets import planet_bp
    app.register_blueprint(planet_bp)
    
    return app
