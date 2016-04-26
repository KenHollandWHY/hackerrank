T = int(input().strip())
for t in range(T):
    N, K = map(int, input().strip().split())
    A = sorted([int(x) for x in input().strip().split()])
    B = sorted([int(x) for x in input().strip().split()], reverse=True)

    flag = True
    for n in range(N):
        flag &= (A[n]+B[n] >= K)

    print("YES" if flag else "NO")