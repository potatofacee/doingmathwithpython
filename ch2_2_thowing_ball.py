
# plotting the arc of a ball when thrown
# launch velocity
# uy = u * sin(theta)
# ux = u * cos(theta)

# vy = u * sin(theta) - g*t

# Sx = u * cos(theta) * t
# Sy = u * sin(theta) * t - (1/2) * g * t**2

# determine flight time; tpeak = u * sin(theta) / g

# for u of 5 m/s, theta of 45 deg, t = 0.72154

from matplotlib import pyplot as plt
import math

def frange(start, final, increment):

    numbers = []
    while start < final:
        numbers.append(start)
        start += increment

    return numbers

def draw_graph(x, y):

    plt.plot(x, y)
    plt.xlabel('x_coordinate')
    plt.ylabel('y_coordinate')
    plt.title('projectile arc')

def draw_trajectory(u, theta):

    g = 9.81
    theta = math.radians(theta)
    t_flight = 2 * u * math.sin(theta) / g

    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in intervals:
        x.append((u * math.cos(theta) * t))
        y.append((u * math.sin(theta) * t - 0.5 * g * t**2))

    draw_graph(x, y)


if __name__ == '__main__':

    u_list = [20, 40, 60]
    theta = 50

    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['20', '40', '60'])
    plt.show()


'''
    try:
        u = float(input('initial velocity in m/s: '))
        theta = float(input('initial angle from X axis in degrees: '))
    except ValueError:
        print('use numbers, yo')
    else:
        draw_trajectory(u, theta)
        plt.show()
'''