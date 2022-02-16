from flask_app.config.mysqlconnection import connectToMySQL

class Burger:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM burgers WHERE id=%(id)s"
        connectToMySQL("burgers").query_db(query, data)
        return
    
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM burgers WHERE id=%(id)s"
        results = connectToMySQL("burgers").query_db(query, data)
        return results[0]

    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name= %(name)s, bun= %(bun)s, meat= %(meat)s WHERE id = %(id)s"
        connectToMySQL("burgers").query_db(query, data)
        return