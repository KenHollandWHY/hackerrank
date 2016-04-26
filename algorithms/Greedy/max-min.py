N = int(input().strip())
K = int(input().strip())

values = sorted([int(input().strip()) for _ in range(N)])

unfairness = values[-1]

for i in range(N - K + 1):
    _temp_unfairness = values[i+K-1] - values[i] # max - min
    if unfairness > _temp_unfairness:
        unfairness = _temp_unfairness
    #print(unfairness)
print(unfairness)