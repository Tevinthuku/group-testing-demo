from flask import Flask

from app.routes.home import simpleblueprint


def createapp():
    app = Flask(__name__)
    app.register_blueprint(simpleblueprint)
    return app
