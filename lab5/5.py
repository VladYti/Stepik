import numpy as np

GLOBAL_PRIME = 71

def bareiss_det(input_matrix: np.ndarray) -> int:
    matrix_m = input_matrix.copy()
    deg = matrix_m.shape[0]
    sign = 1
    prev = 1
    
    for i in range(deg-1):
        if matrix_m[i, i] == 0:
            swapto = next( (j for j in range(i+1, deg) if matrix_m[j, i] != 0), None )
            if swapto is None:
                return 0
            matrix_m[[i, swapto]] = matrix_m[[swapto, i]]
            sign = -sign
        
        for j in range(i+1, deg):
            for k in range(i+1, deg):
                matrix_m[j, k] = ((matrix_m[j, k]*matrix_m[i, i] \
                                - matrix_m[j, i]*matrix_m[i, k]) // prev) % GLOBAL_PRIME
        prev = matrix_m[i, i]
    
    res = (matrix_m[-1, -1] * sign) %GLOBAL_PRIME
    return res #if res >= 0 else res + GLOBAL_PRIME


def main():
    edge_count = int(input())
    edge_list = []
    
    vertices_count = 0
    for _ in range(edge_count):
        input_str = tuple(map(int, input().split(' ')))
        edge_list.append(input_str)
        
        cur_max_vatrtex_count = max(input_str)
        if cur_max_vatrtex_count > vertices_count:
            vertices_count = cur_max_vatrtex_count
    
    adj_matrix = np.zeros((vertices_count+1, vertices_count+1), dtype=int)
    
    for egde in edge_list:
        adj_matrix[egde[0], egde[1]] = 1
    # print(adj_matrix)
    
    computed_matrix = np.random.randint(2, GLOBAL_PRIME-2, size=(vertices_count+1, vertices_count+1), 
                                        dtype=int)
    #computed_matrix = computed_matrix.astype(np.int64)
    # print(computed_matrix)
    
    matrix_c = np.where(adj_matrix == 1, computed_matrix, adj_matrix)
    # print(matrix_c)
    
    det_c = bareiss_det(matrix_c)#%GLOBAL_PRIME
    #det_c = int(np.linalg.det(matrix_c))%GLOBAL_PRIME
    
    if det_c != 0:
        print('yes')
    else:
        print('no')
    
    return 0



if __name__ == '__main__':
    main()



