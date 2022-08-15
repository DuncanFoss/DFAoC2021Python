"""
Author: Duncan Foss
Project: Advent of Code 2021 Challenges for Day 1

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

class Day2:
    """Contains logic for day 2 challenges"""
    def __init__(self, data, challenge):
        self.data = data
        self.challenge = challenge

    def calculate_movement(self):
        """Calculates movements as required and returns coord and bearing dict"""
        coord = [0, 0]
        bearing = [0, 0, 0]

        for line in self.data:
            operator, value = line.split(" ")
            value = int(value)

            if operator == "forward":
                coord[0] += value
                bearing[0] += value
                bearing[1] += value * bearing[2]
            elif operator == "up":
                coord[1] -= value
                bearing[2] -= value
            elif operator == "down":
                coord[1] += value
                bearing[2] += value
            else:
                raise KeyError("Improper submarine movement. All hands lost.")
        return {'coord': coord, 'bearing': bearing}

    def run(self):
        """Run routine for script"""
        movement = self.calculate_movement()
        if self.challenge == 'a':
            result = movement['coord'][0] * movement['coord'][1]
        else:
            result = movement['bearing'][0] * movement['bearing'][1]
        print(f"Day 2 challenge {self.challenge.upper()} result: {result}")

if __name__ == "__main__":
    DATA = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    SCRIPT = Day2(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day2(DATA, 'b')
    SCRIPT.run()
