from collections import defaultdict

R = 100
N = int(input())

data = defaultdict(lambda: [])

for i in range(N):
    x, v = input().strip().split()
    x = int(x)
    if i < N/2:
        v = "-"
    data[x].append(v)

for key in sorted(data):
    #print(data[key])
    print(' '.join(data[key]), end = ' ')
print('')
