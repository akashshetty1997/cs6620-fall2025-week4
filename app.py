"""Simple calculator application."""


def add(number1, number2):
    """Add two numbers."""
    return number1 + number2


def subtract(number1, number2):
    """Subtract two numbers."""
    return number1 - number2


def multiply(number1, number2):
    """Multiply two numbers."""
    return number1 * number2


def divide(number1, number2):
    """Divide two numbers."""
    if number2 == 0:
        raise ValueError("Cannot divide by zero")
    return number1 / number2


def calculate(operation, num1, num2):
    """Perform a calculation based on the requested operation."""
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    return result


if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)

    result1 = calculate("add", 10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calculate("multiply", 7, 3)
    print(f"7 * 3 = {result2}")

    print("Calculator completed successfully!")
