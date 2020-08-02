n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = input().split()
    x.append(int(xi))
    y.append(int(yi))

longest_distance = 0

for i in range(n-1):
    for j in range(i+1, n):
        distance = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)
        if(longest_distance < distance):
            longest_distance = distance

print(longest_distance)
