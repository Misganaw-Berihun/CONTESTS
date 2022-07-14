def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        order = [0 for i in range(26)]
        for j in range(n):
            idx = ord(s[j]) - 65
            if order[idx] == 0:
                order[idx] = 1
            order[idx] += 1
        print(sum(order))
main()