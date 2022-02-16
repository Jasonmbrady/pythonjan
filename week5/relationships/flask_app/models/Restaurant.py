from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Burger import Burger
class Restaurant:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burgers = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO restaurants (name) VALUES (%(name)s)"
        results = connectToMySQL("burger_restaurants").query_db(query, data)
        return results
    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM restaurants"
        rest_list = []
        results = connectToMySQL("burger_restaurants").query_db(query)
        for row in results:
            rest_list.append(cls(row))
        return rest_list

    @classmethod
    def read_one_w_burgers(cls):
        query = "SELECT * FROM restaurants JOIN burgers ON restaurants.id = burgers.restaurant_id;"
        results = connectToMySQL("burger_restaurants").query_db(query)
        print(results)
        # restaurants = []
        # for row in results:
            # compare the restaurants.id with each dictionary already in 
        # rest = (cls(results[0]))
        # for row in results:
        #     burger= {
        #         "id": row['id'],
        #         "name": row["name"],
        #         "meat": row["meat"],
        #         "bun": row["bun"],
        #         "cheese": row["cheese"],
        #         "calories": row["calories"],
        #         "created_at": row["created_at"],
        #         "updated_at": row["updated_at"]
        #     }
        #     rest.burgers.append(Burger(burger))
        # return rest



        