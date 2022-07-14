def binarySearch(new, num):
    left, right = 0, len(new)
    while left < right:
        mid = left + (right - left) // 2

        if new[mid][0] < num:
            left = mid + 1
        else:
            right = mid
    return left
        
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        new = [(i + 1, nums[i]) for i in range(len(nums)) if nums[i] < i + 1]
        new.sort()
        ans = 0
        for i in range(len(new) - 1, 0, -1):
            ans += binarySearch(new, new[i][1])
        print(ans)
main()

