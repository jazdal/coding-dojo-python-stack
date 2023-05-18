from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Message:
    db = "private_wall_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.sender_id = data["sender_id"]
        self.sender = data["sender"]
        self.receiver_id = data["receiver_id"]
        self.receiver = data["receiver"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif(math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"
    
    @classmethod
    def get_user_messages(cls, data):
        query = """
                SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users 
                LEFT JOIN messages ON users.id = messages.sender_id 
                LEFT JOIN users as users2 ON users2.id = messages.receiver_id 
                WHERE users2.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return [cls(message) for message in results]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO messages (content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)