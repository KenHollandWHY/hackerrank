N = int(input().strip())
data = {}
for n in range(N):
    t, d = [int(x) for x in input().strip().split()]
    data[n+1] = t+d

print(" ".join(map(str, sorted(data, key=data.get))))
