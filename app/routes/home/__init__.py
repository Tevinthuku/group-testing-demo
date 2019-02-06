from flask import Blueprint, jsonify, make_response
from app.routes import simpleblueprint


@simpleblueprint.route('/')
def home():
    return make_response(jsonify({
        "data": "Hello world",
        "status": 200
    }), 200)
