import operator

class Calculator:
    def __init__(self):
        self.numbers = []
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def add_number(self, number):
        self.numbers.append(number)

    def calculate(self, operation):
        try:
            result = self.numbers[0]
            for num in self.numbers[1:]:
                result = self.operations[operation](result, num)
            return result
        except ZeroDivisionError:
            return "Division by zero is not allowed"

# Create a calculator instance
calculator = Calculator()

# Get numbers from the user
while True:
    num = input("Enter a number (or 'finish' to end): ")
    if num == 'finish':
        break
    calculator.add_number(float(num))

# Get the operation from the user
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation
result = calculator.calculate(operation)
print("Result:", result)