def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        red = input()
        blue = input()

        nb, nr = 0, 0
        for j in range(n):
            if red[j] > blue[j]:
                nr += 1
            elif red[j] < blue[j]:
                nb += 1
        
        if (nr > nb):
            print("RED")
        elif (nr < nb):
            print("BLUE")
        else:
            print("EQUAL")
main()
