from flask import flash
import re
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"(?=.*\d)(?=.*[A-Z])")

class User:
    db = "users_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.birthday = data["birthday"]
        self.region = data["region"]
        self.email = data["email"]
        self.password = data["password"]
        self.os = data["os"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.confirm_password = ""
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, birthday, region, email, password, os) VALUES (%(first_name)s, %(last_name)s, %(birthday)s, %(region)s, %(email)s, %(password)s, %(os)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(user) for user in results]
    
    @classmethod
    def get_by_email(cls, data):
        query = """
                SELECT * FROM users 
                WHERE email = %(email)s;
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        return False if len(result) <1 else cls(result[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        result = User.get_by_email(user)

        if len(user["fname"]) < 2:
            flash("First name must be at least 2 characters", "first_name")
            is_valid = False
        if not user["fname"].isalpha():
            flash("First name must only contain letters", "first_name")
            is_valid = False
        
        if len(user["lname"]) < 2:
            flash("Last name must be at least 2 characters", "last_name")
            is_valid = False
        if not user["lname"].isalpha():
            flash("Last name must only contain letters", "last_name")
            is_valid = False
        
        if not user["bday"]:
            flash("Birthday is required", "birthday")
            is_valid = False
        else:
            date_of_birth = datetime.strptime(user["bday"], "%Y-%m-%d")
            current_date = datetime.now()
            age = current_date.year - date_of_birth.year
            if age < 10:
                flash("Must be at least 10 yrs old to create an account", "birthday")
                is_valid = False

        if not user.get("region"):
            flash("Region needs to be selected", "region")
            is_valid = False

        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address", "email")
            is_valid = False
        if result:
            flash("Email already taken", "email")
            is_valid = False
        
        if len(user["password"]) < 8:
            flash("Password must be at least 8 characters", "password")
            is_valid = False
        
        if not PASSWORD_REGEX.match(user["password"]):
            flash("Password must contain at least one number and one uppercase letter", "password")
            is_valid = False
        
        if user["confirm_password"] != user["password"]:
            flash("Passwords must match!", "password")
            is_valid = False
        
        if not user.get("os"):
            flash("Please select an operating system", "first_name")
            is_valid = False
        
        return is_valid