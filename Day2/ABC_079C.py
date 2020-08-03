def make7(i, f, sum):
    if i == 3:
        if sum == 7:
            print(f + "=7")
            exit()
    else:
        make7(i+1, f+"+"+S[i+1], sum+int(S[i+1]))
        make7(i+1, f+"-"+S[i+1], sum-int(S[i+1]))


S = input()
n = len(S)

make7(0, S[0], int(S[0]))
