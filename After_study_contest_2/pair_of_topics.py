def binarySearch(arr, left, right, dif):
    while (left < right):
        mid = left + (right - left) // 2
        if (arr[mid][0] - arr[mid][1]) > dif:
            right = mid
        else:
            left = mid + 1
    return left

def main():
    n = int(input())
    teacher = list(map(int, input().split()))
    student = list(map(int, input().split()))
    tea_std = list(zip(teacher, student))
    tea_std.sort(key = lambda a: [a[0] - a[1], a[0]])
    ans = 0
    for i in range(n):
        dif = tea_std[i][0] - tea_std[i][1]
        ret = binarySearch(tea_std, i + 1, n, -dif)
        ans += (n - ret)
    print(ans)
main()
