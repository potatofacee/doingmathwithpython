import matplotlib.pyplot as plt

# todo create list of x axis values
def create_x_values():
    rchg = 0.5
    x = []
    i = -2
    while i <= 2:
        i = round(i, 2)
        x.append(i)
        i += rchg

    return x

# todo make quadatic function
def create_quadratic(x, a, b):
    y_vals = []
    for x in x:
        y = x**2 + a*x + b
        y = round(y,4)
        y_vals.append(y)
    return y_vals

# todo plot x-y
def plot_quad(x, y, a, b):
    plt.plot(x, y)
    plt.title(f'quadratic function of x^2 + ({a}*x + ({b}).')

    if min(y) > max(y):
        lim = abs(min(y))
    else:
        lim = max(y)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.show()




x = create_x_values()
print(x)
print(len(x))
y = create_quadratic(x, 2, 0)

a = -1
b = 0
while a <= 1:
    round(a, 2)
    y = create_quadratic(x, a, b)
    a += 0.1

    #plot_quad(x, y, a, b)

    plt.plot(x, y)


plt.title(f'quadratic function changing b in [ a x^2 + b x + c ]')
plt.xlim(-2, 2)
plt.ylim(-0.5, 2)
plt.show()