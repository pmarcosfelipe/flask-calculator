from typing import Dict
from flask import request as FlaskRequest


class CalculatorOne:
    """
    * Number is divided in 3 parts;
    * Process 1: The first part is divided by 4 and the result is summed 7. The result to the power of 2 and multiplied by 0.257;
    * Process 2: The second part to the power of 2.121, divided by 5 and summed 1;
    * Process 3: The 3 results before are summed and return the result.
    """

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        data = self.__validate_body(body)
        splitted_number = data / 3

        first_process_result = self.__first_process(splitted_number)
        second_process_result = self.__second_process(splitted_number)

        result = first_process_result + second_process_result + splitted_number

        return self.__format_response(result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Body format is not correct!")

        data = body["number"]
        return data

    def __first_process(self, number: float) -> float:
        first_part = (number / 4) + 7
        second_part = (first_part**2) * 0.257

        return second_part

    def __second_process(self, number: float) -> float:
        return ((number**2.121) / 5) + 1

    def __format_response(self, result: float) -> Dict:
        return {"data": {"Calculator": 1, "result": round(result, 2)}}
