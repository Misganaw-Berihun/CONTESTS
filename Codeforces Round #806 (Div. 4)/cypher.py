def sequence(ins, num):
    if ins == "D":
        if num == 9:
            return 0
        return num + 1
    if ins == 'U':
        if num == 0:
            return 9
        return num - 1

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        for j in range(n):
            b, move = input().split()
            for k in range(int(b)):
                nums[j] = sequence(move[k], nums[j])
        print(*nums, end = " ")

main()
