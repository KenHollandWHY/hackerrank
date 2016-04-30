N = int(input().strip())
X = list(map(int, input().strip().split()))

length = len(X)
mean = sum(X)/length

X = sorted(X)
i = length//2
if length % 2 == 1:
    median = X[i]
else:
    median = (X[i-1] + X[i])/2

mode = None
count_X = [0]*pow(10, 5)
for a in X:
    count_X[a] += 1
mode = count_X.index(max(count_X))

s = pow(sum(map(lambda x: (x-mean)**2, X))/N, 1/2)

lower = mean - 1.96*s/N**(1/2)
upper = mean + 1.96*s/N**(1/2)
print("%.1f"%mean)
print("%.1f"%median)
print("%d"%mode)
print("%.1f"%s)
print("%.1f %.1f"%(lower,upper))