def main():
    n = int(input())
    nums = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < len(nums):
        count = 1
        while i < len(nums) - 1 and nums[i + 1] > nums[i]:
            count += 1
            i += 1
        i += 1
        ans = max(count, ans)
    print(ans)
main() 
