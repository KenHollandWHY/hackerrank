# using merge sort
def count_inversions(arr):
    n = len(arr)
    if n == 1:
        return 0

    n1 = n//2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    cnt = count_inversions(arr1) + count_inversions(arr2)

    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            cnt += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    #print(n, n1, n2, arr1, arr2, cnt)
    return cnt

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = count_inversions(arr)
    print(cnt)
