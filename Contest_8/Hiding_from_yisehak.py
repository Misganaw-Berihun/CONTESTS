def main():
    n = int(input())

    for i in range(n):
        ans = 0
        ai = int(input())
        heights = list(map(int, input().split()))
        maxx = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if maxx > heights[i]:
                ans += 1
            maxx = max(maxx, heights[i])
        print(ans)
main()

