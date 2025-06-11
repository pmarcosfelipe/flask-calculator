from typing import Dict, List
from pytest import raises
from .calculator_three import CalculatorThree


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 10


class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1000000


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_three = CalculatorThree(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_three.calculate(mock_request)

    assert str(excinfo.value) == "Process failure: Variance lesser than Multiplication"


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_three = CalculatorThree(MockDriverHandler())

    response = calculator_three.calculate(mock_request)
    assert response == {"data": {"Calculator": 3, "result": 1000000, "success": True}}
