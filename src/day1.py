"""
Author: Duncan Foss
Project: Advent of Code 2021 Challenges for Day 1

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

class Day1:
    """Contains logic for day 1 challenges"""

    WINDOW = 3

    def __init__(self, data, challenge):
        self.data = data
        self.challenge = challenge

    def increment_count(self):
        """
        Returns count of how often the next number in a list is larger than the last
        """
        count = 0
        holder = None
        for number in self.data:
            number = int(number)
            if holder is not None:
                if number > holder:
                    count = count + 1
            holder = number
        return count

    def roll_count(self):
        """
        Returns count of how often a rolling sum of 3 values in a list is larger
        than it was in previous iteration
        """
        holders = []
        watermark = None

        count = 0

        for number in self.data:
            number = int(number)
            if len(holders) == self.WINDOW:
                holders.pop(0)
            holders.append(int(number))

            if watermark is not None and len(holders) == self.WINDOW:
                if watermark < sum(holders):
                    count += 1

            if len(holders) == self.WINDOW:
                watermark = sum(holders)

        return count

    def run(self):
        """Run routine"""
        result = self.increment_count() if self.challenge == 'a' else self.roll_count()
        print(f"Day 1 challenge {self.challenge.upper()} result: {result}")

if __name__ == "__main__":
    DATA = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
    SCRIPT = Day1(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day1(DATA, 'b')
    SCRIPT.run()
