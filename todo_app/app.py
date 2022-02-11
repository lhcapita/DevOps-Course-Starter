from flask import Flask, request, render_template, redirect, url_for

from todo_app.flask_config import Config
from todo_app.utils import simple_validation, reformat_due_date

from todo_app.data.trello_items import get_trello_lists, get_trello_items, get_trello_item, add_trello_item, save_trello_item, delete_trello_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    error = request.args.get("error") or False

    items = get_trello_items()

    items = sorted(items, key=lambda item: item.status)

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
    trello_lists = get_trello_lists()
    date_due_text = reformat_due_date(item.due)
    return render_template("updateToDo.html", item=item, statuses = trello_lists, due=date_due_text)


@app.route("/updateToDo/<id>", methods=["POST"])
def UpdateToDoPost(id):
    item = get_trello_item(id)
    title = request.form.get("title")
    status = request.form.get("status")
    desc = request.form.get("desc")
    due = request.form.get("date-due")

    error = simple_validation(title, status)
    
    if error:
        trello_lists = get_trello_lists()
        date_due_text = reformat_due_date(item.due)
        return render_template("updateToDo.html", item=item, statuses = trello_lists, due=date_due_text)

    item.name = title
    item.status = status
    item.desc = desc
    item.due = due
    save_trello_item(item)
    return redirect(url_for("index"))


@app.route("/deleteToDo/<id>")
def DeleteToDo(id):

    delete_trello_item(id)

    return redirect(url_for("index"))
