class Data:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def get_numbers(self):
        return self.numbers

class Operations:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        pass  # Abstract method

class Sum(Operations):
    def calculate(self):
        result = 0
        for number in self.data.get_numbers():
            result += number
        return result

class Subtract(Operations):
    def calculate(self):
        numbers = self.data.get_numbers()
        if not numbers:
            return "No numbers for Subtractr"
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        return result
    
class Multiplication(Operations):
    def calculate(self):
        result = 1
        for number in self.data.get_numbers():
            result *= number
        return result
    
class Division(Operations):
    def calculate(self):
        if 0 in self.data.get_numbers():
            return "Error: División por cero"
        result = self.data.get_numbers()[0]  # Initialize with the first number
        for i in range(1, len(self.data.get_numbers())):
            result /= self.data.get_numbers()[i]
        return result

class Results:
    def __init__(self, result):
        self.result = result

    def get_result(self):
        return self.result

class PrintResults:
    def print_result(self, result):
        print("The result is:", result)
        print("Goodbye!")
        print("Created by: Jhon Acevedo, Diego Contreras, William Sosa")
        print("UFPS Systems Engineering Students(High Quality Accredited)")
        print("Web Programming by Ing. Jorge Galvis 2024-2")

# def main():
#     data = data()
#     data.agregar_number(5)
#     data.agregar_number(3)
#     data.agregar_number(2)
#     data.agregar_number(2)
#     suma = Suma(data)
#     result_suma = suma.calculate()
#     results = results(result_suma)
#     imprimir = Imprimirresults()
#     imprimir.mostrar_result(results.get_result())

def main():
    data = Data()
    print("-----------------------------------")
    print(" Welcome to UFPS Python Calculator ")
    print("-----------------------------------")

    while True:
        number = input("Enter a number (or 'x' to exit)")
        if number.lower() == 'x':
            break
        try:
            data.add_number(float(number))
        except ValueError:
            print("Invalid entry. Please enter a number")
    if data.get_numbers():
        operation = input("Enter the operation (+, -, *, /): ")
        if operation == "+":
            result = Sum(data).calculate()
        elif operation == "-":
            result = Subtract(data).calculate()
        elif operation == "*":
            result = Multiplication(data).calculate()
        elif operation == "/":
            try:
                result = Division(data).calculate()
            except ZeroDivisionError:
                print("Error: Division by zero")
        else:
            print("Invalid operation")

        if isinstance(result, str): #Check if the result is an error message
            print(result)
        else: 
            PrintResults().print_result(result)
    else:
        print("No se ingresaron números.")
if __name__ == "__main__":
    main()