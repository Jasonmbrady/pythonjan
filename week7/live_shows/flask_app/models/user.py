from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
my_db = "live_shows"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_reg(user):
        is_valid = True
        if user['password'] != user['confirm_pw']:
            is_valid = False
            flash("passwords don't match")
        return is_valid

    @classmethod
    def read_all():
        pass

    @classmethod
    def read_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(my_db).query_db(query, data)
        if len(results > 0):
            return cls(results[0])
        else:
            return False

    @classmethod
    def read_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(my_db).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        results = connectToMySQL(my_db).query_db(query, data)
        return results