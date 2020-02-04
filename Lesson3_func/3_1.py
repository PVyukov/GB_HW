def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("The second number has not to be a 0 ")


num1, num2 = map(int, (input("Enter two numbers separated by ',':").split(',')))
print(my_div(num1, num2))
