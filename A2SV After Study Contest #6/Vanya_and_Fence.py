def main():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))
    tot_width = 0
    for height in heights:
        if height > h:
            tot_width += 2
        else:
            tot_width += 1
    print(tot_width)
main()