def main():
    s = input()
    n = len(s)
    mid = (n - 1) // 2
    i = mid
    j = n - 1
    while i >= 0 and s[i] != s[j]:
        i -= 1
    
    k = i
    while i >= 0:
        while i >= 0 and s[i] == s[j]:
            i -= 1
            j -= 1
        j = n - 1
        if i < 0:
            break
        i = k - 1
        k = i
    valid = False
    if k == mid:
        print(s[: n // 3])
        valid = True
    elif k >= 0:
         for o in range(k, -1, -1):
            tmp = s[: o + 1]
            if tmp in s[o + 1: -(o + 1)] and s[-(o + 1):] == tmp:
                print(tmp)
                valid = True
                break
    if not valid:
        print("Just a legend")
main()
