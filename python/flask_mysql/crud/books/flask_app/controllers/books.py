from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route("/books", methods=['GET', 'POST'])
def new_book():
    if request.method == 'GET':
        return render_template("books.html", all_books = Book.get_all())
    else:
        Book.create(request.form)
        return redirect("/books")

@app.route("/books/<id>", methods=['GET', 'POST'])
def book_favorite(id):
    data = {"id": id}
    
    if request.method == 'GET':
        books = Book.get_authors_favorite(data)
        authors_with_favorites = [author.name for author in books.authors_favorite]
        
        authors = Author.get_all()
        free_authors = [author for author in authors if author.name not in authors_with_favorites]

        return render_template("show_books.html", one_book = Book.get_one(data), books = books, authors = free_authors)
    
    else:
        Author.add_favorite(request.form)
        return redirect(f"/books/{id}")