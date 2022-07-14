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
    for j in range(1,n + 1):
        if j in visited:
            continue
        queue = deque()
        queue.append(j)
        visited.add(j)
        min_cost = float('inf')
        while queue:
            k = len(queue)

            for l in range(k):
                cur = queue.popleft()
                min_cost = min(min_cost, golds[cur - 1])
                for val in adjList[cur]:
                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
        ans += min_cost
    print(ans)
main()