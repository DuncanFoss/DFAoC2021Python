from lib.Utility import data_reader, derive_basename
import re


class day5a:

    def run():
        h_lines = []
        v_lines = []
        d_lines = []
        all_lines = []

        x_max = 0
        y_max = 0

        INTERSECT_THRESHOLD = 2

        source = data_reader(derive_basename(__file__))

        def flip_coords(coord_sets):
            holder = [coord_sets['x1'], coord_sets['y1']]
            coord_sets['x1'] = coord_sets['x2']
            coord_sets['y1'] = coord_sets['y2']
            coord_sets['x2'] = holder[0]
            coord_sets['y2'] = holder[1]
            return coord_sets

        for line in source:
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
                v_lines.append(line_dict)
            else:
                if line_dict['x1'] > line_dict['x2']:
                    line_dict = flip_coords(line_dict)
                if line_dict['y1'] == line_dict['y2']: # left to right
                    h_lines.append(line_dict)
                else:   # left to right, ascending or descending
                    d_lines.append(line_dict)
            all_lines.append(line_dict)

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
        grid = [[0]*(x_max + 1) for i in range(y_max + 1)]
        
        # Process horizontal lines
        for line in h_lines:
            x_pos = line['x1']
            while x_pos <= line['x2']:
                grid[x_pos][line['y1']] = grid[x_pos][line['y1']] + 1
                x_pos = x_pos + 1

        # Process vertical lines
        for line in v_lines:
            y_pos = line['y1']
            while y_pos <= line['y2']:
                grid[line['x1']][y_pos] = grid[line['x1']][y_pos] + 1
                y_pos = y_pos + 1
        
        # Process diagonal lines
        for line in d_lines:
            x_pos = line['x1']
            y_pos = line['y1']

            # descending diagonals
            if y_pos > line['y2']:
                while y_pos >= line['y2']:
                    grid[x_pos][y_pos] = grid[x_pos][y_pos] + 1
                    x_pos = x_pos + 1
                    y_pos = y_pos - 1
            # ascending diagonals
            else:
                while y_pos <= line['y2']:
                    grid[x_pos][y_pos] = grid[x_pos][y_pos] + 1
                    x_pos = x_pos + 1
                    y_pos = y_pos + 1
        
        # Count intersections over predefined limit
        counter = 0
        for line in grid:
            for val in line:
                if val >= INTERSECT_THRESHOLD:
                    counter = counter + 1
        
        print(f"Final count of grid locations with at least 2 overlaps with horizontal, vertical, and diagonal vents: {counter}")

if __name__ == "__main__":
    script = day5a()
    day5a.run()
