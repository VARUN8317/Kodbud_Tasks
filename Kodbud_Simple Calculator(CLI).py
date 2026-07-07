def calculator():
    print("Simple Calculator")
    print("-----------------")

    # Take input from the user
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Check the operation
    if operation == "+":
        answer = num1 + num2
        print("Answer =", answer)

    elif operation == "-":
        answer = num1 - num2
        print("Answer =", answer)

    elif operation == "*":
        answer = num1 * num2
        print("Answer =", answer)

    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            answer = num1 / num2
            print("Answer =", answer)

    else:
        print("Invalid operation.")

# Call the function
calculator()