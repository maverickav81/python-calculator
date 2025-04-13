#python calculator
while True:
    operator = input("Choose the operator: ")
    
    if operator.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    if operator == "+":
        print(f"Result: {a + b}")
    elif operator == "-":
        print(f"Result: {a - b}")
    elif operator == "*":
        print(f"Result: {a * b}")
    elif operator == "/":
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Error: Division by zero!")
    else:
        print(f"{operator} is an invalid operator.")
