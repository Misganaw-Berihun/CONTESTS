from collections import defaultdict

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = ""
        strs = []
        dict = defaultdict(int)
        for i in range(n):
            s = input() 
            strs.append(s)
            dict[s] += 1
        
        for a in range(n):
            status = False
            for b in range(1, len(strs[a])):
                s = strs[a][:b]
                s2 = strs[a][b:]
                if s in dict and s2 in dict:
                        status = True
                        break
            if status:
                ans += "1"
            else:
                ans += "0"
        print(ans)
main()

        

