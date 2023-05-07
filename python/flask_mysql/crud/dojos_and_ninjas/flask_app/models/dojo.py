from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(dojoname)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return [cls(dojo) for dojo in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db['ninjas.id'], 
                "first_name": row_from_db['first_name'], 
                "last_name": row_from_db['last_name'], 
                "age": row_from_db['age'], 
                "created_at": row_from_db['ninjas.created_at'], 
                "updated_at": row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo