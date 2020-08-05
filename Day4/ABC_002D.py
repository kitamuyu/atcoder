N, M = map(int, input().split())
relation = [list(map(int, input().split())) for i in range(M)]

max_members = 1

for bit in range(1 << N):
    members = []
    isPossible = True
    for i in range(N):
        if bit & 1 << i:
            members.append(i+1)

    n = len(members)
    for i in range(n-1):
        for j in range(i+1, n):
            if [members[i], members[j]] in relation:
                isPossible = True
            else:
                isPossible = False
                break
        if(not isPossible):
            break

    if(isPossible):
        max_members = max(max_members, n)

print(max_members)
