from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger

class Restaurant:
    db = "burgers_schema"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.burgers = []
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO restaurants (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM restaurants;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(restaurant) for restaurant in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM restaurants WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_burgers_from_restaurant(cls, data):
        query = """
                SELECT * FROM restaurants 
                LEFT JOIN burgers 
                ON restaurants.id = burgers.restaurant_id 
                WHERE restaurants.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        restaurant = cls(results[0])
        for row in results:
            burger_data = {
                "id": row["burgers.id"], 
                "name": row["burgers.name"], 
                "bun": row["bun"], 
                "meat": row["meat"], 
                "calories": row["calories"], 
                "created_at": row["burgers.created_at"], 
                "updated_at": row["burgers.updated_at"]
            }
            restaurant.burgers.append(burger.Burger(burger_data))
        return restaurant