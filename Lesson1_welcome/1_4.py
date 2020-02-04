number = int(input('Enter number:'))
if number // 10:
    maximum = number % 10
    number //= 10
    while number:
        last_digit = number % 10
        if maximum < last_digit:
            maximum = last_digit
        number //= 10
else:
    maximum = number

print(maximum)