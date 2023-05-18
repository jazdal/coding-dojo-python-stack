from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/recipes/new", methods=['GET', 'POST'])
def new_recipe():
    if request.method == 'GET':
        return render_template("new_recipe.html")
    else:
        if not Recipe.validate_recipe(request.form):
            return redirect("/recipes/new")
        recipe_data = {
            "name": request.form["name"], 
            "description": request.form["description"], 
            "under_30_mins": request.form["under_30_mins"], 
            "instructions": request.form["instructions"], 
            "created_at": request.form["created_at"], 
            "user_id": session["user_id"]
        }
        Recipe.create(recipe_data)
        return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def show_recipe(id):
    recipe_id = {"id": id}
    user_id = {"id": session["user_id"]}
    return render_template("show_recipe.html", recipe = Recipe.get_one(recipe_id), user = User.get_one(user_id))

@app.route("/recipes/edit/<int:id>", methods=['GET', 'POST'])
def edit_recipe(id):
    recipe_id = {"id": id}
    if request.method == 'GET':
        return render_template("edit_recipe.html", recipe = Recipe.get_one(recipe_id))
    else:
        if not Recipe.validate_recipe(request.form):
            return redirect(f"/recipes/edit/{id}")
        data = {
            "id": id, 
            "name": request.form["name"], 
            "description": request.form["description"], 
            "under_30_mins": request.form["under_30_mins"], 
            "instructions": request.form["instructions"], 
            "created_at": request.form["created_at"]
        }
        Recipe.update(data)
        return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete_recipe(id):
    data = {"id": id}
    Recipe.delete(data)
    return redirect("/dashboard")