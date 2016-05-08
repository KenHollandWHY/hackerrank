def is_sorted(a):
    b = a[:]
    b.sort()
    if a == b:
        return True
    else:
        return False

N = int(input())
arr = list(map(int,input().split()))

i = -1
j = -1

# find the start position for swap ot reverse
for n in range(N-1):
    if arr[n] > arr[n+1]:
        i = n
        break
# find the end position for swap ot reverse
for n in range(N-1, 0, -1):
    if arr[n] < arr[n-1]:
        j = n
        break
# create swapped array
temp_swap = arr[:]
temp_swap[i],temp_swap[j] = temp_swap[j],temp_swap[i]

# create reversed array
temp_reverse = arr[0:i] + arr[i:j+1][::-1] + arr[j+1:]

# check
if i == -1 and j == -1:
    print("yes")
elif is_sorted(temp_swap):
    print("yes")
    print("swap",i+1,j+1)
elif is_sorted(temp_reverse):
    print("yes")
    print("reverse",i+1,j+1)
else:
    print("no")
