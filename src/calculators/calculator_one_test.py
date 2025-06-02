from typing import Dict
from pytest import raises
from .calculator_one import CalculatorOne


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_one = CalculatorOne()

    response = calculator_one.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_one = CalculatorOne()

    with raises(Exception) as esceptionInfo:
        calculator_one.calculate(mock_request)

    assert str(esceptionInfo.value) == "Body format is not correct!"
