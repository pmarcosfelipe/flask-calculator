from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class CalculatorTwo:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    """
    * N numbers are sent;
    * Process 1: All N numbers are multiplied by 11 and raised to the power 0.95;
    * Process 2: The Standard Deviation is calculated of the results and returned the inverse (1 / result);
    * Tip: Use Numpy to calculate the Standard Deviation.
    """

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        print(body)
        data = self.__validate_body(body)
        print(data)

        calculated_data = self.__process_data(data)

        formatted_response = self.__format_response(calculated_data)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Body format is not correct!")

        data = body["numbers"]
        return data

    def __process_data(self, data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.96 for num in data]

        result = self.__driver_handler.standard_deviation(first_process_result)

        return 1 / result

    def __format_response(self, calculated_data: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(calculated_data, 2)}}
