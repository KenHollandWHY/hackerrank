def rotate(l,n):
    n = n % len(l)
    return l[-n:] + l[:-n]

N, K, Q = [int(i) for i in input().strip().split()]
ar = [int(i) for i in input().strip().split()]
idx = []
for q in range(Q):
    idx.append(int(input()))

#print(ar)
ar = rotate(ar, K)
#print(ar)
for i in idx:
    print(ar[i])