N = int(input())
t = [int(input()) for i in range(N)]

min_time = float("inf")

for bit in range(1 << N):
    grill1 = 0
    grill2 = 0
    for i in range(N):
        if bit & 1 << i:
            grill1 += t[i]
        elif not bit & 1 << i:
            grill2 += t[i]
    min_time = min(min_time, max(grill1, grill2))

print(min_time)
