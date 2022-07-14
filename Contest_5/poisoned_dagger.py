def findMinAttack(attacks,h):
    n = len(attacks)
    dif = [0 for i in range(n)]
    for i in range(1,n):
        dif[i - 1] = attacks[i] - attacks[i-1]

    l ,r = 1,h - n + 1

    while l <= r:
        m = l + (r-l)//2
        dif[n-1] = m
        temp = 0

        for i in range(n):
            if dif[i] <= m:
                temp += dif[i]
            else:
                temp += m

        if temp >= h:
            r = m - 1
        else:
            l = m + 1

    return int(l)
       
def main():
    t = int(input())

    for i in range(t):
        n,h = map(int,input().split())

        attacks = list(map(int,input().split()))
        print(findMinAttack(attacks,h))

main()