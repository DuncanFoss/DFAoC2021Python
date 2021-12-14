from lib.Models import BingoBoard
from lib.Utility import file_reader, derive_basename


class day4a:
    def run():
        source = file_reader(derive_basename(__file__))
        callouts = source.pop(0).split(",")
        boards: list[BingoBoard] = []
        board_stack = []
        next_board_id = 0

        def call_numbers():
            for number in callouts:
                for board in boards:
                    board.blot_number(number)
                    if board.winner:
                        return board.unblotted_sum * board.last_call

        for line in source:
            if line:
                if line[0] == " ":
                    board_line = line[1:].replace("  ", " ").split(" ")
                else:
                    board_line = line.replace("  ", " ").split(" ")
                board_stack.append(board_line)

            if len(board_stack) == 5:
                boards.append(BingoBoard(next_board_id, board_stack))
                next_board_id += 1
                board_stack = []

        print(f"Line SUM * last called number: {call_numbers()}")


if __name__ == "__main__":
    script = day4a()
    day4a.run()
