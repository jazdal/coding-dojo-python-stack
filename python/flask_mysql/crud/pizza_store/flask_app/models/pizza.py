from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.customer import Customer

class Pizza:
    db = "pizza_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.pizza_type = data["pizza_type"]
        self.pizza_crust = data["pizza_crust"]
        self.pizza_size = data["pizza_size"]
        self.pizza_sauce = data["pizza_sauce"]
        self.amount_of_toppings = data["amount_of_toppings"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pizzas;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(pizza) for pizza in results]
    
    @classmethod
    def get_one(cls, data):
        cust = Customer.get_all()
        query = "SELECT * FROM pizzas WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO pizzas (pizza_type, pizza_crust, pizza_size, pizza_sauce, amount_of_toppings, customer_id) 
                VALUES (%(pt)s, %(pc)s, %(psz)s, %(ps)s, %(t)s, %(customer_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE pizzas SET pizza_type = %(pt)s, pizza_crust = %(pc)s, pizza_size = %(psz)s, pizza_sauce = %(ps)s, amount_of_toppings = %(t)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pizzas WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)