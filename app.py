

from flask import Flask
from flask_restx import Api

from config import Config
# from dao.model import *
from setup_db import db
from views.director import director_ns, directors_ns
from views.genre import genre_ns, genres_ns
from views.movie import movie_ns, movies_ns

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
