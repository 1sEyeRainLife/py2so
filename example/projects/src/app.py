from flask import Flask
from src.routers.shows import bp


app = Flask(__name__)


@app.route("/")
def home():
    return {
        "msg": "Hello World"
    }

app.register_blueprint(bp)