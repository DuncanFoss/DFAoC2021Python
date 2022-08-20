"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

import copy


class BingoBoard: # First used in day 4 challenge a
    """
    Kind of hacky solution, will probably come back to clean it up at some point
    Vertical and horizontal line checks have repetitive code, should be easy to cleanup.
    """

    def __init__(self, board_id: int, values: 'list[list]'):

        self.board: 'list[list[str]]' = copy.deepcopy(values)
        self.blotted_board: 'list[list[str]]' = copy.deepcopy(values)
        self.board_id = board_id
        self.unblotted_sum: int = 0
        self.last_call: int = None
        self.winner = False
        self.processed = False

    def check_blots(self):
        """
        Returns 'True' if a winner is found, else 'False'
        """

        # horizontal blot lines
        for row in self.blotted_board:
            if row.count("X") == 5:
                self.winner = True

        # vertical blot lines
        for i, val in enumerate(self.blotted_board[0]):
            if val == "X":
                j = 1
                while j < 5:
                    if self.blotted_board[j][i] != "X":
                        j = 6
                    else:
                        j = j + 1

                    if j == 5:
                        self.winner = True

        return self.winner

    def blot_number(self, number: str):
        """Blots (marks as 'X') provided number on board if found"""
        if self.winner is not True:
            self.last_call = int(number)

        for i, row in enumerate(self.blotted_board):
            for j, value in enumerate(row):
                if value == number:
                    self.blotted_board[i][j] = "X"
                    self.check_blots()

    def calculate_unblotted_sum(self):
        """Return the sum of all unblotted numbers on the board"""
        for row in self.blotted_board:
            for value in row:
                if value != "X":
                    self.unblotted_sum += int(value)
        return self.unblotted_sum
