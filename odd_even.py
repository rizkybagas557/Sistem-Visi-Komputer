def odd_even():
    x = input("Enter a number: ")
    num = int(x)

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

odd_even()
