N, K = map(int, input().strip().split())
prices = sorted([int(x) for x in input().strip().split()])
#print(prices)

buy_list = []
used = 0
for price in prices:
    used += price
    if used > K:
        break
    buy_list.append(price)

print(len(buy_list))