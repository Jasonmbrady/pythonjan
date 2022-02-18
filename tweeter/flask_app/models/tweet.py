from flask_app.config.mysqlconnection import connectToMySQL

class Tweet:
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO tweets (text, users_id) VALUES (%(text)s, %(users_id)s);"
        results = connectToMySQL("tweeter").query_db(query, data)
        return results