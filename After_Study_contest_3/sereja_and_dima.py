def main():
    n = int(input())
    nums = list(map(int, input().split()))
    left, right = 0, len(nums) - 1
    sPoints, dPoints, turn = 0, 0, True
    while left <= right:
        cur_max = 0
        if nums[left] > nums[right]:
            cur_max = nums[left]
            left += 1
        else:
            cur_max = nums[right]
            right -= 1
        if turn:
            sPoints += cur_max
        else:
            dPoints += cur_max
        turn = (not turn)
    print(sPoints,dPoints)
main()
        

