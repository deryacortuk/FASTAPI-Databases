from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/")
def index_flask():
    return "Hello USA"