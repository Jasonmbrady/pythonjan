from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.User import User
from flask import flash

class Truck:
    db = "food_trucks"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']
        self.liked_by = []

    @staticmethod
    def validate(truck):
        is_valid = True
        if len(truck['name']) < 3:
            flash("Truck names must be at least 3 characters")
            is_valid = False
        if len(truck['type']) < 3:
            flash("Truck food types must be at least 3 characters")
            is_valid = False
        return is_valid

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM trucks JOIN users ON trucks.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_trucks = []
        for row in results:
            user_data = {
                "id" : row["users.id"],
                "username": row["username"],
                "email": row['email'],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            this_user = User(user_data)
            row["user"] = this_user
            all_trucks.append( cls(row) )
        return all_trucks

    @classmethod
    def create(cls, data):
        query = "INSERT INTO trucks (name, type, user_id) VALUES (%(name)s, %(type)s, %(user_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def read_by_id(cls, data):
        query = "SELECT * FROM trucks JOIN users ON trucks.user_id = users.id WHERE trucks.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        row = results[0]
        user_data = {
                "id" : row["users.id"],
                "username": row["username"],
                "email": row['email'],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
        row['user'] = User(user_data)
        return cls(row)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM trucks WHERE id=%(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return

    @classmethod
    def update(cls, data):
        query = "UPDATE trucks SET name=%(name)s, type=%(type)s, updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return

    @classmethod
    def like_truck(cls, data):
        query = "INSERT INTO likes (user_id, truck_id) VALUES (%(user_id)s, %(truck_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def read_truck_with_likes(cls, data):
        query = "SELECT * FROM likes LEFT JOIN users ON likes.user_id = users.id LEFT JOIN trucks ON likes.truck_id = trucks.id WHERE trucks.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        truck_data = {
            "id": results[0]["trucks.id"],
            "name": results[0]["name"],
            "type": results[0]["type"],
            "created_at": results[0]["trucks.created_at"],
            "updated_at": results[0]["trucks.updated_at"],
            "user": User.get_by_id({"id": results[0]["trucks.user_id"]})
        }
        print(results)
        this_truck = cls(truck_data)
        for row in results:
            user_data = {
                "id" : row["users.id"],
                "username": row["username"],
                "email": row['email'],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            this_truck.liked_by.append(User(user_data))
        return this_truck