class UnionFind:
	def __init__(self, n):
		self.parent = {i:i for i in range(1, n + 1)}
		self.size = {i: 0 for i in range(1, n + 1)}
		self.numEts = n;
	
	def find(self, u):
		if self.parent[u] == u:
			return u
		self.parent[u] = self.find(self.parent[u])
		return self.parent[u]

	def union(self, a, b):
		a = self.find(a)
		b = self.find(b)
		if a != b:
			if self.size[a] > self.size[b]:
				a, b = b, a
			self.parent[a] = b
			self.size[b] += self.size[a]
			self.numEts -= 1
def main():
	t = int(input())
	for k in range(t):
		n = int(input())
		uf = UnionFind(n)
		for i in range(n):
			a, b = map(int, input().split())
			uf.union(a, b)
		if uf.numEts == 2:
			print("YES")
		else:
			print("NO")
main()