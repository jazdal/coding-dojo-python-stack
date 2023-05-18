from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30_mins = data["under_30_mins"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO recipes (name, description, under_30_mins, instructions, created_at, user_id) 
                VALUES (%(name)s, %(description)s, %(under_30_mins)s, %(instructions)s, %(created_at)s, %(user_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return False if len(result) <1 else cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, under_30_mins = %(under_30_mins)s, instructions = %(instructions)s, created_at = %(created_at)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        if not recipe["name"]:
            flash("Recipe name is required", "login")
            is_valid = False
        elif len(recipe["name"]) < 3:
            flash("Recipe name must be at least 3 characters long", "login")
            is_valid = False
        
        if not recipe["description"]:
            flash("A brief description of the recipe is required", "login")
            is_valid = False
        elif len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters long", "login")
            is_valid = False
        
        if not recipe["instructions"]:
            flash("Can't cook your recipe if you don't provide instructions!", "login")
            is_valid = False
        elif len(recipe["instructions"]) < 3:
            flash("Instructions must be at least 3 characters long", "login")
            is_valid = False
        
        if not recipe["created_at"]:
            flash("Date created is required", "login")
            is_valid = False
        
        return is_valid