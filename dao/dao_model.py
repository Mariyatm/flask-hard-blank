# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

class ModelDAO:
    def __init__(self, model, session):
        self.model = model
        self.session = session

    def get_one(self, uid):
        return self.session.query(self.model).get(uid)

    def get_all(self, data):
        res = self.session.query(self.model)
        if data and data.get("director_id") is not None:
            print("????"+data.get("director_id"))
            res = res.filter(self.model.director_id == data.get("director_id"))
        if data and data.get("genre_id") is not None:
            res = res.filter(self.model.genre_id == data.get("genre_id"))
        if data and data.get("year") is not None:
            res = res.filter(self.model.year == data.get("year"))
        return res

    def create(self, data):
        element = self.model(**data)
        self.session.add(element)
        self.session.commit()
        return element

    def update(self, element):
        self.session.add(element)
        self.session.commit()

    def delete(self, uid):
        element = self.get_one(uid)
        self.session.delete(element)
        self.session.commit()
