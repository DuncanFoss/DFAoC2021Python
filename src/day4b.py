from lib.Models import BingoBoard
from lib.Utility import data_reader, derive_basename


class day4b:
    def run():
        source = data_reader(derive_basename(__file__))
        callouts = source.pop(0).split(",")
        board_list: list[BingoBoard] = []
        winner_stack: list[int] = []
        board_stack = []
        next_board_id = 0

        def call_numbers():
            for number in callouts:
                for board in board_list:
                    board.blot_number(number)
                    if board.winner:
                        add_winner(board)

        def add_winner(winning_board: BingoBoard):
            if winning_board.board_id not in winner_stack:
                winner_stack.append(winning_board.board_id)

        # Build board_list
        for line in source:
            if line:
                if line[0] == " ":
                    board_line = line[1:].replace("  ", " ").split(" ")
                else:
                    board_line = line.replace("  ", " ").split(" ")
                board_stack.append(board_line)

            if len(board_stack) == 5:
                board_list.append(BingoBoard(next_board_id, board_stack))
                next_board_id += 1
                board_stack = []

        call_numbers()

        for board in board_list:
            if board.board_id == winner_stack[-1]:
                result = 94 * board.unblotted_sum
                print(f"Board with the id '{board.board_id}' was last to win.")
                print(f"Line sum * last called number: {result}")


if __name__ == "__main__":
    script = day4a()
    day4a.run()
