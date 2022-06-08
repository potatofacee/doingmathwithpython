# finds solution to quadratic formula given a, b, and c

def roots(a, b, c):

    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print(f'x1 = {x1}')
    print(f'x2 = {x2}')

if __name__ == '__main__':

    print('For an equation such that: a*x^2 + b*x + c = 0')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    roots(a, b, c)


