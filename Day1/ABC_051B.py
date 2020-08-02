K, S = map(int, input().split())
count = 0

for i in range(0, K+1):
    for j in range(0, K+1):
        k = S-j-i
        if k >= 0 and k <= K:
            count += 1

print(count)
