from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models import recipe

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return False if len(result) < 1 else cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return False if len(results) < 1 else cls(results[0])
    
    @classmethod
    def get_recipes(cls, data):
        query = """
                SELECT * FROM users 
                LEFT JOIN recipes 
                ON users.id = recipes.user_id 
                WHERE users.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            recipe_data = {
                "id": row["recipes.id"], 
                "name": row["name"], 
                "description": row["description"], 
                "under_30_mins": row["under_30_mins"], 
                "instructions": row["instructions"], 
                "created_at": row["recipes.created_at"], 
                "updated_at": row["recipes.updated_at"]
            }
            user.recipes.append(recipe.Recipe(recipe_data))
        return user
    
    @staticmethod
    def validate_user(user):
        is_valid = True

        if not user["first_name"]:
            flash("First name is required", "register")
            is_valid = False
        elif len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters", "register")
            is_valid = False
        
        if not user["last_name"]:
            flash("Last name is required", "register")
            is_valid = False
        elif len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters", "register")
            is_valid = False
        
        if not user["email"]:
            flash("Email address is required", "register")
            is_valid = False
        elif not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address format", "register")
            is_valid = False
        
        if not user["password"]:
            flash("Password is required", "register")
            is_valid = False
        
        if user["password"] != user["confirm_password"]:
            flash("Passwords do not match!", "register")
            is_valid = False
        
        return is_valid