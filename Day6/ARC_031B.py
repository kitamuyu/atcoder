import copy

A = [list(input()) for i in range(10)]
A_copy = copy.deepcopy(A)

land_count = 0
reached = [[0] * 10 for i in range(10)]


def landfill(x, y):
    if x < 0 or 10 <= x or y < 0 or 10 <= y or A_copy[x][y] == "x":
        return
    if reached[x][y] == 1:
        return

    reached[x][y] = 1

    landfill(x+1, y)
    landfill(x-1, y)
    landfill(x, y+1)
    landfill(x, y-1)


for i in range(10):
    for j in range(10):
        if A[i][j] == "o":
            land_count += 1

for i in range(10):
    for j in range(10):
        reached = [[0] * 10 for i in range(10)]
        A_copy = copy.deepcopy(A)
        if A_copy[i][j] == "x":
            A_copy[i][j] = "o"
            # reached[i][j] = 1 はしないでおく(再起の中で絶対1になる)
            landfill(i, j)
        count = sum(map(sum, reached))

        if count == land_count + 1:
            print("YES")
            exit()
print("NO")
