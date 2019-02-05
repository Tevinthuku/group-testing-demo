from flask import Flask

from app.routes.home import simpleblueprint as homeblueprint
from app.routes.offices import simpleblueprint as officesblueprint


def createapp():
    app = Flask(__name__)
    app.register_blueprint(homeblueprint)
    app.register_blueprint(officesblueprint)

    return app
