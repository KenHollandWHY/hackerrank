from __future__ import division

N = int(raw_input())
ar = [int(i) for i in raw_input().strip().split()]

length = len(ar)
mean = sum(ar)/length

ar = sorted(ar)
i = length//2
if length % 2 == 1:
    median = ar[i]
else:
    median = (ar[i-1] + ar[i])/2

mode = None
count_ar = [0]*pow(10, 5)
for a in ar:
    count_ar[a] += 1
mode = count_ar.index(max(count_ar))

s = pow(sum(map(lambda x: (x-mean)**2, ar))/N, 1/2)

print mean
print median
print mode
print s