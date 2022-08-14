"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

import os
import sys

from argparse import ArgumentParser


class DFAoC2021Python:
    """
    --day and --challenge arguments both required

    --day can be any value from 1-25 (for the days in AoC2021)
    --challenge should be either 'a' or 'b' to represent the first or second challenges

    When arguments are properly supplied script will assemble the name of the desired
    script to run.
    eg) $python3 -d 1 -c a  -  will attempt to run a script named day1a.py from ./src/
    """

    def arguments(self) -> ArgumentParser:
        parser = ArgumentParser(description="Argument parser for AoC2021")

        parser.add_argument(
            "-d", "--day", dest="day", required=True, type=int, choices=range(1, 26)
        )
        parser.add_argument(
            "-c", "--challenge", dest="challenge", required=True, choices=("a", "b")
        )

        self.args = parser.parse_args()

    def run(self):
        self.arguments()
        selection = f"day{self.args.day}{self.args.challenge}"
        try:
            print(f"Attempting to run ./src/{selection}.py")
            os.system(f"python3 ./src/{selection}.py")
            return 1
        except Exception as e:
            print(f"Unable to run ./src/{selection}.py: {e}")
            return 0


if __name__ == "__main__":
    script = DFAoC2021Python()
    return_code = script.run()
    sys.exit(return_code)
