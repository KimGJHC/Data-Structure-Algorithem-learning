"""
1275. Find Winner on a Tic Tac Toe Game
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = {'row': [0, 0, 0], 'col': [0, 0, 0], 'diag': [0, 0]}  # {row = [0, 0, 0], col = [0, 0, 0], diag=[0, 0]}
        B = {'row': [0, 0, 0], 'col': [0, 0, 0], 'diag': [0, 0]}

        current = 'A'

        for move in moves:
            if current == 'A':
                r_move, c_move = move
                A['row'][r_move] += 1
                A['col'][c_move] += 1

                if r_move == c_move:
                    if r_move == 1:
                        A['diag'][0] += 1
                        A['diag'][1] += 1
                    else:
                        A['diag'][0] += 1
                elif r_move + c_move == 2:
                    A['diag'][1] += 1

                if 3 in A['row'] or 3 in A['col'] or 3 in A['diag']:
                    return current

                current = 'B'
            else:
                r_move, c_move = move
                B['row'][r_move] += 1
                B['col'][c_move] += 1

                if r_move == c_move:
                    if r_move == 1:
                        B['diag'][0] += 1
                        B['diag'][1] += 1
                    else:
                        B['diag'][0] += 1
                elif r_move + c_move == 2:
                    B['diag'][1] += 1

                if 3 in B['row'] or 3 in B['col'] or 3 in B['diag']:
                    return current

                current = 'A'

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

# time: O(m) where m = len(moves) / O(1)
# space: O(n) n = 3