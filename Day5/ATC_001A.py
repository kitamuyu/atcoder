import sys
sys.setrecursionlimit(500 * 500)

H, W = map(int, input().split())
c = [list(input()) for i in range(H)]

reached = [[False] * W for i in range(H)]


def search(x, y):
    if x < 0 or H <= x or y < 0 or W <= y or c[x][y] == "#":
        return
    if reached[x][y]:
        return

    reached[x][y] = True

    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)


start = []
goal = []

for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            start = [i, j]
        if c[i][j] == "g":
            goal = [i, j]

search(start[0], start[1])

if reached[goal[0]][goal[1]]:
    print("Yes")
else:
    print("No")
