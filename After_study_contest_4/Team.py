def main():
    n = int(input())
    ans = 0
    for i in range(n):
        views = input()
        if views.count('1') >= 2:
            ans += 1
    print(ans)
main()
