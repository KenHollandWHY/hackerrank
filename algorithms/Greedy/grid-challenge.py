T = int(input().strip())

for t in range(T):
    N = int(input().strip())
    G = [[x for x in input().strip()] for n in range(N)]

    #print(G)
    flag = True
    for i in range(N):
        G[i] = sorted(G[i])
        #print(G[i])
        if(i > 0):
            for j in range(N):
                flag &= G[i][j] >= G[i-1][j]
    all_sorted = "YES" if flag else "NO"
    print(all_sorted)