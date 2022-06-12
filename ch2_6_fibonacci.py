import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    a, b = 1, 1
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

def ratio(series):
    if len(series) < 3:
        return
    n = []
    rseries = []
    for i in range(1, len(series)):
        a = series[i-1]
        b = series[i]
        ratio = b / a
        rseries.append(ratio)
        n.append(i)
    return n, rseries

if __name__ == '__main__':
    n = 20

    x, y = ratio(fibo(n))
    plt.plot(x, y)
    #plt.ylim(1.615, 1.62)
    plt.show()
    print('hi')