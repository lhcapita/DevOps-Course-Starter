from flask import Flask, request, render_template, redirect, url_for

from todo_app.utils import simple_validation
from todo_app.data.IndexViewModel import ViewModel

from todo_app.data.db_items import DbHandler

from todo_app.data.User import User

from flask_login import LoginManager, login_required, login_user, current_user

import requests
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = "b2b2da62561829515e83"
        return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}")

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)
    #app.config.from_object(Config())

    @app.route('/login/callback/')
    def login_callback():
        oauth_code = request.args.get("code")
        access_token = get_access_token(oauth_code)
        id = get_user_info(access_token)
        user = User(id)
        login_user(user)
        return redirect(url_for("index"))

    def get_access_token(code):
        url = "https://github.com/login/oauth/access_token"
        headers = {
            "Accept": "application/json"
        }
        data = {
            "client_id": os.environ.get("GITHUB_CLIENT_ID"),
            "client_secret": os.environ.get("GITHUB_CLIENT_SECRET"),
            "code": code
        }
        req = requests.post(url, data=data, headers=headers)
        access_token = req.json()["access_token"]
        return access_token

    def get_user_info(access_token):
        url = "https://api.github.com/user"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        req = requests.get(url, headers=headers)
        id = req.json()["id"]
        return id

    def check_user_permissions(id):
        if id == "94121182":
            return "writer"
        return "reader"

    @app.route('/')
    @login_required
    def index():
        error = request.args.get("error") or False

        db = DbHandler()
        items = db.GetItems()

        items = sorted(items, key=lambda item: item.status)
        
        lists = db.GetLists()


        view_model = ViewModel(items, lists, error, check_user_permissions(current_user.id))

        return render_template("index.html", view_model=view_model)

    @app.route("/addtodo", methods = ["POST"])
    @login_required
    def AddToDo():
        if check_user_permissions(current_user.id) == "reader":
            return redirect(url_for("index"))
        
        title = request.form.get("todoItem")
        desc = request.form.get("desc")
        due = request.form.get("date-due")

        error = simple_validation(title)

        if(error):
            return redirect(url_for("index", error=error))
        else:
            db = DbHandler()
            db.AddItem(title, desc, due)

        return redirect(url_for("index"))

    @app.route("/updateToDo/<id>", methods=["GET"])
    @login_required
    def UpdateToDo(id):
        if check_user_permissions(current_user.id) == "reader":
            return redirect(url_for("index"))

        db = DbHandler()
        item = db.GetItem(id)
        lists = db.GetLists()
        due = None
        if(item.due != None):
            due = item.due.strftime("%m/%d/%Y")
        return render_template("updateToDo.html", item=item, statuses = lists, due=due)

    @app.route("/updateToDo/<id>", methods=["POST"])
    @login_required
    def UpdateToDoPost(id):
        if check_user_permissions(current_user.id) == "reader":
            return redirect(url_for("index"))

        db = DbHandler()
        item = db.GetItem(id)
        title = request.form.get("title")
        status = request.form.get("status")
        desc = request.form.get("desc")
        due = request.form.get("date-due")

        error = simple_validation(title, status)

        if error:
            #trello_lists = get_trello_lists()
            lists = db.GetLists()
            return render_template("updateToDo.html", item=item, statuses = lists, due=item.due.strftime("%m/%d/%Y"))

        item.name = title
        item.status = status
        item.desc = desc
        item.due = due
        db.UpdateItem(item)
        return redirect(url_for("index"))

    @app.route("/deleteToDo/<id>")
    @login_required
    def DeleteToDo(id):  
        if check_user_permissions(current_user.id) == "reader":
            return redirect(url_for("index"))

        db = DbHandler()
        db.DeleteItem(id)

        return redirect(url_for("index"))

    return app

create_app()