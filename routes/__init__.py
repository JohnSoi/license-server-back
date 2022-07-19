from flask_cors import cross_origin
from flask import request

import classes.Product
from app import app
from classes.DevScript import DevScript
from classes.EndpointFactory import EndpointFactory
from classes.HttpQuery import HttpQueryHelpers


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


@app.route('/products', methods=['GET'])
@cross_origin()
def api_products_and_licenses():
    request_Data = request.get_json()
    return classes.Product.HttpQueryHelpers.json_response(request_Data, success=True)
