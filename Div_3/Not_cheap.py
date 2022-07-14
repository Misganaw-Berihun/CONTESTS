import heapq
for i in range(int(input())):
	w = input()
	p = int(input())
	total = 0
	heap = []
	for j in range(len(w)):
		indices = ord(w[j]) - 96
		total += indices
		heapq.heappush(heap, (-indices, j))
	removed = set()
	while total > p:
		poped = (heapq.heappop(heap))
		total -= (-1 *poped[0])
		removed.add(poped[1])
	ans = ["" for i in range(len(w) - len(removed))]
	p = 0
	for k in range(len(w)):
		if k not in removed:
			ans[p] = w[k]
			p += 1
	print(''.join(ans))
