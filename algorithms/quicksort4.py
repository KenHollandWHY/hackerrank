#!/bin/python

# for insersion sort
swap_cnt_insersion_sort = 0
def insertionSort(l):
    global swap_cnt_insersion_sort

    for i in range(1, len(l)):
        tmp = ar[i]
        if(ar[i-1] > tmp):
            j = i

            while (j > 0 and l[j-1] > tmp):
                l[j] = l[j-1]
                j -= 1
                swap_cnt_insersion_sort += 1

            l[j] = tmp


# for quick sort
swap_cnt_quick_sort = 0
def partition(ar, lo, hi):
    global swap_cnt_quick_sort
    pivot = ar[hi]
    i = lo # place for swapping
    for j in range(lo, hi):
        if ar[j] <= pivot:

            # swap ar[i] with ar[j]
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp
            swap_cnt_quick_sort += 1

            i += 1

    # swap ar[i] with ar[hi]
    temp = ar[i]
    ar[i] = ar[hi]
    ar[hi] = temp
    swap_cnt_quick_sort += 1

    return i

def quickSort(ar, lo, hi):
    if(lo < hi):
        p = partition(ar, lo, hi)
        quickSort(ar, lo, p - 1)
        quickSort(ar, p + 1, hi)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
ar_copy = ar[:]
insertionSort(ar)
quickSort(ar_copy, 0, len(ar_copy) - 1)
print(swap_cnt_insersion_sort-swap_cnt_quick_sort)