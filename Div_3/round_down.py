import math
t = int(input())
for i in range(t):
	m = input()
	print(int(m) - int(math.pow(10 , len(m) - 1)))

