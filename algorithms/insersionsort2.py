#!/bin/python
def insertionSort(l):

    for i in range(1, len(l)):
        tmp = ar[i]
        if(ar[i-1] > tmp):
            j = i

            while (j > 0 and l[j-1] > tmp):
                l[j] = l[j-1]
                j -= 1

            l[j] = tmp
        print ' '.join(map(str, l))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)