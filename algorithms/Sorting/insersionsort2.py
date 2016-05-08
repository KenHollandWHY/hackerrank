#!/bin/python
def insertionSort(l):
    for i in range(1, len(l)):
        tmp = l[i]
        if(l[i-1] > tmp):
            j = i

            while (j > 0 and l[j-1] > tmp):
                l[j] = l[j-1]
                j -= 1

            l[j] = tmp
        print(' '.join(map(str, l)))

m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)