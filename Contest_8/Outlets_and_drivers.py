def main():
    t = int(input())
    for i in range(t):
        n, m = map(int,input().split())
        driver_plugs = list(map(int, input().split()))
        driver_plugs.sort(reverse=True)
        j = 0
        while n > 2 and j < len(driver_plugs):
            n -= (driver_plugs[j] - 1)
            j += 1

        if n > 2:
            print(-1)
        else:
            print(j) 
main()