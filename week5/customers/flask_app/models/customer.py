from flask_app.config.mysqlconnection import connectToMySQL

class Customer:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.orders = []

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM customers;"
        results = connectToMySQL('customer').query_db(query)
        cust_list = []
        for row in results:
            cust_list.append(cls(row))
        return cust_list
    
