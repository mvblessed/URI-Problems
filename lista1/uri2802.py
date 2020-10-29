import sys
sys.setrecursionlimit(10**6) 

n = int(input())

def main(n):

    # This formula was taken from http://blogimages.bloggen.be/gnomon/attach/218796.pdf
    r = int(biNum(1, 0) + biNum(n, 2) + biNum(n, 4)) 
    print(r)
    
# Factorial function
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
    
# Bionomial number function
def biNum(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


main(n)

