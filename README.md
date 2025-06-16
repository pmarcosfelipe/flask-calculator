# Flask Calculators API

This project aims to create four calculators using [Flask](https://flask.palletsprojects.com/en/3.0.x/) in order to learn Design Patterns in Python.

## Requirements

- The Calculator One API specification:
  * Number is divided in 3 parts;
  * Process 1: The first part is divided by 4 and the result is summed 7. The result to the power of 2 and multiplied by 0.257;
  * Process 2: The second part to the power of 2.121, divided by 5 and summed 1;
  * Process 3: The 3 results before are summed and return the result.

- The Calculator Two API specification:
  * N numbers are sent;
  * Process 1: All N numbers are multiplied by 11 and raised to the power 0.95;
  * Process 2: The Standard Deviation is calculated of the results and returned the inverse (1 / result);
  * Tip: Use Numpy to calculate the Standard Deviation.

- The Calculator Three API specification:
  * N numbers are sent;
  * Process 1: If the variance between N number is less than N numbers multiplied, a success information is shown to the user, otherwise, a failure information is shown.
  * Tip: For the Variance calculation, use the method "var" from Numpy.

- The Calculator Four API specification:
  * N numbers are sent;
  * Process 1: Calculate the average value between the N numbers.


The main concepts were Unit Test, Integration Test, Facade Pattern, Factory Pattern, Interfaces and Error Handling.

## Run project

```python
python run.py
```

## References

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
