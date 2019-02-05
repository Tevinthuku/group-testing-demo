from flask import Blueprint

simpleblueprint = Blueprint('simpleblueprint', __name__)


@simpleblueprint.route('/')
def home():
    return "Hello world"
