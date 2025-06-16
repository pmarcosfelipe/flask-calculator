from typing import Dict, List
from .calculator_four import CalculatorFour


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 1


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1]})
    calculator_four = CalculatorFour(MockDriverHandler())

    response = calculator_four.calculate(mock_request)
    assert response == {"data": {"Calculator": 4, "result": 1, "success": True}}
