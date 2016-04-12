#!/usr/bin/python3

#Tn+2 = (Tn+1)^2 + Tn

A,B,N = map(int, input().strip().split())

T = [0]*N
T[0] = A
T[1] = B

for i in range(2, N):
    T[i] = T[i-1]**2 + T[i-2]
    #print(i, T[i])

print(T[N-1])
