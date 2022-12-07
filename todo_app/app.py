from flask import Flask, request, render_template, redirect, url_for

from todo_app.utils import simple_validation
from todo_app.data.IndexViewModel import ViewModel

from todo_app.data.db_items import DbHandler

from todo_app.data.trello_items import get_trello_lists, get_trello_items, get_trello_item, add_trello_item, save_trello_item, delete_trello_item


def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config())


    @app.route('/')
    def index():
        error = request.args.get("error") or False

        db = DbHandler()
        items = db.GetItems()

        items = sorted(items, key=lambda item: item.status)
        
        lists = db.GetLists()
        print(lists)


        view_model = ViewModel(items, lists, error)

        return render_template("index.html", view_model=view_model)


    @app.route("/addtodo", methods = ["POST"])
    def AddToDo():
        title = request.form.get("todoItem")
        desc = request.form.get("desc")
        due = request.form.get("date-due")

        error = simple_validation(title)

        if(error):
            return redirect(url_for("index", error=error))
        else:
            add_trello_item(title, desc, due)

        return redirect(url_for("index"))

    @app.route("/updateToDo/<id>", methods=["GET"])
    def UpdateToDo(id):
        item = get_trello_item(id)
        trello_lists = get_trello_lists()
        due = None
        if(item.due != None):
            due = item.due.strftime("%m/%d/%Y")
        return render_template("updateToDo.html", item=item, statuses = trello_lists, due=due)


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
            return render_template("updateToDo.html", item=item, statuses = trello_lists, due=item.due.strftime("%m/%d/%Y"))

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

    return app

create_app()