from collections import defaultdict, deque
def main():
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    adjList = defaultdict(list)
    for i in range(m):
        x, y = map(int, input().split())
        adjList[x].append(y)
        adjList[y].append(x)
    visited = set()
    ans = 0
    def dfs(k):
        nonlocal adjList, visited, golds
        if k not in adjList:
            return golds[k - 1]
        visited.add(k)
        minn = golds[k - 1]
        for f in adjList[k]:
            if f not in visited:
                minn = min(golds[k - 1], dfs(f))
        return minn
                
    for j in range(1, n + 1):
        if j not in visited:
            ans += dfs(j)
    print(ans)
main()
