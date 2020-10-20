
K = int(input())

def main(K):
    lst1 = []
    

    for i in range(K):
        lst1.append(fib(i))



def fib(K):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(K)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
        
        

main(K)
