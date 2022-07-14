def compare(grid, i, j):
    g1, g2, g3, g4 = [], [], [], []
    for k in range(j, i - 1, -1):
        g1.append(grid[k][i])
        g4.append(grid[j][k])
    for k in range(j - i + 1):
        g2.append(grid[i][k])
        g3.append(grid[k][j])

    sum = 0
    for k in range(len(g1)):
        d = 0
        d += int(g1[k])
        d += int(g2[k])
        d += int(g3[k])
        d += int(g4[k])
        sum += min(d, 4 - d)
    return sum
def compute(grid, i, j):
    if j <= i:
        return 0
    return compare(grid, i , j) + compute(grid, i + 1, j - 1)

def solve():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    print("Ans:",compute(grid, 0, n - 1))

def main():
    t = int(input())
    for i in range(t):
        solve()
main()