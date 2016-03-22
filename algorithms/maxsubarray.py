def maxSubArraySum(arr):
    # calcurate non continuous maximum sum
    max_so_far_non_cont = sum(x for x in arr if x > 0)
    if(max_so_far_non_cont == 0):
        max_so_far_non_cont = max(arr)

    # calcurate continuous maximum sum
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    if(max_so_far == 0):
        max_so_far = max(arr)
    return (max_so_far, max_so_far_non_cont)


if __name__ == '__main__':
    test_cases = int(raw_input())
    arr = []
    for i in xrange(test_cases):
        arr_length = int(raw_input())
        arr = [int(i) for i in raw_input().split()]
        (max_so_far, max_so_far_non_cont) = maxSubArraySum(arr)
        print("%d %d")%(max_so_far, max_so_far_non_cont)
