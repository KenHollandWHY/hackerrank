from collections import defaultdict
import math

def nPr(n,r):
    f = math.factorial
    return f(n)//f(n-r)

T = int(input())
for t in range(T):
    N = int(input())
    data = defaultdict(lambda: 0)
    for index, a in enumerate(map(int,input().split())):
        data[a] += 1

    cnt = 0
    for key, value in data.items():
        if value > 1:
            cnt += nPr(value, 2)

    print(cnt)