R = 100
N = input()
ar = [int(i) for i in raw_input().strip().split()]


# count how many times appears for element
buckets = [0]*R
for x in ar:
    buckets[x] += 1

# sort
i = 0
for j in range(R):
    for k in range(buckets[j]):
        ar[i] = j
        i += 1

print(' '.join(map(str, ar)))