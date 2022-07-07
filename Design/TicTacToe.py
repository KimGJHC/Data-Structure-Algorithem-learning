"""
348. Design Tic-Tac-Toe

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
"""


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        # row[0] the number of gamer1's mask in 0th row
        self.gamer = {'gamer1': {'row': [0] * n, 'col': [0] * n, 'diagonal': [0] * 2},
                      'gamer2': {'row': [0] * n, 'col': [0] * n, 'diagonal': [0] * 2}}

    def move(self, row, col, player):
        if player == 1:
            gamer = 'gamer1'
        else:
            gamer = 'gamer2'

        # update the mask placed by gamer
        # update row
        self.gamer[gamer]['row'][row] += 1
        # check if the gamer win
        if self.gamer[gamer]['row'][row] == self.n:
            return player

        # update col
        self.gamer[gamer]['col'][col] += 1
        # check if the gamer win
        if self.gamer[gamer]['col'][col] == self.n:
            return player

        # update diagonal
        if row == col:
            self.gamer[gamer]['diagonal'][0] += 1
        if row + col == self.n - 1:
            self.gamer[gamer]['diagonal'][1] += 1
        # check if the gamer win
        if self.gamer[gamer]['diagonal'][0] == self.n or self.gamer[gamer]['diagonal'][1] == self.n:
            return player
        return 0

# time: O(1) per move()
# space: O(n)