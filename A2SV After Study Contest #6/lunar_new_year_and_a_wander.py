from collections import defaultdict, deque
import heapq
def dfs(start, adjList, visited):
    print(start, end = " ")
    visited.add(start)
    for i in range(len(adjList[start])):
        top = heapq.heappop(adjList[start])
        if top in visited:
            continue
        dfs(top, adjList, visited)

def main():
    n, m = map(int, input().split())
    adjList = defaultdict(list)
    lex_sm = float("inf")
    for i in range(m):
        start, end = map(int, input().split())
        lex_sm = min(start, end, lex_sm)
        heapq.heappush(adjList[start], end)
        heapq.heappush(adjList[end], start)
    dfs(lex_sm, adjList, set())
main()