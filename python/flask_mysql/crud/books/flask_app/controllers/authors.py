from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/")
def reroute():
    return redirect("/authors")

@app.route("/authors", methods=['GET', 'POST'])
def new_author():
    if request.method == 'GET':
        return render_template('authors.html', all_authors = Author.get_all())
    else:
        Author.create(request.form)
        return redirect("/")

@app.route("/authors/<id>", methods=['GET', 'POST'])
def author_favorite(id):
    data = {"id": id}
    if request.method == 'GET':
        authors = Author.get_favorite_books(data)
        favorite_books = []
        for book in authors.favorite_books:
            favorite_books.append(book.title)

        books = Book.get_all()
        free_books = []
        for book in books:
            if book.title not in favorite_books:
                free_books.append(book)
        
        return render_template('show_authors.html', one_author = Author.get_one(data), authors = authors, books = free_books)
    else:
        Author.add_favorite(request.form)
        return redirect(f"/authors/{id}")