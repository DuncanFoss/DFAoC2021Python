"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""
import re


class Day5:
    """Contains logic for day 5 challenges"""

    def __init__(self, data, challenge):

        def flip_coords(coord_sets):
            holder = [coord_sets['x1'], coord_sets['y1']]
            coord_sets['x1'] = coord_sets['x2']
            coord_sets['y1'] = coord_sets['y2']
            coord_sets['x2'] = holder[0]
            coord_sets['y2'] = holder[1]
            return coord_sets

        self.data = data
        self.challenge = challenge

        self.h_lines = []
        self.v_lines = []
        self.d_lines = []

        x_max = 0
        y_max = 0

        self.intersect_threshold = 2

        for line in self.data:
            line = re.split(' -> |,', line)
            line_dict = {
                'x1': int(line[0]),
                'y1': int(line[1]),
                'x2': int(line[2]),
                'y2': int(line[3])
            }

            # Determines if line is horizontal, vertical, or diagonal and append to
            # appropriate list. All lists are oriented left to right in x coord order.
            if line_dict['x1'] == line_dict['x2']: # ascends
                if line_dict['y1'] > line_dict['y2']:
                    line_dict = flip_coords(line_dict)
                self.v_lines.append(line_dict)
            else:
                if line_dict['x1'] > line_dict['x2']:
                    line_dict = flip_coords(line_dict)
                if line_dict['y1'] == line_dict['y2']: # left to right
                    self.h_lines.append(line_dict)
                else:   # left to right, ascending or descending
                    self.d_lines.append(line_dict)

            # Tracks max dimensions of grid
            if x_max < line_dict['x1']:
                x_max = line_dict['x1']
            if x_max < line_dict['x2']:
                x_max = line_dict['x2']
            if y_max < line_dict['y1']:
                y_max = line_dict['y1']
            if y_max < line_dict['y2']:
                y_max = line_dict['y2']

        # Initialize grid
        self.grid = [[0]*(x_max + 1) for i in range(y_max + 1)]

    def process_horizontal(self):
        """Process horizontal lines"""
        for line in self.h_lines:
            x_pos = line['x1']
            while x_pos <= line['x2']:
                self.grid[x_pos][line['y1']] = self.grid[x_pos][line['y1']] + 1
                x_pos = x_pos + 1

    def process_vertical(self):
        """Process vertical lines"""
        for line in self.v_lines:
            y_pos = line['y1']
            while y_pos <= line['y2']:
                self.grid[line['x1']][y_pos] = self.grid[line['x1']][y_pos] + 1
                y_pos = y_pos + 1

    def process_diagonal(self):
        """Process diagonal lines"""
        for line in self.d_lines:
            x_pos = line['x1']
            y_pos = line['y1']

            # descending diagonals
            if y_pos > line['y2']:
                while y_pos >= line['y2']:
                    self.grid[x_pos][y_pos] = self.grid[x_pos][y_pos] + 1
                    x_pos = x_pos + 1
                    y_pos = y_pos - 1
            # ascending diagonals
            else:
                while y_pos <= line['y2']:
                    self.grid[x_pos][y_pos] = self.grid[x_pos][y_pos] + 1
                    x_pos = x_pos + 1
                    y_pos = y_pos + 1

    def count_excessive_intersections(self):
        """Count intersections over predefined limit"""
        counter = 0
        for line in self.grid:
            for val in line:
                if val >= self.intersect_threshold:
                    counter = counter + 1
        return counter

    def run(self):
        """Run routine for script"""
        self.process_horizontal()
        self.process_vertical()
        if self.challenge == 'b':
            self.process_diagonal()

        print(f"Day 5 challenge {self.challenge.upper()} result: " +
              f"{self.count_excessive_intersections()}")

if __name__ == "__main__":
    DATA = ["0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"]

    SCRIPT = Day5(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day5(DATA, 'b')
    SCRIPT.run()
