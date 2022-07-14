def dp(i, turn, n, bosses, memo = {}):
    if i >= n:
        return 0

    if turn: #friends Turn
        if i < n - 1:
            return int(bosses[i]) + min(dp(i + 1, False, n, bosses, memo) + \
                    int(bosses[i + 1]) + dp(i + 2, False,n, bosses, memo))
        else:
            return int(bosses[i])
    else:
        return min(dp(i + 1, True, n, bosses, memo), dp(i + 2, True, n, bosses, memo))
def main():
    t = int(input())
    for k in range(t):
        n = int(input())
        bosses = list(map(int, input().split()))
        skip_point = dp(0, True, n, bosses)
        print(skip_point)
main()
     