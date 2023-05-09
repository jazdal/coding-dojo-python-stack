from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors_favorite = []
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO books (title, num_of_pages) 
                VALUES (%(title)s, %(num_of_pages)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(book) for book in results]
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_authors_favorite(cls, data):
        query = """
                SELECT * FROM books 
                LEFT JOIN favorites 
                ON favorites.book_id = books.id 
                LEFT JOIN authors 
                ON authors.id = favorites.author_id 
                WHERE books.id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_data = {
                "id": row["authors.id"], 
                "name": row["name"], 
                "created_at": row["authors.created_at"], 
                "updated_at": row["authors.updated_at"]
            }
            print(author_data)
            book.authors_favorite.append(author.Author(author_data))
        return book