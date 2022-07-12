from flask_cors import cross_origin
from flask import request

from app import app
from classes.DevScript import DevScript
from classes.EndpointFactory import EndpointFactory


@app.route('/service', methods=['POST'])
@cross_origin()
def main_endpoint():
    request_data = request.get_json() or {}
    return EndpointFactory(request_data).process()


@app.route('/default-data', methods=['GET'])
@cross_origin()
def add_default_data():
    DevScript().add_default_data()
    return True
