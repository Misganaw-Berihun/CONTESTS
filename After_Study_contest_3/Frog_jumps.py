def main():
    t = int(input())
    for i in range(t):
        s = input()
        j = len(s)
        ans = 0
        for k in range(len(s) - 1, -1, -1):
            if s[k] == 'R':
                ans = max(ans, j - k)
                j = k
        ans = max(ans, j + 1)
        print(ans)
main()
