def binarySearch(prices,coin):
    l = 0
    r = len(prices) - 1

    while l <= r:
        m = l + (r - l) // 2

        if prices[m] > coin:
            r = m - 1
        else:
            l = m + 1
    
    return r

def main():
    n = int(input())
    prices = list(map(int,input().split()))
    num_days = int(input())
    coins = [0 for i in range(num_days)]

    for i in range(num_days):
        coins[i] = int(input())
    
    prices.sort()
    
    for i in range(len(coins)):
        print(binarySearch(prices,coins[i]) + 1)

main()
