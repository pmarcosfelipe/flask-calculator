from flask import Blueprint, jsonify, request
from src.calculators.calculator_one import CalculatorOne

calculator_routes_blueprint = Blueprint("calculator_routes", __name__)


@calculator_routes_blueprint.route("/calculator/1", methods=["POST"])
def calculator_one():
    calculator = CalculatorOne()
    response = calculator.calculate(request)

    return jsonify(response), 200
