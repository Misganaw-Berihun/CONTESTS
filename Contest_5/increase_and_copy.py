from collections import deque
from math import sqrt,floor
def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        
        a = sqrt(n)
        cnt = int(a) - 1

        if (a - int(a)) == 0.0:
            cnt += int(a)
        else:
            cnt += int(a) + 1

        print(int(cnt))

main()



        