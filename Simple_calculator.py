def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation ")

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

        else:
            print("Error division by zero  is undefined")

    else:
        print("Invalid operation.  please choose from +,-,* and /")

calculator()

    
