from matplotlib import pyplot as plt


def graph(fx, fy, calculated_x, calculated_y, real_x, real_y):
    plt.scatter(fx, fy, c='black')

    plt.plot(calculated_x, calculated_y, 'red')
    plt.plot(real_x, real_y, 'lime')

    plt.legend(['węzły', 'wielomian interpolacyjny', 'wykres funkcji f(x)'])
    plt.show()