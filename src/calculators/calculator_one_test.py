from typing import Dict
from .calculator_one import CalculatorOne


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_one = CalculatorOne()

    response = calculator_one.calculate(mock_request)
    print()
    print(response)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1
