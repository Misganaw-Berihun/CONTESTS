def main():
    n, t = map(int, input().split())
    s = input()
    temp = list(s)
    while t > 0:
        swaped = False
        for i in range(1, len(temp)):
            if swaped:
                swaped = False
                continue
            if temp[i] == 'G' and temp[i - 1] == 'B':
                temp[i], temp[i -1] = temp[i - 1], temp[i]
                swaped = True
        t -= 1
    print(''.join(temp))
main()
    