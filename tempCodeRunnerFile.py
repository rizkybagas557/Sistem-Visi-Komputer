def odd_even(number):
    input_number = int(input("Enter a number: "))
    number = int(number)  # Ensure the input is an integer
    # Check if the number is even or odd
    if number % 2 == 0:
        print (f'{number} is even')
    else:
        print (f'{number} is odd')
    
    input_number = input("Enter a number: ")
    
    odd_even(input_number)