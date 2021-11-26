from flask import Flask, request, render_template, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_item, get_items, save_item, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    error = request.args.get("error") or False
    items = get_items()
    return render_template("index.html", items=items, error=error)

@app.route("/addtodo", methods = ["POST"])
def AddToDo():
    title = request.form.get("todoItem")
    error = False
    if not title or not title.strip():
        error = True

    if(error):
        return redirect(url_for("index", error=error))
    else:
        add_item(title)

    return redirect(url_for("index"),)