from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_assignment').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email) VALUES ( %(f_name)s, %(l_name)s, %(email)s);"
        results = connectToMySQL('users_assignment').query_db(query, data)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_assignment').query_db(query, data)
        this_user = cls(results[0])
        return this_user
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s WHERE id = %(id)s"
        connectToMySQL('users_assignment').query_db(query, data)
        return data['id']

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        results = connectToMySQL('users_assignment').query_db(query, data)
        return results