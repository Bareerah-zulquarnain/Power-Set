def total_flips(number1, number2):
    """
    Calculate the number of bit flips required to convert number1 to number2.
    """
    flips = 0
    while number1 > 0 or number2 > 0:
        if number1 % 2 != number2 % 2:
            flips += 1
        number1 = number1 // 2
        number2 = number2 // 2
    return flips

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(total_flips(number1, number2))