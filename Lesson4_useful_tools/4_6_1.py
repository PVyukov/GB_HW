from itertools import count
from sys import argv

start_el = int(argv[1])
iterator = count(start_el, 1)

if __name__ == '__main__':
    for i in iterator:
        if i > 20:
            break
        print(i)
