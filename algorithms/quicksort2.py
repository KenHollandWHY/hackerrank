#!/bin/python
def quickSort(ar):
    if len(ar) < 2:
        return(ar)

    p = ar[0]
    left = []
    right = []
    for a in ar[1:]:
        if a > p:
            right.append(a)
        else:
            left.append(a)

    l = quickSort(left)
    r = quickSort(right)

    ret = l+ [p] + r
    print(' '.join(map(str, ret)))
    return ret

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)