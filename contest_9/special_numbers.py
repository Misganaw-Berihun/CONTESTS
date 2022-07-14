def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        b = bin(k)
        ans = 0
        pow = 1
        for i in range(len(b) - 1, 1, -1):
            ans += (pow * int(b[i]))
            pow *= n
        print(ans %(10**9 + 7))
main()
        
            