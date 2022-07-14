for i in range(int(input())):
	s = input()
	visited = set()
	ans = 0
	count = 0
	i = 0
	while i < len(s):
		if s[i] not in visited:
			count += 1
			visited.add(s[i])
		if count != 3:
		    i += 1
		    continue
		
		while i < len(s) and s[i] in visited:
		    i += 1
		    
		ans += 1
		count = 0
		visited = set()
	if count > 0:
	    ans += 1
	print(ans)
