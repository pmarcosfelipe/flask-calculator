from typing import Dict
from pytest import raises
from .calculator_two import CalculatorTwo
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_two = CalculatorTwo(driver)
    formatted_response = calculator_two.calculate(mock_request)
    print()
    print(formatted_response)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.08}}
