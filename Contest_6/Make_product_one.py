def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    cost = 0
    neg_cnt = 0
    zero_cnt = 0


    for i in range(n):
        if (nums[i] < 0):
            neg_cnt += 1
            cost += (-1 - (nums[i]))
        elif (nums[i] == 0):
            zero_cnt += 1
        else:
            cost += (nums[i] - 1)

    if neg_cnt % 2 == 1:
        if zero_cnt > 0:
            cost += 1
            zero_cnt -= 1
        else:
            cost += 2
    print(cost + zero_cnt)
main()