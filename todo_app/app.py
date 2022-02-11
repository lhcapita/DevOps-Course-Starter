from flask import Flask, request, render_template, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import save_item, delete_item
from todo_app.utils import simple_validation

from todo_app.data.trello_items import get_trello_items, get_trello_item, add_trello_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    error = request.args.get("error") or False

    items = get_trello_items()

    items = sorted(items, key=lambda item: item["status"])

    return render_template("index.html", items=items, error=error)


@app.route("/addtodo", methods = ["POST"])
def AddToDo():
    title = request.form.get("todoItem")
    error = simple_validation(title)

    if(error):
        return redirect(url_for("index", error=error))
    else:
        add_trello_item(title)

    return redirect(url_for("index"))

@app.route("/updateToDo/<id>", methods=["GET"])
def UpdateToDo(id):
    item = get_trello_item(id)
    return render_template("updateToDo.html", item=item)


@app.route("/updateToDo/<id>", methods=["POST"])
def UpdateToDoPost(id):
    item = get_trello_item(id)
    title = request.form.get("title")
    status = request.form.get("status")

    error = simple_validation(title, status)
    
    if error:
        return render_template("updateToDo.html", item=item)

    item["title"] = title
    item["status"] = status
    save_item(item)
    return redirect(url_for("index"))


@app.route("/deleteToDo/<id>")
def DeleteToDo(id):

    delete_item(id)

    return redirect(url_for("index"))
