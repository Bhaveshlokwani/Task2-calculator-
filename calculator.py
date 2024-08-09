def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))

    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to input the operation choice
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    # Perform the chosen operation and display the result
    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "/"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid choice. Please try again.")
        return

    print(f"The result of {num1} {operation} {num2} is: {result}")

# Run the calculator
calculator()
