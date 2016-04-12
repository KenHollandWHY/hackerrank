#!/usr/bin/python3

T = int(input())
for t in range(T):
    Px,Py,Qx,Qy = map(int, input().strip().split())
    Rx = 2*Qx - Px
    Ry = 2*Qy - Py
    print(Rx, Ry)