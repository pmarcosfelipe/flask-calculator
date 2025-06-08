from typing import Dict, List
from .calculator_two import CalculatorTwo
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 10


def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_two = CalculatorTwo(driver)
    formatted_response = calculator_two.calculate(mock_request)
    print()
    print(formatted_response)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.08}}


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculator_two = CalculatorTwo(driver)
    formatted_response = calculator_two.calculate(mock_request)
    print()
    print(formatted_response)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.1}}
