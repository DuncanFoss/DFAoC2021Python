"""
Author: Duncan Foss
Project: Advent of Code 2021

Licence: Use this code however you choose. If you copy it please provide credit.

Cheers!

Notes for puzzle:

Ordered by segment count followed by alphabetical order of sequence
Digit - # of occupied segments - letter codes for occupied digit portions
1 - 2 -       c        f
7 - 3 - a     c        f
4 - 4 -    b  c  d     f
5 - 5 - a  b     d     f  g
2 - 5 - a     c  d  e     g
3 - 5 - a     c  d     f  g
9 - 6 - a  b  c  d     f  g
0 - 6 - a  b  c     e  f  g
6 - 6 - a  b     d  e  f  g
8 - 7 - a  b  c  d  e  f  g


Labels for each digit portion

-aaa-
b   c
b   c
b   c
-ddd-
e   f
e   f
e   f
-ggg-

"""

# Functions - No reference to self
def solve_unique_display_digits(key_set, keys):
    """Solves for 1, 4, 7, and 8 (all unique character lengths)"""
    i = 0
    while i < len(keys):
        # i)    1 is 2 long
        if len(keys[i]) == 2:
            key_set['nums'][1] = [*(keys[i])]
            # unique_digit_count_instances = unique_digit_count_instances + 1
        # ii)   7 is 3 long
        elif len(keys[i]) == 3:
            key_set['nums'][7] = [*(keys[i])]
            # unique_digit_count_instances = unique_digit_count_instances + 1
        # iii)  4 is 4 long
        elif len(keys[i]) == 4:
            key_set['nums'][4] = [*(keys[i])]
            # unique_digit_count_instances = unique_digit_count_instances + 1
        # iv)  8 is 7 long
        elif len(keys[i]) == 7:
            key_set['nums'][8] = [*(keys[i])]
            # unique_digit_count_instances = unique_digit_count_instances + 1
        i = i + 1

def solve_for_five(key_set, keys):
    """Solves 5 - 5 digit sequence not containing a 'c' is a 5"""
    for k in keys:
        if len(k) == 5:
            if k.count(key_set['chars']['c']) == 0:
                key_set['nums'][5] = [*k]

def solve_for_three(key_set, keys):
    """Solves 3 - Of 5 digit sequences (2,3,5) only 3 is unsolved"""
    for k in keys:
        if len(k) == 5:
            if [*k] != key_set['nums'][5] and [*k] != key_set['nums'][2]:
                key_set['nums'][3] = [*k]

def solve_for_e(key_set):
    """# Solves 'e' - Last left in 2 after comparing with 3 and removing knowns"""
    for val in key_set['nums'][2]:
        if val not in key_set['nums'][3]:
            key_set['chars']['e'] = val

def solve_six_digits(key_set, keys):
    """Solves 6, 9, 0 - All 6 characters, 6 has no 'c', 9 no 'e', and 0 remains"""
    for k in keys:
        if len(k) == 6:
            if k.count(key_set['chars']['c']) == 0:
                key_set['nums'][6] = [*k]
            elif k.count(key_set['chars']['e']) == 0:
                key_set['nums'][9] = [*k]
            else:
                key_set['nums'][0] = [*k]

def solve_for_d(key_set):
    """Solves for 'd' - 'd' is last character in 8 that isn't in 0"""
    for val in key_set['nums'][8]:
        if val not in key_set['nums'][0]:
            key_set['chars']['d'] = val

def solve_for_b(key_set):
    """Solves for 'b' - 'b' is last unknown character in 4 (c d f are known)"""
    for val in key_set['nums'][4]:
        knowns = [key_set['chars']['c'],
                  key_set['chars']['d'],
                  key_set['chars']['f']]
        if val not in knowns:
            key_set['chars']['b'] = val

def solve_for_g(key_set):
    """Solves for 'g' - 'g' is last unknown in 8"""
    for val in key_set['nums'][8]:
        if val not in key_set['chars'].values():
            key_set['chars']['g'] = val

