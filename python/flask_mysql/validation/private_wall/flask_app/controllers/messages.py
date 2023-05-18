from flask import session, redirect, request, render_template
from flask_app import app
from flask_app.models.message import Message

@app.route("/post_message", methods=["POST"])
def post_message():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "sender_id": request.form["sender_id"], 
        "receiver_id": request.form["receiver_id"], 
        "content": request.form["content"]
    }
    Message.create(data)
    return redirect("/wall")

@app.route("/destroy/message/<int:id>")
def destroy_message(id):
    if "user_id" not in session:
        return redirect("/danger")
    data = {"id": id}
    Message.delete(data)
    return redirect("/wall")

@app.route("/danger")
def show_danger_message():
    ip_address = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
    return render_template("danger.html", ip = ip_address)