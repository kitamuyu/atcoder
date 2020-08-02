N, Y = map(int, input().split())
flag = False

for i in range(0, N+1):  # 10000
    for j in range(0, N+1-i):  # 5000
        if 10000*i + 5000*j + 1000*(N-i-j) == Y:
            print(i, j, N-i-j)
            flag = True
            break
    if flag:
        break
else:
    if not flag:
        print("-1 -1 -1")
