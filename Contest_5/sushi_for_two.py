def main():
    n = int(input())
    sushi = list(map(int,input().split()))
    
    n = len(sushi)
    i =  k= l = 0
    ans = 0

    while i < len(sushi):
        j = i + 1
        while j < n and sushi[i] == sushi[j]:
            j += 1

        k = i
        l = j

        while k < n and l < n and sushi[k] == sushi[i] and \
                    sushi[l] == sushi[j]:
                k += 1
                l += 1

        ans = max(ans,l - j)
        i = j
    print(ans * 2)

main()

             
