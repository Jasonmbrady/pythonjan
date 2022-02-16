from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.num_of_items = data['num_of_items']
        self.summary = data['summary']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    