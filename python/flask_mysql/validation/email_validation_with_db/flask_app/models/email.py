from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db = "email_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(object) for object in results]
    
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        return cls(results[len(results) -1]) if results else "None"
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True

        results = Email.get_all()
        for result in results:
            if email['email'] == result.email:
                flash("Email address must be unique!", 'warning')
                is_valid = False
            continue
        
        if not email['email']:
            flash("Email cannot be blank!", 'warning')
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!", 'error')
            is_valid = False
        return is_valid