def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        k = 0
        n >>= 1
        while n:
            n >>= 1
            k += 1
        print(2 ** k - 1)
main() 