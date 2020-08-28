import timeit
from random import random
import numpy as np
import matplotlib.pyplot as plt


def func1(a):
    a.sort(key=lambda x: x[1])


def func2(a):
    from operator import itemgetter
    a.sort(key=itemgetter(1))


def main():
    n_repeat = 10
    n = 10**6
    a = [[random(), random(), random()] for i in range(n)]
    res1 = timeit.repeat(lambda: func1(a), repeat=n_repeat, number=1)
    res1 = np.array(res1) * 10**3
    res2 = timeit.repeat(lambda: func2(a), repeat=n_repeat, number=1)
    res2 = np.array(res2) * 10**3

    print(np.mean(res1), np.std(res1))
    print(np.mean(res2), np.std(res2))

    # Example data
    y_pos = np.arange(2)
    performance = [np.mean(res1), np.mean(res2)]
    error = [np.std(res1), np.std(res2)]

    # plot
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(5, 7))

    ax.barh(y_pos,
            performance,
            xerr=error,
            align='center',
            height=0.3,
            color=['#41aac7', 'red'])
    ax.text(np.mean(res1) / 2,
            0,
            f'{int(np.mean(res1))}ms',
            fontsize=16,
            ha='center',
            va='center',
            color='black')
    ax.text(np.mean(res2) / 2,
            1,
            f'{int(np.mean(res2))}ms',
            fontsize=16,
            ha='center',
            va='center',
            color='black',
            weight='bold')

    ax.grid(axis='y')
    ax.set_ylim(-0.5, 1.5)
    ax.set_axisbelow(True)
    ax.tick_params(axis='x', labelsize=14)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_yticks(y_pos)
    # ax.set_yticklabels(['', '', ''])
    ax.yaxis.set_ticklabels([])
    # ax.yaxis.set_ticks_position('none')
    ax.set_xlabel('time[ms]')

    plt.grid()
    plt.tight_layout()
    plt.savefig('sort.png', dpi=200)
    plt.show()


if __name__ == '__main__':
    main()
