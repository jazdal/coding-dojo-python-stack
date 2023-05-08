from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger

class Topping:
    db = "burgers_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.topping_name = data["topping_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.on_burgers = []
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO toppings (topping_name) 
                VALUES (%(topping_name)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_topping_with_burgers(cls, data):
        query = """
                SELECT * FROM toppings 
                LEFT JOIN add_ons 
                ON add_ons.topping_id = toppings.id 
                LEFT JOIN burgers 
                ON add_ons.burger_id = burgers.id 
                WHERE toppings.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        topping = cls(results[0])
        for row in results:
            burger_data = {
                "id": row["burgers.id"], 
                "name": row["name"], 
                "bun": row["bun"], 
                "calories": row["calories"], 
                "created_at": row["burgers.created_at"], 
                "updated_at": row["burgers.updated_at"]
            }
            topping.on_burgers.append(burger.Burger(burger_data))
        return topping