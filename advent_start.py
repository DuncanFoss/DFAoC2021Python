"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

import sys
from argparse import ArgumentParser
from src import *

class DFAoC2021Python:
    """
    --day and --challenge arguments both required

    --day can be any value from 1-25 (for the days in AoC2021)
    --challenge should be either 'a' or 'b' to represent the first or second challenges

    When arguments are properly supplied script will assemble the name of the desired
    script to run.
    eg) $python3 -d 1 -c a  -  will attempt to run a script named day1a.py from ./src/
    """

    def __init__(self):
        self.args = None

    def arguments(self) -> ArgumentParser:
        """Sets up arguments used to determine execution behaviour"""
        parser = ArgumentParser(description="Argument parser for AoC2021")

        parser.add_argument(
            "-d", "--day", dest="day", required=True, type=int, choices=range(1, 25)
        )
        parser.add_argument(
            "-c", "--challenge", dest="challenge", required=True, choices=("a", "b")
        )

        self.args = parser.parse_args()

    def run(self):
        """Run routine for script"""
        self.arguments()
        selection = f"day{self.args.day}{self.args.challenge}"
        file = f"./docs/data/day{self.args.day}.txt"

        print(f"Attempting to read data from '{file}'...")
        try:
            data = open(file, "r", newline="").read().splitlines()
        except FileNotFoundError:
            print(f"Unable to read '{file}'.\nDoes it exist and is it named correctly?")
            return 1

        print(f"Executing day '{self.args.day}' challenge '{self.args.challenge}'...")

        try:
            if self.args.day == 1:
                day_script = day1.Day1(data, self.args.challenge)
            elif self.args.day == 2:
                day_script = day2.Day2(data, self.args.challenge)
            elif self.args.day == 3:
                day_script = day3.Day3(data, self.args.challenge)
            elif self.args.day == 4:
                day_script = day4.Day4(data, self.args.challenge)
            elif self.args.day == 5:
                day_script = day5.Day5(data, self.args.challenge)
            elif self.args.day == 6:
                day_script = day6.Day6(data, self.args.challenge)
            elif self.args.day == 7:
                day_script = day7.Day7(data, self.args.challenge)
            elif self.args.day == 8:
                day_script = day8.Day8(data, self.args.challenge)
            day_script.run()
        except:
            print(f"Unable to run {selection}.py")
            raise
        return 0

if __name__ == "__main__":
    SCRIPT = DFAoC2021Python()
    RETURN_CODE = SCRIPT.run()
    sys.exit(RETURN_CODE)
