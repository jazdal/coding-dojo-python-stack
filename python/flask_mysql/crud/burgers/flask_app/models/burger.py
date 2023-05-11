from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping

class Burger:
    db = "burgers_schema"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.bun = db_data['bun']
        self.meat = db_data['meat']
        self.calories = db_data['calories']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.toppings = []
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO burgers 
                (name, bun, meat, calories, restaurant_id) 
                VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(burger) for burger in results]
    
    @classmethod
    def get_burger_with_toppings(cls, data):
        query = """
                SELECT * FROM burgers 
                LEFT JOIN add_ons 
                ON add_ons.burger_id = burgers.id 
                LEFT JOIN toppings 
                ON add_ons.topping_id = toppings.id 
                WHERE burgers.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        burger = cls(results[0])
        for row in results:
            topping_data = {
                "id": row["toppings.id"], 
                "topping_name": row["topping_name"], 
                "created_at": row["toppings.created_at"], 
                "updated_at": row["toppings.updated_at"]
            }
            burger.toppings.append(topping.Topping(topping_data))
        return burger
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate_burger(burger):
        is_valid = True
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Meat must be at least 3 characters.")
            is_valid = False
        return is_valid