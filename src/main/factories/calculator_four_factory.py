from src.calculators.calculator_four import CalculatorFour
from src.drivers.numpy_handler import NumpyHandler


def calculator_four_factory():
    numpy_handler = NumpyHandler()
    calculator = CalculatorFour(numpy_handler)

    return calculator
