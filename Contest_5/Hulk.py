def main():
    n = int(input())

    i = 1
    feeling = ""

    while i <= n:
        if i % 2 == 1:
            feeling += "I hate "
        else:
            feeling += "I love "

        if i == n:
            feeling += "it"
        else:
            feeling += "that "

        i+=1

    print(feeling)
    
main()

