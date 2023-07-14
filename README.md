# Multiples Checker

# Project Overview
The Multiples Checker project provides a way to check if a given number is a multiple of 5, 7, or both. It includes the following files:

1. main.py: The main module that uses a function from the funcoes module to check if a number is a multiple of 5, 7, or both. It prompts the user to input a natural number and displays the result.
2. funcoes.py: The module containing the multiplo function, which is the core logic of the project. It takes a number as input and returns a corresponding message based on whether the number is a multiple of 5, 7, both, or none.
3. test_funcoes.py: The module containing test cases for the multiplo function. It utilizes the pytest framework to perform automated testing and ensures the correctness of the multiplo function.

# Usage
To use this project, follow the steps below:

1. Clone the repository to your local machine using the following command:
git clone https://github.com/<username>/<repository>.githttps://github.com/JGattringer/TDD_Modules.git

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the main.py file using the Python interpreter:
python main.py

4. Enter a natural number when prompted to check if it is a multiple of 5, 7, or both. The program will display the corresponding message.

# Functionality
The multiplo function in the funcoes.py module is responsible for checking if a given number is a multiple of 5, 7, or both. It uses a match statement to evaluate the input number and returns the appropriate message based on the matching conditions.

The main.py module demonstrates the usage of the multiplo function by taking user input and displaying the result.

The test_funcoes.py module contains test cases for the multiplo function. It utilizes the pytest framework to perform automated testing. Three test functions are defined to check if a number is a multiple of 5, 7, or both, respectively. Each test function asserts that the expected result matches the actual result returned by the multiplo function.

# Running Tests

To run the automated tests for the multiplo function, execute the following command in the project directory:

pytest test_funcoes.py

The tests will be executed, and the results will be displayed in the console.

# Contributing

Contributions to this project are welcome. If you would like to contribute, please follow these steps:

1.  Fork the repository and create a new branch.

2. Make your desired changes or additions.

3. Ensure that the tests pass successfully.

4. Commit your changes with a descriptive commit message.

5. Push your changes to your forked repository.

6. Submit a pull request to the original repository.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

Feel free to modify and use this code for your own purposes. Contributions and suggestions are always welcome!





