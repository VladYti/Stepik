import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



def main():
    n = int(input())

    G = nx.Graph()
    for i in range(n):
        G.add_edge(*map(int, input().split(' ')))

    print(list(G.nodes))
    print(list(G.edges))

    subax1 = plt.subplot()
    nx.draw_circular(G, with_labels=True, font_weight='bold')
    plt.show()

    cut_value, partition = nx.minimum_cut(G)
    reachable, non_reachable = partition

    return 0


if __name__ == '__main__':
    main()
