from collections import defaultdict

N = int(input())
ar = list(map(int, input().strip().split()))

diff_pairs = defaultdict(lambda: [])
ar.sort()

min_diff = float('inf')
min_index = None

for i in range(N-1):
    diff = abs(ar[i+1] - ar[i])
    if diff <= min_diff:
        diff_pairs[diff].append([ar[i], ar[i+1]])
        min_index = diff
        if diff < min_diff and min_diff != float('inf'):
            # delete old data
            del(diff_pairs[min_diff])

        min_diff = diff

for v0, v1 in diff_pairs[min_index]:
    print("%d %d"%(v0, v1), end = " ")

print("")