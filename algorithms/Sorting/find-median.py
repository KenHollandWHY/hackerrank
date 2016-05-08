N = int(input())
ar = [int(i) for i in input().strip().split()]
ar.sort()

index = N//2
print(ar[index])