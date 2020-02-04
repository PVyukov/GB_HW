a = int(input('First result is:'))
b = int(input('Goal is :'))

count = 1
result = a
while result <= b:
    count += 1
    result = result + result*0.1

print(result)
