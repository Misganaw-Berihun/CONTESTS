def main():
    n = int(input())
    heights = list(map(int, input().split()))
    m = int(input())
    for i in range(m):
        width, height = map(int, input().split())
        print(max(heights[0], heights[width - 1]))
        heights[width - 1] += height
        heights[0] = max(heights[0], heights[width - 1])
main()
