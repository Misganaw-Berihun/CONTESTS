from collections import Counter
from typing import Counter
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        count = Counter(nums)
        print(count)
main()
