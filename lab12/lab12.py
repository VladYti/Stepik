import numpy as np 

def DFT(x: np.ndarray) -> np.ndarray:
    n = x.shape[0]
    
    def pol(x: np.ndarray, eps: np.complex) -> np.float64:
        return np.sum(a * eps ** k for k, a in enumerate(x))

    result = np.array(([pol(x, 
                        np.cos(2 * np.pi * k / n) \
                        + 1j * np.sin(2 * np.pi * k / n)) for k in range(n)]), 
                        dtype=np.complex)
    
    return result

def FFT(x: np.ndarray) -> np.ndarray:
    n = x.shape[0]
    
    if n <= 4:
        return DFT(x)
    x_even = FFT(x[::2])
    x_odd = FFT(x[1::2])
    w = np.cos(2 * np.pi * np.arange(n) / n) + 1j * np.sin(2 * np.pi * np.arange(n) / n)
    return np.concatenate((x_even + w[:n // 2] * x_odd,
                           x_even + w[n // 2:] * x_odd))

def main():
    input_str = input()
    coeffs = np.array((input_str.split(' ')), dtype=np.float64)
    n = coeffs.shape[0]
    W = FFT(coeffs)
    
    # W = np.round(W, 5)
    # print(' '.join(f'{x.real},{x.imag}' for x in W))
    # print(W)
    # result = [polynomial(coeffs, np.cos(2 * np.pi * k / n) \
    #                              + 1j * np.sin(2 * np.pi * k / n)) for k in range(n)]

    # res = np.array(result, dtype=np.complex)
    # print(res)
    # print(W)
    # print(np.isclose(W, res))
    # print(np.where(W, res, np.isclose(W, res) == False))
    
    print(' '.join(f'{x.real},{x.imag}' for x in W))
   
    
    return 0
    
    
if __name__ == '__main__':
    main()