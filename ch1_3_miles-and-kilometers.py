'''
converts between miles and kilometers
'''

def print_menu():
    print('1. Convert miles to kilometers.')
    print('2. Convert kilometers to miles.')

def mi_to_km():
    mi = float(input('Enter the number of miles: '))
    km = 1.609 * mi

    print(f'{mi} is equal to {km} kilometers.')

def km_to_mi():
    km = float(input('Enter the number of kilometers: '))
    mi = km / 1.609

    print(f'{km} kilometers is equal to {mi} miles.')

if __name__ == '__main__':
    print_menu()
    choice = int(input('Which conversion would you like to do?: '))
    if choice == 1:
        mi_to_km()

    elif choice == 2:
        km_to_mi()

    else:
        print('Invalid entry.')