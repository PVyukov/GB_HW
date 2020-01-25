revenue = int(input('Enter your revenue: '))
cost = int(input("Enter your cost:"))
pribil = revenue - cost

if pribil > 0:
    rental = pribil/revenue
    people = int(input('Enter number of employees: '))
    avrg_pribil = pribil / people
    print(f'выручка больше издержек; рентабильность:{rental}; прибыль на одного человека: {avrg_pribil}')
else:
    print('издержки больше выручки')
