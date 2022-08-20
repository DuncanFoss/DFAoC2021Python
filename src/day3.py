"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!
"""

class Day3:
    """Contains logic for day 3 challenges"""
    def __init__(self, data, challenge):
        self.data = data
        self.challenge = challenge

    def calc_gamma_and_epsilon(self):
        """Calculates gamma and epsilon values for submarine"""
        rates = {"g": "", "e": ""}
        digit_counts = [0] * len(self.data[0])

        # Counts occurrences of '1' digits in a binary string
        for line in self.data:
            for i, digit in enumerate(line):
                if int(digit) == 1:
                    digit_counts[i] += 1

        for count in digit_counts:
            if count > (len(self.data) / 2):
                rates["g"] = f"{rates['g']}1"
            else:
                rates["g"] = f"{rates['g']}0"

        # creates bit flipped copy of the binary sequence stored in data["e"]
        for i, digit in enumerate(rates["g"]):
            rates["e"] = rates["e"] + "0" if rates["g"][i] == "1" else rates["e"] + "1"

        return rates

    def sort_values(self, common_val: bool = True):
        """Returns sorted dictionary of life support readings"""
        digit_check = 0
        post_sort = []
        presort = self.data.copy()

        while len(presort) > 1:
            digit_count = 0
            chosen_value = "1"
            # count occurrences of digit
            for line in presort:
                if line[digit_check] == "1":
                    digit_count += 1

            if digit_count < len(presort) / 2:
                chosen_value = "0"

            for line in presort:
                if common_val:
                    if line[digit_check] == chosen_value:
                        post_sort.append(line)
                else:
                    if line[digit_check] != chosen_value:
                        post_sort.append(line)

            if len(post_sort) > 1:
                presort = post_sort
                post_sort = []
            else:
                return post_sort.pop()

            digit_check += 1

    def run(self):
        """Run routine for script"""
        if self.challenge == 'a':
            rates = self.calc_gamma_and_epsilon()
            print(f"Product of g * e: {int(rates['g'], 2) * int(rates['e'], 2)}")
        else:
            rates = {"o": self.sort_values(), "c": self.sort_values(False)}
            print(f"Product of o * c: {int(rates['o'], 2) * int(rates['c'], 2)}")


if __name__ == "__main__":
    DATA = ['00100', '11110', '10110', '10111',
            '10101', '01111', '00111', '11100',
            '10000', '11001', '00010', '01010']

    SCRIPT = Day3(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day3(DATA, 'b')
    SCRIPT.run()
