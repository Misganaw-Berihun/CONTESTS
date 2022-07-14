from collections import defaultdict, deque

n = int(input())
adjList = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

q = int(input())
for i in range(q):
    k = int(input())
    p = list(map(int,input().split()))
    visited = set(p)
    seen = set()


    queue = deque()
    queue.append(p[0])
    seen.add(p[0])

    while queue:
        cur = queue.popleft()
        if cur in visited:
            visited.remove(cur)
        for nei in adjList[cur]:
            if nei not in seen:
                queue.append(nei)
                seen.add(nei)
                
    if len(visited) != 0:
        print("NO")
    else:
        print("YES")