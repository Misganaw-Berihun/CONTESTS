def main():
    n = int(input())
    nums = list(map(int, input().split()))
    i, j = 0, n - 1
    while i < n - 1 and nums[i + 1] >= nums[i]:
        i += 1
    
    while j >= 1 and nums[j] >= nums[j - 1]:
        j -= 1

    if i == n - 1 and j == 0:
        print("yes")
        print(1,1)
        return

    if j < n - 1  and nums[i] > nums[j + 1]:
        print("no")
        return
    if i >= 1 and nums[j] < nums[i - 1]:
        print("no")
        return

    status = True
    for k in range(i + 1, j + 1):
        if nums[k] > nums[k - 1]:
            status = False
            break
        
    if status:
        print("yes")
        print(i + 1, j + 1)
    else:
        print("no")
main()
