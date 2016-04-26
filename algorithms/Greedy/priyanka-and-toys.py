from collections import defaultdict

N = int(input().strip())
W = sorted([int(x) for x in input().strip().split()])
toys = defaultdict(lambda: [])

price = 1
border_weight = W[0] + 4

for w in W:
    if border_weight < w:
        border_weight = w + 4
    else:
        pass

    toys[border_weight].append(w)

print(len(toys))