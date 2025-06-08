from flask import Blueprint, jsonify, request
from src.calculators.calculator_one import CalculatorOne
from src.calculators.calculator_two import CalculatorTwo
from src.drivers.numpy_handler import NumpyHandler

calculator_routes_blueprint = Blueprint("calculator_routes", __name__)


@calculator_routes_blueprint.route("/calculator/1", methods=["POST"])
def calculator_one():
    calculator = CalculatorOne()
    response = calculator.calculate(request)

    return jsonify(response), 200


@calculator_routes_blueprint.route("/calculator/2", methods=["POST"])
def calculator_two():
    numpy_handler = NumpyHandler()
    calculator = CalculatorTwo(numpy_handler)
    response = calculator.calculate(request)

    return jsonify(response), 200
