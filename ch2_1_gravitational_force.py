
# draw the gravitational relationsip of two bodies
# F = (G * m1 * m2) / (r ** 2)


import matplotlib.pyplot as plt

# draw graph
def draw_graph(x, y):

    plt.plot(x, y, marker='o')
    plt.xlabel('Distance between bodies')
    plt.ylabel('Force between bodies')
    plt.title('Newton\'s Law of Universal Gravitation')
    plt.show()

def generate_F_r():

    # gen values for R
    r = range(100, 1001, 50)

    G = 6.674 * 10 ** -11
    F = []

    m1 = 0.5
    m2 = 1.5

    for dist in r:
        force = G * m1 * m2 / (dist ** 2)
        F.append(force)

    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()
    
