from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db = "dojo_survey_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos 
                (name, location, language, comment) 
                VALUES 
                (%(name)s, %(location)s, %(language)s, %(comment)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(dojo) for dojo in results]
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if not dojo['name']:
            flash("Name is required.")
            is_valid = False
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not dojo['location']:
            flash("Dojo location is required.")
            is_valid = False
        if not dojo['language']:
            flash("Favorite language is required.")
            is_valid = False
        if not dojo['comment']:
            flash("Comments are required.")
            is_valid = False
        return is_valid