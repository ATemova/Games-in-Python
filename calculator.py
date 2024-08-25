def simple_calculator():
    print("Simple Calculator")
    print("Options:")
    print("Add")
    print("Subtract")
    print("Multiply")
    print("Divide")
    
    operation = input("Choose an operation (Add/Subtract/Multiply/Divide): ").lower()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error! Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation!")
        return
    
    print(f"The result is: {result}")

simple_calculator()
