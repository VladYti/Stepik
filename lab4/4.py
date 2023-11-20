from functools import reduce
import numpy as np 

def triv_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.matmul(a, b)%9
    
def strassen_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    deg = a.shape[0]
    
    if deg <= 2:
        return triv_mul(a, b)

    ma = a.copy()
    mb = b.copy()
    
    upper_half_ma = np.hsplit(np.vsplit(ma, 2)[0], 2)
    lower_half_ma = np.hsplit(np.vsplit(ma, 2)[1], 2)

    A11 = upper_half_ma[0]
    A12 = upper_half_ma[1]
    A21 = lower_half_ma[0]
    A22 = lower_half_ma[1]
    
    upper_half_mb = np.hsplit(np.vsplit(mb, 2)[0], 2)
    lower_half_mb = np.hsplit(np.vsplit(mb, 2)[1], 2)

    B11 = upper_half_mb[0]
    B12 = upper_half_mb[1]
    B21 = lower_half_mb[0]
    B22 = lower_half_mb[1]
    
    
    D = strassen_mul(A11+A22, B11+B22)
    D1 = strassen_mul(A12-A22, B21+B22)
    D2 = strassen_mul(A21-A11, B11+B12)
    
    H1 = strassen_mul(A11+A12, B22)
    H2 = strassen_mul(A21+A22, B11)
    
    V1 = strassen_mul(A22, B21-B11)
    V2 = strassen_mul(A11, B12-B22)
    
    
    C11 = D + D1 + V1 - H1
    C12 = V2 + H1
    C21 = V1 + H2
    C22 = D + D2 + V2 - H2
    
    C = np.vstack([np.hstack([C11, C12]), np.hstack([C21, C22])])
    
    return C
    
    
def main():
    new_l = []
    new_l.append(list(map(int, input().split(' '))))
    
    deg = len(new_l[0])

    for i in range(deg-1):
        new_l.append(list(map(int, input().split(' '))))
    
    matrix_A = np.array(new_l)
    
    if deg == 1:
        print(matrix_A[0][0]%9)
        return 0
    
    if deg == 2:
        print(triv_mul(matrix_A, matrix_A))
        return 0
    
    # print(deg)
    deg_list = list(map(int, str(bin(deg))[2::][::-1]))
    upper_bound_2 = 2**(len(deg_list))
    lower_bound_2 = 2**(len(deg_list)-1)
    
    if deg != upper_bound_2 and deg != lower_bound_2:
        service_A = np.eye(upper_bound_2)
        service_A[:deg, :deg] = matrix_A
        matrix_A = service_A.copy()
    
    degrees_A = []
    
    if deg_list[0] == 1:
        degrees_A.append(matrix_A)

    serv_res = matrix_A.copy()
    for i in range(len(deg_list)-1):
        serv_res = strassen_mul(serv_res, serv_res)
        
        if deg_list[i+1] == 1:
            degrees_A.append(serv_res)

    res = reduce(strassen_mul, degrees_A)
    res = res[:deg, :deg]
    res = res.astype(int)%9
    for row in res:
        for num in row:
            print(num, end=' ')
        print()
    
    return 0

if __name__ == '__main__':
    main()