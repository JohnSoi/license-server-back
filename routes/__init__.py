from flask_cors import cross_origin
from flask import request

from classes.Product import Product
from app import app
from classes.DevScript import DevScript
from classes.EndpointFactory import EndpointFactory
from classes.Accrual import Accrual
from helpers.PhotoLoader import PhotoLoader


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


@app.route('/accruals_create', methods=['POST'])
def api_add_accrual_point():
    request_data = request.get_json() or {}
    return Accrual.api_create_accrual(request_data)


@app.route('/get_products_list', methods=['POST'])
@cross_origin()
def api_products_and_licenses():
    request_data = request.get_json() or {}
    return Product.api_products_and_licenses(request_data)


@app.route('/photo_load', methods=['POST'])
@cross_origin()
def load_photo():
    request_data = request.files
    return PhotoLoader().load(request_data)


@app.route('/get_photo/<file_name>', methods=['GET'])
@cross_origin()
def get_photo(file_name):
    return PhotoLoader().get(file_name)
