from dao.dao_model import ModelDAO
from service.model import ModelService
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db


movie_dao = ModelDAO(Movie, db.session)
movie_service =ModelService(dao=movie_dao)

genre_dao = ModelDAO(Genre, db.session)
genre_service = ModelService(dao=genre_dao)

director_dao = ModelDAO(Director, db.session)
director_service =ModelService(dao=director_dao)
