from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger

class Restaurant:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.burgers = []
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO restaurants (name) VALUES (%(name)s);"
        return connectToMySQL('burgers_schema').query_db(query, data)
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM restaurants;"
        results = connectToMySQL('burgers_schema').query_db(query)
        return [cls(restaurant) for restaurant in results]
    
    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM restaurants WHERE id = %(id)s;"
        result = connectToMySQL('burgers_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def show_one_with_burgers(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON restaurants.id = burgers.restaurant_id WHERE restaurants.id = %(id)s;"

        results = connectToMySQL('burgers_schema').query_db(query, data)
        restaurant = cls(results[0])

        for row_from_db in results:
            print(row_from_db)
            burger_data = {
                "id": row_from_db["burgers.id"], 
                "name": row_from_db["burgers.name"], 
                "bun": row_from_db["bun"], 
                "meat": row_from_db["meat"], 
                "calories": row_from_db["calories"], 
                "created_at": row_from_db["burgers.created_at"], 
                "updated_at": row_from_db["burgers.updated_at"]
            }
            print(burger_data)
            restaurant.burgers.append(burger.Burger(burger_data))

        return burger_data