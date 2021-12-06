from flask import Flask, request, render_template, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_item, get_items, save_item, add_item, delete_item
from todo_app.utils import simple_validation

app = Flask(__name__)
app.config.from_object(Config())

# Route for the index page
# Display the to do items on the index page - retrieving them from the session. Sort Alphabetically.

@app.route('/')
def index():
    error = request.args.get("error") or False
    items = get_items()

    items = sorted(items, key=lambda item: item["status"])

    return render_template("index.html", items=items, error=error)

#End of Index

#Route for the Add To Do POST request
#Get and validate items from the form, if there's an error, return to the index page with an error
#displayed, otherwise add the item to the session, and return to the index page.

@app.route("/addtodo", methods = ["POST"])
def AddToDo():
    title = request.form.get("todoItem")
    error = simple_validation(title)

    if(error):
        return redirect(url_for("index", error=error))
    else:
        add_item(title)

    return redirect(url_for("index"))

#End of AddToDo

#Route for UpdateToDo
#Update a to do item, change the status, or title in the form. Validation is done on the post,
# for the get, the existing item populates the form, and updates can be made.

@app.route("/updateToDo/<id>", methods=["GET"])
def UpdateToDo(id):
    item = get_item(id)
    return render_template("updateToDo.html", item=item)


@app.route("/updateToDo/<id>", methods=["POST"])
def UpdateToDoPost(id):
    item = get_item(id)
    title = request.form.get("title")
    status = request.form.get("status")

    error = simple_validation(title, status)
    
    if error:
        return render_template("updateToDo.html", item=item)

    item["title"] = title
    item["status"] = status
    save_item(item)
    return redirect(url_for("index"))


#End of UpdateToDo

#Route for DeleteToDo
#this request removes an item from the session, and then redirects to the homepage.

@app.route("/deleteToDo/<id>")
def DeleteToDo(id):

    delete_item(id)

    return redirect(url_for("index"))

#End of DeleteToDo

#EOF