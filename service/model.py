from dao.dao_model import ModelDAO


class ModelService:

    def __init__(self, dao: ModelDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self, data):
        return self.dao.get_all(data)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        self.dao.delete(uid)
        self.dao.create(data)

    def delete(self, uid):
        self.dao.delete(uid)
