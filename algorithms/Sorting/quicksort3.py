#!/bin/python
def partition(ar, lo, hi):
    pivot = ar[hi]
    i = lo # place for swapping
    for j in range(lo, hi):
        if ar[j] <= pivot:
            # swap ar[i] with ar[j]
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp

            i += 1

    # swap ar[i] with ar[hi]
    temp = ar[i]
    ar[i] = ar[hi]
    ar[hi] = temp

    print(' '.join(map(str, ar)))

    return i

def quickSort(ar, lo, hi):
    if(lo < hi):
        p = partition(ar, lo, hi)
        quickSort(ar, lo, p - 1)
        quickSort(ar, p + 1, hi)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar, 0, len(ar) - 1)