"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

from src import *
from lib import Utility, Models
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
        file = f"./docs/data/day{self.args.day}.txt"

        print(f"Attempting to read data from '{file}'...")
        try:
            data = open(file, "r", newline="").read().splitlines()
        except:
            print(f"Unable to read '{file}'.\nDoes it exist and is it named correctly?")
            return 1

        print(f"Attempting to run code for day '{self.args.day}' challenge '{self.args.challenge}'...")

        try:
            if self.args.day == 1:
                day_script = day1.Day1(data, self.args.challenge)
        #     elif selection == 'day2':
        #         day_script = day2a() if self.args.challenge == 'a' else day2b()
        #     elif selection == 'day3':
        #         day_script = day3a() if self.args.challenge == 'a' else day3b()
        #     elif selection == 'day4':
        #         day_script = day4a() if self.args.challenge == 'a' else day4b()
        #     elif selection == 'day5':
        #         day_script = day5a() if self.args.challenge == 'a' else day5b()
        #     elif selection == 'day6':
        #         day_script = day6a() if self.args.challenge == 'a' else day6b()
        #     elif selection == 'day7':
        #         day_script = day7a() if self.args.challenge == 'a' else day7b()
        #     elif selection == 'day8':
        #         day_script = day8a() if self.args.challenge == 'a' else day8b()
        #     elif selection == 'day9':
        #         day_script = day9a() if self.args.challenge == 'a' else day9b()
        #     elif selection == 'day10':
        #         day_script = day10()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
        #     elif selection == 'day1a':
        #         day_script = day1a()
            
            day_script.run()
        except Exception as e:
            print(f"Unable to run {selection}.py - Does the file exist?")
            print(e)

if __name__ == "__main__":
    script = DFAoC2021Python()
    return_code = script.run()
    sys.exit(return_code)
