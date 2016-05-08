'''
[Ref] https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
'''
def next_permutation(arr):

    # Find non-increasing suffix
    len_arr = len(arr)
    i = len_arr-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len_arr-1
    while arr[j] <= arr[i-1]:
        j -= 1
    #print(i,j)

    # swap with privot
    arr[i-1], arr[j] = arr[j], arr[i-1]

    # Reverse suffix
    arr[i:] = arr[len_arr-1:i-1:-1]
    return True


T = int(input())
for t in range(T):
    w = list(input())
    if next_permutation(w):
        print(''.join(w))
    else:
        print('no answer')
