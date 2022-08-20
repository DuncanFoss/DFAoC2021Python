"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

class Day6:
    """Contains logic for day 6 challenges"""

    def __init__(self, data, challenge):
        self.data = data[0].split(',')
        self.challenge = challenge

        self.iteration_limit = 80 if challenge == 'a' else 256
        self.iteration_count = 0
        self.fish_population = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        self.new_fish = 0

    def advance_states(self):
        """Advances the states by one iteration"""
        while self.iteration_count < self.iteration_limit:
            self.new_fish = self.fish_population[0]
            roll_over = self.fish_population[0]
            self.fish_population[0] = self.fish_population[1]
            self.fish_population[1] = self.fish_population[2]
            self.fish_population[2] = self.fish_population[3]
            self.fish_population[3] = self.fish_population[4]
            self.fish_population[4] = self.fish_population[5]
            self.fish_population[5] = self.fish_population[6]
            self.fish_population[6] = self.fish_population[7] + roll_over
            self.fish_population[7] = self.fish_population[8]
            self.fish_population[8] = self.new_fish
            self.iteration_count = self.iteration_count + 1

            self.new_fish = 0

    def run(self):
        """Run routine for script"""
        for state in self.data:
            self.fish_population[int(state)] = self.fish_population[int(state)] + 1

        self.advance_states()

        print(f"Day 6 challenge {self.challenge.upper()} result: " +
              f"{sum(self.fish_population.values())}")


if __name__ == "__main__":
    DATA = ["3,4,3,1,2"]

    SCRIPT = Day6(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day6(DATA, 'b')
    SCRIPT.run()
