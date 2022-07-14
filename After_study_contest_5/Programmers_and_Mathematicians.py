from itertools import combinations
import math
def nCr(n, r):
    f = math.factorial
    return f(n) // (f(n - r) * f(r))
def main():
    t = int(input())
    for i in range(t):
        ans = 0
        a, b = map(int, input().split())
        total = a + b
        ans = nCr(total, 4) - nCr(a, 4) - nCr(b, 4)
        print(ans)
main()
        


    
