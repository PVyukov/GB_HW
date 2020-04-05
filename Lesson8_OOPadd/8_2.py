"""
2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""
# print(8 / 0)


class DivByZero(Exception):
    def __init__(self, error):
        self.error = error


def division(a, b):
    try:
        if b == 0:
            raise DivByZero('Wrong the second number!! Division by zero!!')
    except DivByZero as err:
        print(err)
    else:
        return a / b


while True:
    a, b = [int(i) for i in input('Enter two numbers: ').split()]
    print(f'a/b = {division(a, b)}')