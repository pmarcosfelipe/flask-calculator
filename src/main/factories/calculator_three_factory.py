from src.calculators.calculator_three import CalculatorThree
from src.drivers.numpy_handler import NumpyHandler


def calculator_three_factory():
    numpy_handler = NumpyHandler()
    calculator = CalculatorThree(numpy_handler)

    return calculator
