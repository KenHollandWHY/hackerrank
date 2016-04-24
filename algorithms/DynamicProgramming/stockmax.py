def calc_profit(stock_values):
    days = len(stock_values)
    do_buy = [1]*days # 1 for buy, 0 for sell
    profit = 0
    maximum = 0
    for i in range(days-1,-1,-1):
        _temp = stock_values[i]
        if maximum <= _temp:
            do_buy[i] = 0 # sell
            maximum = _temp
        profit += maximum - _temp

    #print(profit, do_buy)

    return profit

#print(calc_profit([1,3,1,2]))

T = int(input().strip())
for t in range(T):
    N = int(input().strip())

    stock_values = list(map(int, input().strip().split()))
    print(calc_profit(stock_values))
