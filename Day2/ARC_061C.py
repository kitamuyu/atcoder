S = input()
n = len(S)

ans = 0

for bit in range(1 << (n - 1)):
    partial_sum = S[0]
    for i in range(n-1):
        if bit & (1 << i):
            partial_sum += "+"
        partial_sum += S[i+1]
    ans += sum(map(int, partial_sum.split("+")))

print(ans)
