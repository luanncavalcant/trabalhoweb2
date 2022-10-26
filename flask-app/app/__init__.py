from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app=Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

from app.model.autor import Autor
from app.model.post import Post

from app.controller import autor_controller
from app.controller import post_controller

