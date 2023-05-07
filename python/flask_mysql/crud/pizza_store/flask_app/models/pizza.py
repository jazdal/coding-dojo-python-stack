from flask_app.config.mysqlconnection import connectToMySQL

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
        print(results)
        return [cls(pizza) for pizza in results]