class Day8:
    """Contains logic for day 8 challenges"""

    def __init__(self, data, challenge):
        self.data = data
        self.challenge = challenge
        self.feed_data = []
        self.characters = [chr(c) for c in range(ord('a'), ord('h'))]

        # Counter for challenge 'a'
        self.unique_display_digits = 0

    def decode_digits(self, key_set, keys):
        """
        Calls all required methods and functions used to solve for both numbers and
        characters in the order required to do so.
        """
        solve_unique_display_digits(key_set, keys)

        # Solves 'a' - What 7 does not share with 1 is an 'a'
        key_set['chars']['a'] = [letter for letter in key_set['nums'][7] if \
            letter not in key_set['nums'][1]][0]

        self.solve_for_two_and_f(key_set, keys)

        # Solves 'c' - 1 has unknown ('c') and 'f' is known
        key_set['chars']['c'] = \
            ''.join(key_set['nums'][1]).replace(key_set['chars']['f'], '')

        solve_for_five(key_set, keys)
        solve_for_three(key_set, keys)
        solve_for_e(key_set)
        solve_six_digits(key_set, keys)
        solve_for_d(key_set)
        solve_for_b(key_set)
        solve_for_g(key_set)


    def solve_for_two_and_f(self, key_set, keys):
        """Solves for 2 - 2 is only # without an 'f'"""
        full_set = ''.join(keys)

        for val in self.characters:
            if full_set.count(val) == 9:
                key_set['chars']['f'] = val
                for sequence in keys:
                    if sequence.count(val) == 0:
                        key_set['nums'][2] = [*sequence]
                        break
                break

    def decode_display(self, key_set, display):
        """Reads & decodes the displays using key_set and returns the display reading"""
        display_digits = ""
        for digit in display:
            digit_set = set([*digit])
            for k, val in key_set['nums'].items():
                if len(digit_set - set(val)) == 0 and len(set(val) - digit_set) == 0:
                    display_digits = f"{display_digits}{k}"
                    if k in (1, 4, 7, 8):
                        self.unique_display_digits = self.unique_display_digits + 1
        return display_digits

    def run(self):
        """Run routine for script"""

        for data in self.data:
            split_text = data.split(" | ")
            keys = split_text[0].split(" ")
            display = split_text[1].split(" ")

            # Creates dict of dicts character to code and number to letter data
            key_set = {
                'chars': dict.fromkeys(self.characters, ''),
                'nums': dict.fromkeys(range(0, 10), [])
            }

            self.decode_digits(key_set, keys)

            # read, decode, and store displays
            display_digits = self.decode_display(key_set, display)

            self.feed_data.append({'keys': keys,
                                   'displays': {'encoded': display,
                                                'decoded': int(display_digits)},
                                   'key_set': key_set})
            display_total = 0
            for feed in self.feed_data:
                display_total = display_total + feed['displays']['decoded']

        if self.challenge == 'a':
            result = self.unique_display_digits
        else:
            result = display_total

        print(f"Day 8 challenge {self.challenge.upper()} result: {result}")

if __name__ == "__main__":
    DATA = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | ' + \
            'fdgacbe cefdb cefbgd gcbe',
            'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | ' + \
            'fcgedb cgb dgebacf gc',
            'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | ' + \
            'cg cg fdcagb cbg',
            'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | ' + \
            'efabcd cedba gadfec cb',
            'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | ' + \
            'gecf egdcabf bgf bfgea',
            'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | ' + \
            'gebdcfa ecba ca fadegcb',
            'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | ' + \
            'cefg dcbef fcge gbcadfe',
            'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ' + \
            'ed bcgafe cdgba cbgef',
            'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | ' + \
            'gbdfcae bgc cg cgb',
            'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | ' + \
            'fgae cfgab fg bagce']

    SCRIPT = Day8(DATA, 'a')
    SCRIPT.run()

    SCRIPT = Day8(DATA, 'b')
    SCRIPT.run()
