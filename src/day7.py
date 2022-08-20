"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

class Day7:
    """Contains logic for day 7 challenges"""

    def __init__(self, data, challenge):
        self.data = list(map(int, data[0].split(',')))
        self.challenge = challenge
        self.pos = max(self.data)
        self.linear = {}
        self.scaling = {}

    def calculate_movements(self):
        """Calculates optimal movements for both linear and scaling fuel costs"""
        while self.pos >= 0:
            self.linear[self.pos] = 0
            self.scaling[self.pos] = 0
            for state in self.data:
                abs_val = abs(self.pos - state)
                self.linear[self.pos] = self.linear[self.pos] + abs_val
                self.scaling[self.pos] = self.scaling[self.pos] + \
                    sum(range(1, abs_val + 1))
            self.pos = self.pos - 1

    def run(self):
        """Run routine for script"""
        self.calculate_movements()

        if self.challenge == 'a':
            result = min(self.linear.items(), key=lambda data: data[1])
        else:
            result = min(self.scaling.items(), key=lambda data: data[1])

        print(f"Day 7 challenge {self.challenge.upper()} result: " +
              f" Collectively move to {result[0]}. Will cost {result[1]} fuel.")

if __name__ == "__main__":
    DATA = ["16,1,2,0,4,2,7,1,2,14"]

    SCRIPT = Day7(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day7(DATA, 'b')
    SCRIPT.run()
