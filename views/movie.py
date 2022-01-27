from flask_restx import Resource, Namespace
from flask import request
from implemented import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movie')
movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)



@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        request_data = request.args
        movies = movie_service.get_all(request_data)
        return movies_schema.dump(movies), 200


    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self):
        req_json = request.json
        movie_service.update(req_json)

    def delete(self, uid: int):
        try:
            movie_service.delete(uid)
            return "", 404
        except Exception as e:
            return "", 204
