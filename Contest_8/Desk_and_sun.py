def main():
    n, m = map(int,input().split())
    chair_loc = [[0 for _ in range(105)] for j in range(105)]
    for i in range(n):
        xi, yi = map(int, input().split())
        chair_loc[xi + 1][yi + 1] += 1
    for i in range(1,len(chair_loc)):
        for j in range(1, len(chair_loc)):
            chair_loc[i][j] = chair_loc[i][j] + chair_loc[i - 1][j] + chair_loc[i][j - 1] - chair_loc[i - 1][j - 1]
    for j in range(m):
        sxi, syi, exi,eyi = map(int, input().split())
        ans = 0
        ans = chair_loc[exi + 1][eyi + 1] - chair_loc[exi + 1][syi] - chair_loc[sxi][eyi + 1] + chair_loc[sxi][syi]
        print(ans)
main()
        

