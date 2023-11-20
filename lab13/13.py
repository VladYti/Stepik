from collections import defaultdict
import numpy as np


def circle_points(n: int) -> np.ndarray:
    t = np.pi * 2 / n
    p = np.array([(np.cos(t * i), np.sin(t * i)) for i in range(n)])
    return p * 10 + 10


class Graph:

    def __init__(self):
        self.v_count = 0
        self.edges = defaultdict(list)

    def add_edge(self, u, w):
        self.edges[u].append(w)
        self.edges[w].append(u)
        self.v_count = max([u, w, self.v_count])

    def get_adj_matrix(self):
        adj_matrix = np.zeros((self.v_count + 1, self.v_count + 1), dtype=int)
        for key, item in self.edges.items():
            for i in item:
                # print(key)
                adj_matrix[key, i] = 1
        return adj_matrix

    def find_simple_cycle(self):
        for i in range(3, self.v_count + 1):
            if 0 in self.edges[i]:
                return i

    def get_laplacian_matrix(self):
        lp_matrix = -1 * self.get_adj_matrix()
        for i in range(lp_matrix.shape[0]):
            lp_matrix[i, i] = -np.sum(lp_matrix[i, :])
        return lp_matrix


def main():
    edge_count = int(input())
    main_graph = Graph()

    for _ in range(edge_count):
        input_str = tuple(map(int, input().split(' ')))
        main_graph.add_edge(input_str[0], input_str[1])

    # adj = main_graph.get_adj_matrix()
    sc = main_graph.find_simple_cycle()
    lp = main_graph.get_laplacian_matrix()

    p_out = circle_points(sc)
    Q = lp[sc:, :sc]
    L1 = lp[sc:, sc:]

    L1 = np.linalg.inv(L1)
    p_in_x = -np.matmul(np.matmul(Q, p_out[:, 0]), L1)
    p_in_y = -np.matmul(np.matmul(Q, p_out[:, 1]), L1)

    p_in = np.concatenate((p_in_x, p_in_y), axis=0).reshape(Q.shape[0], 2)
    p = np.concatenate((p_out, p_in), axis=0)

    p = np.round(p, 3)
    for i, item in enumerate(p):
        print(f'{i} {item[0]} {item[1]}')

    return 0


if __name__ == '__main__':
    main()