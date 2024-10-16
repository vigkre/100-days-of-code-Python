"""Calculator Application"""
from art import logo

print(logo)


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(number):
    """Calculate"""
    for symbol, _ in operations.items():
        print(symbol)
    operand = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    output = operations[operand](number, next_number)
    print(f"{number} {operand} {next_number} = {output}")
    return output


def calculator():
    """ Recursively calculates."""
    first_number = float(input("What's the first number?: "))
    continue_calculating = True
    while continue_calculating:
        result = calculate(first_number)
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new "
                                f"calculation: ").lower()
        if should_continue == "y":
            first_number = result
        elif should_continue == "n":
            continue_calculating = False
            print("\n" * 10)
            print(logo)
            calculator()


calculator()
