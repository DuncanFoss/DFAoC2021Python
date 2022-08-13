import copy


class BingoBoard: # First used in day 4 challenge a
    """
    Kind of hacky solution, will probably come back to clean it up at some point
    Vertical and horizontal line checks have repetitive code, should be easy to cleanup.
    """

    board: 'list[list[str]]' = []
    blotted_board: 'list[list[str]]' = []
    winning_state: 'list[list[str]]' = None
    last_call: int = None
    unblotted_sum: int = 0
    winner = False

    def __init__(self, board_id: int, values: 'list[list]'):
        self.board = copy.deepcopy(values)
        self.blotted_board = copy.deepcopy(values)
        self.board_id = board_id

    def check_blots(self, last_call):
        """
        Returns 'True' if a winner is found, else 'False'
        """

        # horizontal blot lines
        for i, row in enumerate(self.blotted_board):
            blot_count = 0
            for j, value in enumerate(row):
                if value == "X":
                    blot_count += 1
            if blot_count == 5:
                self.winner = True
                if self.winning_state is None:
                    self.winning_state = copy.deepcopy(self.blotted_board)
                    self.calculate_unblotted_sum()
                    self.last_call = int(last_call)

        # vertical blot lines
        for i, row in enumerate(self.blotted_board):
            blot_count = 0
            j = 0
            while j < 5:
                if self.blotted_board[j][i] == "X":
                    blot_count += 1
                if blot_count == 5:
                    self.winner = True
                    if self.winning_state is None:
                        self.winning_state = copy.deepcopy(self.blotted_board)
                        self.calculate_unblotted_sum()
                        self.last_call = int(last_call)
                    # print(f"BOARD ID '{self.board_id}' HAS WON")
                j += 1

        return self.winner

    def blot_number(self, number: str):
        for i, row in enumerate(self.blotted_board):
            for j, value in enumerate(row):
                if value == number:
                    self.blotted_board[i][j] = "X"
                    self.check_blots(number)

    def calculate_unblotted_sum(self):
        for row in self.winning_state:
            for value in row:
                if value != "X":
                    self.unblotted_sum += int(value)
