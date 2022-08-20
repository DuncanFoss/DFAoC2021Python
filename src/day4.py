"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""
from lib.models import BingoBoard


class Day4:
    """Contains logic for day 4 challenges"""

    def __init__(self, data, challenge):
        self.data = data
        self.challenge = challenge
        self.board_list = []
        self.winner_count: int = 0
        self.board_stack = []
        self.call_outs = self.data.pop(0).split(",")
        self.selected_winner = None

    def call_numbers(self):
        """
        Calls all of the bingo numbers until either the first winning board is
        found (challenge A) or the last winner has been found (challenge b).
        Returns selected board.
        """
        selected_board = None
        for number in self.call_outs:
            for board in self.board_list:
                if len(self.board_list) > 0:
                    board.blot_number(number)

                if board.processed is False and board.winner:
                    board.processed = True
                    if self.challenge == 'a':
                        selected_board = board
                    else:
                        self.winner_count = self.winner_count + 1
                        if self.winner_count == len(self.board_list):
                            selected_board = board
                    if selected_board:
                        break
            if selected_board:
                break
        return selected_board

    def run(self):
        """Run routine for script"""

        next_board_id = 0

        # Assemble list of boards. Builds a stack of lines first, then makes board
        for line in self.data:
            if line:
                if line[0] == " ":
                    board_line = line[1:].replace("  ", " ").split(" ")
                else:
                    board_line = line.replace("  ", " ").split(" ")
                self.board_stack.append(board_line)

            if len(self.board_stack) == 5:
                self.board_list.append(BingoBoard(next_board_id, self.board_stack))
                next_board_id += 1
                self.board_stack = []
        winner = self.call_numbers()

        if winner:
            result = winner.calculate_unblotted_sum() * winner.last_call
            print(f"Day 4 challenge {self.challenge.upper()} result: {result}")
        else:
            print("No winner identified")

if __name__ == "__main__":
    DATA = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
            '',
            '22 13 17 11  0',
            ' 8  2 23  4 24',
            '21  9 14 16  7',
            ' 6 10  3 18  5',
            ' 1 12 20 15 19',
            '',
            ' 3 15  0  2 22',
            ' 9 18 13 17  5',
            '19  8  7 25 23',
            '20 11 10 24  4',
            '14 21 16 12  6',
            '',
            '14 21 17 24  4',
            '10 16 15  9 19',
            '18  8 23 26 20',
            '22 11 13  6  5',
            ' 2  0 12  3  7']

    SCRIPT = Day4(DATA.copy(), 'a')
    SCRIPT.run()

    SCRIPT = Day4(DATA, 'b')
    SCRIPT.run()
