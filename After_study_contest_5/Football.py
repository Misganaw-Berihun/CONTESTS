def main():
    s = input()
    i = 0
    while i < len(s):
        j = i + 1
        c = s[i]
        cnt = 1
        while j < len(s) and s[j] == c:
            j += 1
            i += 1
            cnt += 1
        
        if cnt >= 7:
            print("YES")
            return
        i += 1
    print("NO")
main()
