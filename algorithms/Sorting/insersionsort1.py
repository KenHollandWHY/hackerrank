#!/bin/python
def insertionSort(ar):
    n = len(ar)
    target = ar[n-1]
    k = n-2
    while k >=0 and ar[k] > target:
        ar[k + 1] = ar[k]
        print(' '.join(map(str, ar)))
        k -= 1
    ar[k + 1] = target
    print(' '.join(map(str, ar)))

N = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)