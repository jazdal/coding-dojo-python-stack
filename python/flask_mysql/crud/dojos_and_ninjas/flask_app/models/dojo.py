from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(dojoname)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(dojo) for dojo in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_ninjas_from_dojo(cls, data):
        query = """
                SELECT * FROM dojos 
                LEFT JOIN ninjas 
                ON ninjas.dojo_id = dojos.id 
                WHERE dojos.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row['ninjas.id'], 
                "first_name": row['first_name'], 
                "last_name": row['last_name'], 
                "age": row['age'], 
                "created_at": row['ninjas.created_at'], 
                "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo