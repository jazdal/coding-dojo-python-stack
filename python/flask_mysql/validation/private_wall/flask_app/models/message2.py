from flask_app.config.mysqlconnection import connectToMySQL

class Message2:
    db = "private_wall_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.sender_id = data["sender_id"]
        self.receiver_id = data["receiver_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_sent_messages(cls, data):
        query = "SELECT * FROM messages WHERE sender_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return [cls(message) for message in results]