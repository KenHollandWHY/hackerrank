N, K = map(int, input().strip().split())
flowers = sorted([int(x) for x in input().strip().split()], reverse=True)
num_flowers = len(flowers)

total_cost = 0

for i, flower in enumerate(flowers):
    num = i // K
    #print(num)
    total_cost += (num + 1) * flower

print(total_cost)