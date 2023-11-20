import numpy as np

SQUARES_LIST = set()


def hi(x: int) -> int:
    if x in SQUARES_LIST:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def main():
    n = int(input())
    p = n - 1
    squares = [i**2 for i in range(1, p)]

    for item in squares:
        SQUARES_LIST.add(item % p)

    m1 = np.ones((n, n), dtype=int)
    for i in range(1, n):
        for j in range(1, n):
            m1[i, j] = hi((i-j) % p)
        m1[i, i] = -1

    m2 = -1 * m1
    res = np.concatenate((m1, m2), axis=0)
    res = np.where(res == -1, 0, res)
    # print(res)

    for item in res:
        print(''.join(str(i) for i in item))
    return 0


if __name__ == '__main__':
    main()
