from math import floor
def solve():
    n, k = map(int, input().split())
    coins = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(-1, n):
        now = sum
        for j in range(i + 1, min(n, i + 32)):
            copy = coins[j]
            copy >>= (j - i)
            now += copy
        ans = max(ans, now)
        if i + 1 != n:
            sum += coins[i + 1] - k
    print(ans)
    
def main():
    t = int(input())
    for i in range(t):
        solve()
        
main()
