# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:08:33 2024

@author: Lenovo
"""

def get_user_choice():
    print("Choose an operation:")
    print("1. Subtraction")
    print("2. Multiplication")
    print("3. Addition")
    print("4. Normal Division")
    print("5. Floor Division")
    print("6. Modulo")
    print("7. Exponentiation")
 
    choice = input("Enter your choice (1-7): ")
    return choice

def get_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print (num1, num2)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def perform_operation(choice, num1, num2):
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = num1 / num2
    elif choice == '5':
        result = num1 // num2
    elif choice == '6':
        result = num1 % num2
    elif choice == '7':
        result = num1 ** num2
    return result

def check_odd_even(result):
    if result % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    while True:
        choice = get_user_choice()
        num1, num2 = get_numbers()
        result = perform_operation(choice, num1, num2)
        odd_even = check_odd_even(result)

        print(f"Numbers: {num1}, {num2}")
        print(f"Result of the operation: {result}")
        print(f"Result is {odd_even}.")

        repeat = input("Do you want to perform another operation? (yes/no): ")
        if repeat.lower() != 'yes':
            print("Thank you for using the Arithmetic Operations Program.")
