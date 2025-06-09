from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class CalculatorThree:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    """
    * N numbers are sent;
    * Process 1: If the variance between N number is less than N numbers multiplied, a success information is shown to the user,
    * otherwise, a failure information is shown.
    * Tip: For the Variance calculation, use the method "var" from Numpy.
    """

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        data = self.__validate_body(body)

        variance = self.__calculate_variance(data)
        multiplication = self.__calculate_multiplication(data)

        self.__verify_result(variance, multiplication)

        formatted_response = self.__format_response(variance)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Body format is not correct!")

        data = body["numbers"]
        return data

    def __calculate_variance(self, data: List[float]) -> float:
        variance = self.__driver_handler.variance(data)

        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1

        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Process failure: Variance lesser than Multiplication")

    def __format_response(self, variance: float) -> Dict:
        return {"data": {"Calculator": 3, "result": variance, "success": True}}
