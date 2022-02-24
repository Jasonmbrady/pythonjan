from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

my_db = "live_shows"

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.band_name = data['band_name']
        self.date = data['date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL(my_db).query_db(query)
        all_shows = []
        for row in results:
            all_shows.append( cls(row) )
        return all_shows

    @classmethod
    def create(cls, data):
        query = "INSERT INTO shows (band_name, date, description, user_id) VALUES (%(band_name)s, %(date)s, %(description)s, %(user_id)s);"
        results = connectToMySQL(my_db).query_db(query, data)
        return results
    
    @classmethod
    def read_by_id(cls, data):
        query = "SELECT * FROM shows WHERE id=%(id)s;"
        results = connectToMySQL(my_db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET band_name=%(band_name)s, date=%(date)s, description=%(description)s, user_id=%(user_id)s, updated_at=NOW() WHERE id=%(id)s"
        connectToMySQL(my_db).query_db(query, data)
        return

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id=%(id)s;"
        connectToMySQL(my_db).query_db(query, data)
        return