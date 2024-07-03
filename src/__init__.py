from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig(app))
db = SQLAlchemy(app,add_models_to_shell=True)
migrate = Migrate(app, db)

from . import routes, model

@app.cli.command("seed")
def create_user():
	from seeds.seedDev import SeedDev
	seeder = SeedDev()
	seeder.run(app)