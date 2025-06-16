from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class CalculatorFour:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    """
    * N numbers are sent;
    * Process 1: Calculate the average value between the N numbers.
    """

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        data = self.__validate_body(body)

        average = self.__calculate_average(data)

        formatted_response = self.__format_response(average)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body format is not correct!")

        data = body["numbers"]
        return data

    def __calculate_average(self, data: List[float]) -> float:
        average = self.__driver_handler.average(data)

        return average

    def __format_response(self, average: float) -> Dict:
        return {"data": {"Calculator": 4, "result": average, "success": True}}
