from flask import Blueprint, jsonify, request
from src.main.factories.calculator_one_factory import calculator_one_factory
from src.main.factories.calculator_two_factory import calculator_two_factory
from src.main.factories.calculator_three_factory import calculator_three_factory

from src.errors.error_controller import handle_errors


calculator_routes_blueprint = Blueprint("calculator_routes", __name__)


@calculator_routes_blueprint.route("/calculator/1", methods=["POST"])
def calculator_one():
    try:

        calculator = calculator_one_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calculator_routes_blueprint.route("/calculator/2", methods=["POST"])
def calculator_two():
    try:
        calculator = calculator_two_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calculator_routes_blueprint.route("/calculator/3", methods=["POST"])
def calculator_three():
    try:
        calculator = calculator_three_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]
