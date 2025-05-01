def fibonacci():

    n = int(input("Enter max output1: "))

    a, b = 0, 1
    
    print("Fibonacci sequence:")
    
    # Print first term
    print(a, end=" ")
    
    # Print remaining terms
    for i in range(1, n):
        print(b, end=" ")
        a, b = b, a + b

# Call the function
fibonacci()