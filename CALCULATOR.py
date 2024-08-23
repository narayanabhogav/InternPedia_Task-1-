def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Simple Calculator!")
    operations = {
        1: ("Addition", add),
        2: ("Subtraction", subtract),
        3: ("Multiplication", multiply),
        4: ("Division", divide),
        5: ("Exit", None)
    }

    while True:
        print("\nSelect operation:")
        for key in sorted(operations.keys()):
            print(f"{key}. {operations[key][0]}")

        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice == 5:
                print("Thank you for using the calculator.")
                break
            elif choice in operations:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = operations[choice][1](num1, num2)
                print(f"The result is: {result}")
            else:
                print("Invalid input! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

calculator()
