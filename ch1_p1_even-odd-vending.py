
# this program acts as an even / odd vending machine.
# it identifies if the number is even or odd then prints the subsequent 9 even/odd digits

def even_or_odd(a):

    if a % 2 == 0:
        print('Even.')
    else:
        print('Odd.')

def print_more(a):

    for i in range(1, 10):
        print(a + 2*i)

if __name__ == '__main__':

    try:
        num = float(input('Please input an integer: '))
        if not num.is_integer():
            print(f'Your float, {num}, has been truncated to {int(num)}.')
        num = int(num)
        even_or_odd(num)
        print_more(num)

    except ValueError:
        print('Invalid entry.')




