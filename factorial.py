def factorial():
    """
    Calculates the factorial of a number from user input.
    """
    num = int(input("Enter a number: "))
    
    result = 1
    for i in range(1, num + 1):
        result *= i
    
    print(f"The factorial of {num} is {result}")

# Call the function
factorial()