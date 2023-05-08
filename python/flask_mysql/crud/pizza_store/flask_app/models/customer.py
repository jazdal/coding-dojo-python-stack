from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pizza

class Customer:
    db = "pizza_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.pizzas = []
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM customers
                LEFT JOIN pizzas
                ON pizzas.customer_id = customers.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        all_customers = []
        for row in results:
            c = cls(row)
            pizza_data = {
                "id": row["pizzas.id"], 
                "pizza_type": row["pizza_type"], 
                "pizza_crust": row["pizza_crust"], 
                "pizza_size": row["pizza_size"], 
                "pizza_sauce": row["pizza_sauce"], 
                "amount_of_toppings": row["amount_of_toppings"], 
                "created_at": row["pizzas.created_at"], 
                "updated_at": row["pizzas.updated_at"]
            }
            c.pizzas.append(pizza.Pizza(pizza_data))
            all_customers.append(c)
        return all_customers
    
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM customers
                JOIN pizzas
                ON pizzas.customer_id = customers.id
                WHERE id = %(id)s;
                """
        