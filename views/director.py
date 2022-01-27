from flask_restx import Resource, Namespace
from flask import request
from implemented import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('director')
directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)



@directors_ns.route('/')
class directorsView(Resource):

    def get(self):
        request_data = request.args
        directors = director_service.get_all(request_data)
        return directors_schema.dump(directors), 200


    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:uid>')
class directorView(Resource):
    def get(self, uid: int):
        try:
            director = director_service.get_one(uid)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404

    def put(self):
        req_json = request.json
        director_service.update(req_json)

    def delete(self, uid: int):
        try:
            director_service.delete(uid)
            return "", 404
        except Exception as e:
            return "", 204
