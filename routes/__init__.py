from flask_cors import cross_origin
from flask import request

import classes.Accrual
from app import app
from classes.DevScript import DevScript
from classes.EndpointFactory import EndpointFactory
from classes.Accrual import Accrual


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
