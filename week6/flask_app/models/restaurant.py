from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.burger import Burger
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Restaurant:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burgers = []

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM restaurants"
        results = connectToMySQL("burgers").query_db(query)
        all_restaurants = []
        for row in results:
            all_restaurants.append( cls(row))
        return all_restaurants

    @classmethod
    def create(cls, data):
        query = "INSERT INTO restaurants (name) VALUES (%(name)s)"
        results = connectToMySQL("burgers").query_db(query, data)
        return results
    
    @classmethod
    def read_one_with_burgers(cls, data):
        query = "SELECT * from restaurants LEFT JOIN burgers ON restaurants.id = burgers.restaurants_id WHERE restaurants.id = %(id)s"
        results = connectToMySQL("burgers").query_db(query, data)
        this_restaurant = cls(results[0])
        for row in results:
            burger_data = {
                "id": row['burgers.id'],
                "name": row['burgers.name'],
                "bun": row["bun"],
                "meat": row['meat'],
                "created_at" : row["burgers.created_at"],
                "updated_at" : row["burgers.updated_at"]
            }
            this_restaurant.burgers.append(Burger(burger_data))
        return this_restaurant

    @staticmethod
    def validate_restaurant(restaurant):
        is_valid = True
        if len(restaurant['name']) < 3:
            is_valid = False
            flash("Restaurant names must be at least 3 characters long")
        if not EMAIL_REGEX.match(restaurant['name']):
            is_valid = False
            flash("Restaurant names must be email addresses!")
        return is_valid