from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import restaurant

class Burger:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.bun = db_data['bun']
        self.meat = db_data['meat']
        self.calories = db_data['calories']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO burgers (name, bun, meat, calories, restaurant_id) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s);"
        return connectToMySQL('burgers_schema').query_db(query, data)
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL('burgers_schema').query_db(query)
        return [cls(burger) for burger in results]
    
    @classmethod
    def show_burgers_from_restaurants(cls, data):
        query = "SELECT * FROM burgers LEFT JOIN restaurants ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        results = connectToMySQL('burgers_schema').query_db(query, data)
        burger_data = []
        for burger in results:
            burger_dict = {
                "id": burger['id'], 
                "name": burger['name'], 
                "bun": burger['bun'], 
                "meat": burger['meat'], 
                "calories": burger['calories'], 
                "restaurant_id": burger['restaurant_id'], 
                "created_at": burger['created_at'], 
                "updated_at": burger['updated_at'], 
                "restaurantid": burger['restaurants.id'], 
                "restaurant_name": burger['restaurants.name'], 
                "restaurant_created_at": burger['restaurants.created_at'], 
                "restaurant_updated_at": burger['restaurants.updated_at']
            }
            burger_data.append(burger_dict)
        return burger_data
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgers_schema').query_db(query, data)