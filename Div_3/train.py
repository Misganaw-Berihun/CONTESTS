for i in range(int(input())):
	input()
	n, k = map(int, input().split())
	nums = list(map(int, input().split()))
	start_dict = {}
	end_dict = {}
	for idx, val in enumerate(nums):
		if val not in start_dict:
			start_dict[val] = idx
		end_dict[val] = idx

	for x in range(k):
		a, b = map(int, input().split())

		if a in start_dict and b in end_dict and start_dict[a] < end_dict[b]:
			print("YES")
		else:
			print("NO")



        
		

		
