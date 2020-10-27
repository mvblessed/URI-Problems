import sys
sys.setrecursionlimit(10**6) 

N = int(input())

def main(N):

    r = int(newBin(1, 0) + newBin(N, 2) + newBin(N, 4)) // This formula was taken from http://blogimages.bloggen.be/gnomon/attach/218796.pdf
    print(r)
    
# Factorial function
def factorial(N):
    return 1 if N < 2 else N * factorial(N - 1)
    
# Newton's Binomial function
def newBin(N, K):
    return factorial(N) / (factorial(N - K) * factorial(K))


main(N)

