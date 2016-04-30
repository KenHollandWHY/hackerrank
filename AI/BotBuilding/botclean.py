#!/usr/bin/python

def find_next_d(posr, posc, board):
    d_pos = [] # x,y

    board_length = len(board)
    distance = float('inf')
    for j in range(board_length):
        for i in range(board_length):
            if(board[j][i] == 'd'):
                _temp = abs(posr - j) + abs(posc - i)
                if _temp < distance:
                    distance = _temp
                    d_pos = [i,j]
    return d_pos


def next_move(posr, posc, board):
    d_pos = find_next_d(posr, posc, board)

    delta_x = d_pos[0] - posc
    delta_y = d_pos[1] - posr

    # print
    if delta_x > 0 :
        print("RIGHT")
    elif delta_x < 0 :
        print("LEFT")
    elif delta_y > 0 :
        print("DOWN")
    elif delta_y < 0 :
        print("UP")
    else:
        print("CLEAN")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
