# Python Calculator
Perform basic arithmetic operations.
![image](https://github.com/user-attachments/assets/c7db79c5-8f87-45f6-8761-693daf32c9c5)

This arithmetic calculator allows the user to enter data for the solution of their respective operations. In its first version it was limited to only 2 data.

## Step by step explanation of an arithmetic calculator in Python
## Step 1
![image](https://github.com/user-attachments/assets/69ee5fb1-bdbd-4cfe-8f6c-bb1637171e41)


"__init__“:It is the constructor of the class that initializes an empty list of numbers to store the numbers entered by the user.
"add_number": Method that adds a number to the list of numbers.
"get_numbers": Method that returns the stored list of numbers.

## Step 2
![image](https://github.com/user-attachments/assets/6281fdbb-749c-4462-b865-49c87543f0b3)

"init__": Constructor that initializes a data object (of the Data class) to access numbers.
"calculate": Abstract method that the child classes will implement to perform arithmetic operations. It is a “skeleton” that the derived classes must overwrite.

## Step 3
![image](https://github.com/user-attachments/assets/201ff2f3-fe7c-4553-b7f3-39425e80ec05)

This class inherits from Operations and implements the method calculate to perform the corresponding operation, likewise for the operations subtract, multiply and divide.

sum: Performs the sum of all numbers.
Subtract: Subtracts the numbers in sequential order.
Multiply: Multiplies all numbers.
Divide: Divide the numbers in sequential order.

Initialize result to 0 and then sum each number in the list.

## Step 4
![image](https://github.com/user-attachments/assets/191c5d73-cd13-43a8-b8b8-bc76ac8dbfc8)

__“init”__: Stores the result of an operation.
“get_result": Returns the stored result.

## Step 5
![image](https://github.com/user-attachments/assets/ac53a84e-f5d2-4c88-af19-179772a49d9a)

"print_result": Prints the result of the operation, a farewell message, and author credits.

## Step 6
![image](https://github.com/user-attachments/assets/a41fbf38-cdae-4391-a814-3f219778dad4)

Initialization: Creates a Data object to store numbers and displays a welcome message.
User Input Loop: Repeatedly asks the user to input numbers. If the user types 'x', the loop stops. If the input is invalid, an error message is displayed.

## Step 7
![image](https://github.com/user-attachments/assets/782ee3ed-fd93-4108-b988-464380912dc0)

Check for Numbers: After exiting the loop, the code checks if any numbers were entered. If no numbers were entered, it ends; otherwise, it prompts for the operation type.

## Step 8 
![image](https://github.com/user-attachments/assets/f244cda6-def7-498d-9b8a-2c428a745dfe)

Operation Selection: Based on the user's input, the code selects the corresponding operation (addition, subtraction, multiplication, or division). If division by zero occurs, an error is handled.

## Step 9
![image](https://github.com/user-attachments/assets/8ec2a68d-0dc2-4617-a568-9760d412b54b)

Result Handling: If the operation is valid, the result is calculated and displayed. If the operation is invalid, or if there's an error (like division by zero), an appropriate message is printed.

This structure provides a clear flow from taking user input to performing calculations and handling errors.

## Operations supported
Addition, subtraction, multiplication, division.

## Technologies
Python 🐍

## Installation
You need to have Python 3.12 installed to run it. You can verify by typing the following command in your terminal:
````bash
  py
```
Clone the repository from the following link:

 https://github.com/jhoncarlosam-dev/calculator

```bash
git clone https://github.com/jhoncarlosam-dev/calculator.git
```

Execute the following command:
```bash
  py Calculator.py
```

# Colaborators
William Steven Sosa Osorio 1151734
Juan Diego Contreras 1152224
Jhon Carlos Acevedo Mendoza 1151661
