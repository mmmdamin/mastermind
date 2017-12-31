import random

from consts import *


class Game(object):
    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.initial_state = self.new_game()
        self.turns = 0
        self.is_won = False
        self.is_ended = False

    def new_game(self):
        initial = []
        while len(initial) < self.length:
            r = random.randint(MIN_COLOR, MAX_COLOR)
            if r not in initial:
                initial.append(r)
        initial = [COLORS[i] for i in initial]
        return initial

    def turn(self):
        if self.is_ended:
            print("Game Over!")
            return

        guess = input()
        guess = guess.split(",")

        black = 0
        white = 0
        for i in range(self.length):
            if self.initial_state[i] == guess[i]:
                black += 1
            elif guess[i] in self.initial_state:
                white += 1

        print("black: {} , white: {}".format(black, white))

        self.turns += 1
        self.check_state(black)

    def to_str(self):
        return ",".join(self.initial_state)

    def check_state(self, black):
        if self.check_win(black):
            print(WIN_MESSAGE)
            self.end()
        elif self.check_lose():
            print(LOSE_MESSAGE.format(self.to_str()))
            self.end()

    def check_win(self, black):
        return black == self.length

    def check_lose(self):
        return (self.turns == MAX_TURNS) and not self.is_won

    def end(self):
        self.is_ended = True

    @staticmethod
    def start():
        for i in range(MAX_TURNS):
            game.turn()


game = Game()
game.start()
