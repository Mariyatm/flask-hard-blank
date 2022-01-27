from flask_restx import Resource, Namespace
from flask import request
from implemented import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genre')
genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



@genres_ns.route('/')
class genresView(Resource):

    def get(self):
        request_data = request.args
        genres = genre_service.get_all(request_data)
        return genres_schema.dump(genres), 200


    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genre_ns.route('/<int:uid>')
class genreView(Resource):
    def get(self, uid: int):
        try:
            genre = genre_service.get_one(uid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return "", 404

    def put(self):
        req_json = request.json
        genre_service.update(req_json)

    def delete(self, uid: int):
        try:
            genre_service.delete(uid)
            return "", 404
        except Exception as e:
            return "", 204
