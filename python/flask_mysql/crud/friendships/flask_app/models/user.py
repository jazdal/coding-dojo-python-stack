from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "friendships_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(user) for user in results]
    
    @classmethod
    def get_friendships(cls):
        query = """
                SELECT * FROM users
                LEFT JOIN friendships
                ON users.id = friendships.user_id
                LEFT JOIN users AS friends
                ON friendships.friend_id = friends.id;
                """
        results = connectToMySQL(cls.db).query_db(query)
        friendships = []
        for row in results:
            parsed_data = {
                "user_id": row["id"], 
                "user_fname": row["first_name"], 
                "user_lname": row['last_name'], 
                "user_created_at": row['created_at'], 
                "user_updated_at": row['updated_at'], 
                "friend_id": row['friends.id'], 
                "friend_fname": row['friends.first_name'] if not row['friends.first_name'] == None else "", 
                "friend_lname": row['friends.last_name'] if not row['friends.last_name'] == None else "", 
                "friend_created_at": row['friends.created_at'], 
                "friend_updated_at": row['friends.updated_at']
            }
            friendships.append(parsed_data)
        return friendships
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def add_friend(cls, data):
        query = """
                INSERT INTO friendships (user_id, friend_id) 
                SELECT %(user_id)s, %(friend_id)s
                WHERE NOT EXISTS (
                    SELECT 1 FROM friendships
                    WHERE user_id = %(user_id)s
                    AND friend_id = %(friend_id)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)