'''
[Ref] https://www.hackerrank.com/challenges/connected-cell-in-a-grid/editorial
'''
from itertools import chain

def dfs(arr, r, c, currentCount):
    if arr[r][c] == 1:
        arr[r][c] = currentCount
        for delR in range(-1, 2):
            for delC in range(-1, 2):
                if delR*delR + delC*delC > 0: # except myself
                    if arr[r+delR][c+delC] == 1:
                        currentCount = dfs(arr, r+delR, c+delC, currentCount+1)
    return currentCount



n = int(input().strip())
m = int(input().strip())

arr = [[0 for i in range(m+2)] for j in range(n+2)]

for j in range(1, n+1):
    arr[j][1:-1] = list(map(int, input().strip().split()))

#print(arr)
for r in range(1,n+1):
    for c in range(1, m+1):
        if arr[r][c] == 1:
            dfs(arr, r, c, 2)

flatten_list = list(chain.from_iterable(arr))
#print(flatten_list)
print(max(flatten_list) - 1) # max(flatten) - 1