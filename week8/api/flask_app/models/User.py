from flask_app.config.mysqlconnection import connectToMySQL
import os
import requests
from flask import jsonify

class User:
    db = "my_weather"
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.lat = data['lat']
        self.lon = data['lon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_dict(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results[0]

    @classmethod
    def get_by_username(cls, data):
        query = "SELECT * FROM users WHERE username=%(username)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (username, password, lat, lon) VALUES (%(username)s, %(password)s, %(lat)s, %(lon)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET lat=%(lat)s, lon=%(lon)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        return