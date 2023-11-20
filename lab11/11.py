from __future__ import annotations
import copy
from collections import defaultdict
import numpy as np


def circle_points(n: int) -> np.ndarray:
    t = np.pi * 2 / n
    p = np.array([(np.cos(t * i), np.sin(t * i)) for i in range(n)])
    return p * 10 + 10


def find_second_max(x: np.ndarray) -> int:
    # index_array = np.argpartition(x, -2)[-2:]
    index_array = np.argsort(x)  # [::-1]
    second_max_ind = index_array[1]
    return second_max_ind


def get_sorted_permutation(x: np.ndarray | list, max_min=True) -> list[int]:
    index_array = np.argsort(x)[::-1]
    return list(index_array) if max_min else list(index_array)[::-1]


def phi_functional(g1: Graph, g2: Graph) -> float:
    numerator = Graph.count_edges_between_graphs(g1, g2)
    denominator = (g1.v_count+1) * (g2.v_count+1)
    res = (numerator / denominator) * (g1.v_count + g2.v_count)
    return res


class Graph:
    def __init__(self):
        self.v_count = 0
        self.edges = defaultdict(list)

    def add_edge(self, u, w):
        self.edges[u].append(w)
        self.edges[w].append(u)
        self.v_count = max([u, w, self.v_count])

    def from_dict(self, input_dict: dict):
        self.edges = defaultdict(list)
        for key, item in input_dict.items():
            self.edges[key] = item
        self.v_count = len(input_dict.keys())-1

    def get_adj_matrix(self):
        adj_matrix = np.zeros((self.v_count + 1, self.v_count + 1), dtype=int)
        for key, item in self.edges.items():
            for i in item:
                # print(key)
                adj_matrix[key, i] = 1
        return adj_matrix

    def get_laplacian_matrix(self):
        lp_matrix = -1 * self.get_adj_matrix()
        for i in range(lp_matrix.shape[0]):
            lp_matrix[i, i] = -np.sum(lp_matrix[i, :])
        return lp_matrix

    @classmethod
    def create_two_sub_graphs(cls, g: Graph, vertex_indexes: list):
        dict_a = dict()
        dict_v_without_a = copy.deepcopy(g.edges)
        # print(vertex_indexes)
        # print(dict_v_without_a)

        for key in vertex_indexes:
            # print(key)
            dict_a[key] = dict_v_without_a.pop(key)

        graph_a = Graph()
        graph_a.from_dict(dict_a)

        graph_without_a = Graph()
        graph_without_a.from_dict(dict_v_without_a)

        return graph_a, graph_without_a

    @classmethod
    def count_edges_between_graphs(cls, g1: Graph, g2: Graph) -> int:
        count = 0
        for vertex in g1.edges.keys():
            for vertices in g2.edges.values():
                if vertex in vertices:
                    count += 1
        return count


def main():

    edge_count = int(input())
    main_graph = Graph()

    for _ in range(edge_count):
        input_str = tuple(map(int, input().split(' ')))
        main_graph.add_edge(input_str[0], input_str[1])

    mg_v_count = main_graph.v_count
    mg_vert = set(main_graph.edges.keys())
    lp = main_graph.get_laplacian_matrix()
    eig_val, eig_vec = np.linalg.eigh(lp)
    for i, eig in enumerate(eig_val):
        print(f'For eigen value {eig} eigen vector {eig_vec[i, get_sorted_permutation(eig_vec[i])]}', end='\n\n')
        print(get_sorted_permutation(eig_vec[i]))
        print()

    sm_ind = find_second_max(eig_val)
    sm_vec = eig_vec[sm_ind]
    per_ind = get_sorted_permutation(sm_vec)

    sets_a = [per_ind[:i + 1] for i in range(len(per_ind) - 1)]
    # print(sets_a)
    # print(type(sets_a))
    for i, set_a in enumerate(sets_a):
        if len(set_a) >= mg_v_count // 2 + 1:
            service_l = [i for i in set_a]
            sets_a[i] = list(mg_vert - set(service_l))
    # print(sets_a)
    #
    # print(set_a)
    # print(type(set_a))
    # print(sets_a)
    #
    # sub_graph = Graph()
    # sub_graph.from_dict(dict(list(main_graph.edges.items())[i] for i in sets_a[3]))
    #
    # print(main_graph.edges)
    # print(sub_graph.edges)
    # print(type(sub_graph))
    # print(main_graph.edges)
    # print(sets_a[2])
    # graph_a, graph_without_a = Graph.create_two_sub_graphs(main_graph, sets_a[2])
    # print(graph_a.edges)
    # print(graph_without_a.edges)
    # count_edges = Graph.count_edges_between_graphs(graph_a, graph_without_a)
    # print(count_edges)
    #
    # f_value = phi_functional(graph_a, graph_without_a)
    # print(f_value)

    phi_list = []
    for set_a in sets_a:
        graph_a, graph_without_a = Graph.create_two_sub_graphs(main_graph, set_a)
        f_value = phi_functional(graph_a, graph_without_a)
        phi_list.append(f_value)

    phi_min = get_sorted_permutation(phi_list, max_min=False)

    # phi_min = np.where(phi_list == np.array(phi_list).min())
    # print(phi_min)
    # print(get_sorted_permutation(phi_list))

    output_strs = []
    for i, ind in enumerate(phi_min):
        s = ' '.join(str(i) for i in sets_a[ind])
        output_strs.append(s)
        if not (np.isclose(phi_list[ind], phi_list[phi_min[i + 1]])):
            break
        else:
            continue

    ind = 0
    if len(output_strs) > 1:
        min_s = len(output_strs[ind])
        for i, item in enumerate(output_strs):
            if len(item) <= min_s:
                min_s = len(item)
                ind = i

    print(output_strs[ind])

    return 0


if __name__ == '__main__':
    main()
