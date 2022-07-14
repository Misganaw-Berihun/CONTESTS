from collections import defaultdict

def main():
    t = int(input())
    memo = defaultdict(list)
    memo[0] = [1 for i in range(18)]
    memo[-1] = [0 for i in range(18)]
    for i in range(1, 200001):
        temp = [0 for k in range(18)]
        for j in range(18):
            if i & (1 << j) == 0:
                temp[18 - j - 1] = memo[i - 1][18 - j - 1] + 1
            else:
                temp[18 -j - 1] = memo[i - 1][18 - j - 1]
        memo[i] = temp
    for i in range(t):
        l, r = map(int, input().split())
        minn = float('inf')
        for i in range(18):
            minn = min(memo[r][i] - memo[l - 1][i] , minn)
        print(minn)
main()
