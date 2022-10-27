# Grid Challenge

t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    for j in range(n):
        gr = list(map(str,input().split()))
        gr.sort()
        grid.append(gr)
print(grid)


def gridChallenge(grid):

    for i in range(n-1):
        for j in range(n):
            if grid[i][j] > grid[i+1][j]:
                return False

    return True

if gridChallenge(grid):
    print('YES')
else:
    print('NO')
