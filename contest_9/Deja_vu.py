def main():
    t = int(input())
    for i in range(t):
        s = input()
        not_a = False
        if s[0] == 'a':
            i , j = 1, len(s) - 1
            while i <= j and s[i] == s[j]:
                if s[i] != 'a' or s[j] != 'a':
                    not_a = True
                i += 1
                j -= 1
        
            if not not_a and i >= j:
                print('NO')
                continue
            elif j <= i:
                print("YES")
                print("a" + s)
                continue
        print("YES")
        print(s + "a")
main()

