"""
1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def str_to_int(cls, day_month_year):
        return [int(number) for number in day_month_year.split('-')]

    @staticmethod
    def verify(day_month_year):
        output = ''
        error = False
        day, month, year = Data.str_to_int(day_month_year)
        if day < 1 or day > 31:
            output += 'Incorrect day '
            error = True
        if month < 1 or month > 12:
            output += 'Incorrect month '
            error = True
        if year < 1980 or year > 2020:
            output += 'Incorrect year'
            error = True
        if error is True:
            print('Error: ', output)
        else:
            print('Date is correct')


d1 = Data('22-02-1987')
print(Data.str_to_int('22-2-1987'))
print(d1.str_to_int('22-2-1987'))
Data.verify('22-2-1987')
d1.verify('0-13-1970')
