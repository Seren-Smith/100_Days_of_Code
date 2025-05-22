"""
SMARTCALC - AN INTELLIGENT PYTHON CALCULATOR
--------------------------------------------
Features:
- Supports all basic arithmetic operations (+, -, *, /)
- Advanced operations: floor division (//), modulus (%), exponentiation (**)
- Comprehensive error handling (invalid inputs, division by zero)
- User-friendly interface with operation validation
- Continuous calculation mode
- Clean, professional output formatting
"""


def display_welcome():
    print("\n" + "=" * 50)
    print("||" + " " * 46 + "||")
    print("||" + " SMART CALCULATOR ".center(46) + "||")
    print("||" + " " * 46 + "||")
    print("=" * 50)
    print("\nInstructions:")
    print("- Enter two numbers")
    print("- Choose from these operations: +, -, *, /, //, %, **")
    print("- Type 'exit' at any time to quit\n")


def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'exit':
            return None
        try:
            return float(value)
        except ValueError:
            print("⚠️ Invalid input! Please enter a number or 'exit'")


def get_operation():
    """Validate and return the selected operation"""
    valid_ops = ['+', '-', '*', '/', '//', '%', '**']
    while True:
        op = input("Select operation (+, -, *, /, //, %, **): ")
        if op.lower() == 'exit':
            return None
        if op in valid_ops:
            return op
        print("⚠️ Invalid operation! Please choose from the available options")


def calculate(num1, num2, op):
    """Perform the calculation with proper error handling"""
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        elif op == '//':
            return num1 // num2
        elif op == '%':
            return num1 % num2
        elif op == '**':
            return num1 ** num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    display_welcome()

    while True:
        # Get user input with validation
        num1 = get_number("\nEnter first number (or 'exit'): ")
        if num1 is None: break

        num2 = get_number("Enter second number (or 'exit'): ")
        if num2 is None: break

        op = get_operation()
        if op is None: break

        # Perform calculation and display result
        result = calculate(num1, num2, op)
        print(f"\n🔹 Result: {num1} {op} {num2} = {result}\n")

        # Prompt for another calculation
        if input("Calculate again? (y/n): ").lower() != 'y':
            print("\nThank you for using SmartCalc!")
            break


if __name__ == "__main__":
    main()
