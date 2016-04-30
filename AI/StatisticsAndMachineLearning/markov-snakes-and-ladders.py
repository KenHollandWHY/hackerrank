import random

BOARD_SIZE = 100
LIMIT_MOVES = 1000
#LIMIT_MOVES = 20
NUM_TRIALS = 5000
#NUM_TRIALS = 2

class Board:
    def __init__(self, probs, start_end):
        self.current = 1
        self.probs = [float(x) for x in probs]
        self.warp = {}
        for start, end in start_end:
            self.warp[start] = end

    def move(self, num):
        if self.current + num <= BOARD_SIZE:
            self.current += num
        if self.current in self.warp:
            self.current = self.warp[self.current]
        return self.current

    def roll(self):
        rand = random.random()
        for index, prob in enumerate(self.probs):
            if rand < prob:
                return index + 1
            rand -= prob
        return 6

    def play(self):
        num_moves = 0
        while num_moves < LIMIT_MOVES and self.move(self.roll()) != BOARD_SIZE:
            num_moves += 1
        return num_moves


if __name__ == "__main__":

    T = int(input().strip())
    for t in range(T):
            probs = list(map(float, input().strip().split(",")))
            num_ladders, num_snakes = map(int, input().strip().split(","))
            ladders = [list(map(int, x.split(","))) for x in input().strip().split(" ")]
            snakes = [list(map(int, x.split(","))) for x in input().strip().split(" ")]
            sum_moves = 0
            num_trials = 0
            for i in range(NUM_TRIALS):
                board = Board(probs, ladders+snakes)
                num_moves = board.play()
                if num_moves < LIMIT_MOVES:
                    sum_moves += num_moves
                    num_trials += 1
            print(sum_moves//num_trials)