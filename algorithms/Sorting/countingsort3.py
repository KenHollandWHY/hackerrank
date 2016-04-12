R = 100
N = input()

arr = [0]*R
for i in range(N):
    x, _ = raw_input().strip().split()
    x = int(x)
    arr[x] += 1

s = 0
for j in range(R):
    s += arr[j]
    print s,
