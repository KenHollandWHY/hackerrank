#!/usr/bin/python
directions = ["LEFT", "RIGHT", "UP", "DOWN"]

def displayPathtoPrincess(n,grid):
    princess_pos = None
    bot_pos = [N//2, N//2]
    #print(grid)
    #print(bot_pos)
    for i in range(N):
        this_row = grid[i]
        if 'p' in this_row:
            princess_pos = [this_row.index('p'), i]
        else:
            continue

    #print(princess_pos)

    diff_x = bot_pos[0] - princess_pos[0]
    diff_y = bot_pos[1] - princess_pos[1]

    #print(diff_x, diff_y)
    d_x = None
    if diff_x < 0:
        d_x = "RIGHT"
    else:
        d_x = "LEFT"

    if diff_y < 0:
        d_y = "DOWN"
    else:
        d_y = "UP"

    print("%s\n"%d_x*abs(diff_x), end="")
    print("%s\n"%d_y*abs(diff_y), end="")



N = int(input())
grid = []
for i in range(0, N):
    grid.append(list(input().strip()))

displayPathtoPrincess(N,grid)
