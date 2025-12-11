#!/usr/bin/env python3
"""
Calculator Program with Addition, Subtraction, Multiplication, and Division
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("       CALCULATOR PROGRAM")
    print("="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("="*40)

def main():
    """Main function to run the calculator"""
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice! Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
