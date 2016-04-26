class Pos:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist_to(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

def next_move(posx, posy, board):
    bot_pos = Pos(posx, posy)

    dirty_poss = []
    for y in range(len(board)):
        #print(board[y])
        for x in range(len(board[y])):
            if board[y][x] == "d":
                dirty_poss.append(Pos(x, y))


    # find the nearest dirty pos.(but this select may not be the best for global?)
    next_d = None
    for dirty_pos in dirty_poss:
        if next_d is None or dirty_pos.dist_to(bot_pos) < next_d.dist_to(bot_pos):
            next_d = dirty_pos

    if next_d is not None:
        print_command(next_d.x - bot_pos.x, next_d.y - bot_pos.y)

def print_command(delta_x, delta_y):
    #print(delta_x, delta_y)
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

# Tail starts here
if __name__ == "__main__":
    r, c = [int(i) for i in input().strip().split()]
    h, w = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(h)]
    next_move(c, r, board)