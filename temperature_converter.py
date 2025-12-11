#!/usr/bin/env python3
"""
Temperature Converter Program
Supports conversions between Celsius, Fahrenheit, and Kelvin
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def display_menu():
    """Display the temperature converter menu"""
    print("\n" + "="*50)
    print("    TEMPERATURE CONVERTER PROGRAM")
    print("="*50)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. View Conversion Formulas")
    print("8. Exit")
    print("="*50)

def show_formulas():
    """Display conversion formulas"""
    print("\n" + "-"*50)
    print("TEMPERATURE CONVERSION FORMULAS:")
    print("-"*50)
    print("°F = (°C × 9/5) + 32")
    print("°C = (°F - 32) × 5/9")
    print("K = °C + 273.15")
    print("°C = K - 273.15")
    print("K = (°F - 32) × 5/9 + 273.15")
    print("°F = (K - 273.15) × 9/5 + 32")
    print("-"*50 + "\n")

def main():
    """Main function to run the temperature converter"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        
        if choice == '8':
            print("Thank you for using the temperature converter. Goodbye!")
            break
        
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                # Get the temperature value
                if choice == '1':
                    temp = float(input("Enter temperature in Celsius: "))
                    result = celsius_to_fahrenheit(temp)
                    print(f"\n{temp}°C = {result:.2f}°F\n")
                
                elif choice == '2':
                    temp = float(input("Enter temperature in Fahrenheit: "))
                    result = fahrenheit_to_celsius(temp)
                    print(f"\n{temp}°F = {result:.2f}°C\n")
                
                elif choice == '3':
                    temp = float(input("Enter temperature in Celsius: "))
                    result = celsius_to_kelvin(temp)
                    print(f"\n{temp}°C = {result:.2f}K\n")
                
                elif choice == '4':
                    temp = float(input("Enter temperature in Kelvin: "))
                    result = kelvin_to_celsius(temp)
                    print(f"\n{temp}K = {result:.2f}°C\n")
                
                elif choice == '5':
                    temp = float(input("Enter temperature in Fahrenheit: "))
                    result = fahrenheit_to_kelvin(temp)
                    print(f"\n{temp}°F = {result:.2f}K\n")
                
                elif choice == '6':
                    temp = float(input("Enter temperature in Kelvin: "))
                    result = kelvin_to_fahrenheit(temp)
                    print(f"\n{temp}K = {result:.2f}°F\n")
            
            except ValueError:
                print("Invalid input! Please enter a valid temperature value.")
        
        elif choice == '7':
            show_formulas()
        
        else:
            print("Invalid choice! Please enter a valid option (1-8).")

if __name__ == "__main__":
    main()
