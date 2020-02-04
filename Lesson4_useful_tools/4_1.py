import sys as cmd

if __name__ == '__main__':
    try:
        works = int(cmd.argv[1])
        rate = int(cmd.argv[2])
        premium = int(cmd.argv[3])
        salary = (works * rate) + premium
        print('You salary is {}'.format(salary))
    except IndexError:
        print('Error!!Usage: {} "works" "rate" "salary"'.format(cmd.argv[0]))
    except ValueError:
        print('Error!! All arguments should be "int"')

