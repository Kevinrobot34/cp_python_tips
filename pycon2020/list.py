import timeit
import numpy as np
import matplotlib.pyplot as plt


def func1(n, a):
    for i in range(n):
        a[i]


def func2(n, a):
    for ai in a:
        ai


def func3(n, a):
    for i, ai in enumerate(a):
        ai


def main():
    n_repeat = 10
    n = 10**7
    a = list(range(n))
    res1 = timeit.repeat(lambda: func1(n, a), repeat=n_repeat, number=1)
    res1 = np.array(res1) * 10**3
    res2 = timeit.repeat(lambda: func2(n, a), repeat=n_repeat, number=1)
    res2 = np.array(res2) * 10**3
    res3 = timeit.repeat(lambda: func3(n, a), repeat=n_repeat, number=1)
    res3 = np.array(res3) * 10**3

    print(np.mean(res1), np.std(res1))
    print(np.mean(res2), np.std(res2))
    print(np.mean(res3), np.std(res3))

    # Example data
    y_pos = np.arange(3)
    performance = [np.mean(res1), np.mean(res2), np.mean(res3)]
    error = [np.std(res1), np.std(res2), np.std(res3)]

    # plot
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(5, 7))

    ax.barh(y_pos,
            performance,
            xerr=error,
            align='center',
            height=0.3,
            color=['#41aac7', 'red', '#41aac7'])
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
    ax.text(np.mean(res3) / 2,
            2,
            f'{int(np.mean(res3))}ms',
            fontsize=16,
            ha='center',
            va='center',
            color='black')

    ax.grid(axis='y')
    ax.set_ylim(-0.5, 2.5)
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
    plt.savefig('list.png', dpi=200)
    plt.show()


if __name__ == '__main__':
    main()
