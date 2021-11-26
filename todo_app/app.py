from flask import Flask, request, render_template, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_item, get_items, save_item, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    error = request.args.get("error") or False
    items = get_items()

    items = sorted(items, key=lambda item: item["status"])

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

@app.route("/updateToDo/<id>", methods=["GET", "POST"])
def UpdateToDo(id):
    if request.method == "POST":
        item = get_item(id)
        title = request.form.get("title")
        status = request.form.get("status")

        error = False

        if not title or not title.strip():
            error = True
        if not status or not status.strip():
            error = True
        
        if error:
            return render_template("updateToDo.html", item=item)

        item["title"] = title
        item["status"] = status
        save_item(item)
        return redirect(url_for("index"))

    if request.method == "GET":
        item = get_item(id)
        return render_template("updateToDo.html", item=item)
