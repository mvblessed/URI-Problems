import sys
sys.setrecursionlimit(10**6) 

N = int(input())

def main(N):

    r = int(pascal(1, 0) + pascal(N, 2) + pascal(N, 4))
    print(r)
    
def factorial(N):
    return 1 if N < 2 else N * factorial(N - 1)
    
def pascal(N, K):
    return factorial(N) / (factorial(N - K) * factorial(K))
    

main(N)
