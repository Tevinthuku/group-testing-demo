from flask import Blueprint
from app.routes import simpleblueprint


@simpleblueprint.route('/')
def home():
    return "Hello world"
