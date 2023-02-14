#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        move = input("'rock', 'paper', or 'scissors'?")
        while move not in moves:
            print("invalid input!")
            move = input("'rock', 'paper', or 'scissors'?")
        return move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    x = 0

    def move(self):
        if self.x != 966:
            self.x = 966
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    x = 0

    def move(self):
        if self.x != 966:
            self.x = 966
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.score[0] = self.score[0] + 1
            print("Player 1 wins the round!")
        elif beats(move2, move1):
            self.score[1] = self.score[1] + 1
            print("Player 2 wins the round!")
        else:
            print("Round TIE!")
        print(f"Score | Player 1: {self.score[0]}  Player 2: {self.score[1]}")

    def play_game(self):
        self.score = [0, 0]
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        if self.score[0] > self.score[1]:
            print("Player 1 wins!")
            print(f"Final Score | Player 1: {self.score[0]}  Player 2: {self.score[1]}")
        elif self.score[0] < self.score[1]:
            print("Player 2 wins!")
            print(f"Final Score | Player 1: {self.score[0]}  Player 2: {self.score[1]}")
        else:
            print("Game Tie!")
            print(f"Final Score | Player 1: {self.score[0]}  Player 2: {self.score[1]}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), RandomPlayer())
    game.play_game()
