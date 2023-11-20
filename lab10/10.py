import numpy as np


def my_func(s_arr, clauses, m, n) -> list:
    for value in s_arr.T:
        count = 0
        for clause in clauses:
            bool_value = False
            for i in range(n):
                if int(clause[i]) > 0:
                    bool_value = bool_value or bool(value[abs(int(clause[i])) - 1])
                else:
                    bool_value = bool_value or not bool(value[abs(int(clause[i])) - 1])
            # print(f'for value {value} clause {clause} is {bool_value}')
            if bool_value:
                count += 1
        if count >= (7 / 8) * m:
            return list(value)


def main():
    n, m = map(int, input().split(' '))
    clauses = []
    for _ in range(m):
        clauses.append(input().split(' '))

    k = int(np.ceil(np.log2(n)))

    k_arr = np.zeros((2 ** k, k + 1), dtype=int)
    k_arr[:, 0] = 1
    service_arr = [list(map(int, list(str(bin(i))[2:].zfill(k)))) for i in range(k_arr.shape[0])]
    service_arr = np.array(service_arr)
    k_arr[:, 1:] = service_arr

    alpha_arr = [list(map(int, list(str(bin(i))[2:].zfill(k + 1)))) for i in range(2 ** (k + 1))]
    alpha_arr = np.array(alpha_arr)
    # print(alpha_arr)
    # print(k_arr)

    s_arr = np.zeros((n, 2 ** (k + 1)), dtype=int)
    for i in range(n):
        for j in range(2 ** (k + 1)):
            s_arr[i, j] = np.dot(k_arr[i], alpha_arr[j]) % 2

    # print()
    # print(s_arr)
    # print(s_arr.T)

    res = my_func(s_arr, clauses, m, n)
    # print(res)

    print(''.join(str(i) for i in res))

    return 0


if __name__ == '__main__':
    main()
