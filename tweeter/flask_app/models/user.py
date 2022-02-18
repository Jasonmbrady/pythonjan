from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.tweet import Tweet

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tweets = []

    @staticmethod
    def is_valid(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        email_matches = connectToMySQL("tweeter").query_db(query, {"email": user['email']})
        if len(email_matches) > 0:
            flash("That email is already in use")
            is_valid = False
        if user["password"] != user["confirm-password"]:
            flash("Passwords do not match")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format")
            is_valid = False
        if len(user["password"]) < 8:
            flash("passwords must be at least 8 characters long!")
            is_valid = False
        return is_valid
        
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (name, email, password) VALUES (%(name)s, %(email)s, %(password)s)"
        results = connectToMySQL('tweeter').query_db(query, data) #Query returns the id of the new record
        return results #passing the id back to the controller

    @classmethod
    def read_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL("tweeter").query_db(query, data)
        if len(results) < 1:
            return False
        else:
            return cls(results[0])
        
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN tweets ON users.id = tweets.users_id WHERE users.id = %(id)s"
        results = connectToMySQL("tweeter").query_db(query, data)
        this_user = cls(results[0])
        for row in results:
            this_user.tweets.append(
                Tweet(
                    {
                        "id": row['tweets.id'],
                        "text": row["text"],
                        "created_at": row["tweets.created_at"],
                        "updated_at": row["tweets.updated_at"],
                        "users_id": this_user.id
                    }
                )
            )
        return this_user