from src.calculators.calculator_two import CalculatorTwo
from src.drivers.numpy_handler import NumpyHandler


def calculator_two_factory():
    numpy_handler = NumpyHandler()
    calculator = CalculatorTwo(numpy_handler)

    return calculator
