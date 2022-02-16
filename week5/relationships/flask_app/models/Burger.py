from flask_app.config.mysqlconnection import connectToMySQL

class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.restaurant = data['restaurant']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers"
        results = connectToMySQL("burger_restaurants").query_db(query)
        all_burgers = []
        for row in results:
            all_burgers.append(cls(row))
        return all_burgers

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM burgers WHERE id=%(id)s"
        results = connectToMySQL("burger_restaurants").query_db(query, data)
        burger = cls(results[0])
        return burger

    @classmethod
    def create(cls, data):
        query = "INSERT INTO burgers (name, bun, meat, cheese, calories, restaurant_id) VALUES (%(name)s, %(bun)s, %(meat)s, %(cheese)s, %(calories)s, %(restaurant)s);"
        results = connectToMySQL("burger_restaurants").query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name = %(name)s, bun = %(bun)s, meat = %(meat)s, cheese = %(cheese)s, calories = %(calories)s, updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL("burger_restaurants").query_db(query, data)
        return data['id']

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM burgers WHERE id=%(id)s"
        connectToMySQL("burger_restaurants").query_db(query, data)
        return
    
    @classmethod
    def read_all_with_rest(cls):
        pass
