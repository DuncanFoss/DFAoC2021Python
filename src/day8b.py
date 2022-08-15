from lib.Utility import data_reader, derive_basename


class day8b:
    def run():
        source = data_reader(derive_basename(__file__))
        feed_data = []
        characters = [c for c in (chr(c) for c in range(ord('a'), ord('h')))]
        unique_digit_count_instances = 0
        
        for s in source:
            split_text = s.split(" | ")
            keys = split_text[0].split(" ")
            display = split_text[1].split(" ")
        
            # Creates dict of dicts containing character to code and number to letter data
            key_set = {
                'chars': dict.fromkeys(characters, ''),
                'nums': dict.fromkeys(range(0,10), [])
            }

            # Steps 1-4) Solves for 1, 4, 7, and 8 (all unique character lengths)
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

            # v)    What 7 does not share with 1 is an 'a'
            key_set['chars']['a'] = [letter for letter in key_set['nums'][7] if letter not in key_set['nums'][1]][0]

            # vi)   2 is only # without an 'f'
            full_set = ''.join(keys)

            for c in characters:
                if full_set.count(c) == 9:
                    key_set['chars']['f'] = c
                    for sequence in keys:
                        if sequence.count(c) == 0:
                            key_set['nums'][2] = [*sequence]
                            break
                    break

            # vii)  1 has unknown ('c') and 'f' is known
            key_set['chars']['c'] = ''.join(key_set['nums'][1]).replace(key_set['chars']['f'], '')

            # viii) 5 digit sequence not containing a 'c' is a 5
            for k in keys:
                if len(k) == 5:
                    if k.count(key_set['chars']['c']) == 0:
                        key_set['nums'][5] = [*k]

            # ix)   Of 5 digit sequences (2,3,5) only 3 is unsolved
            for k in keys:
                if len(k) == 5:
                    if [*k] != key_set['nums'][5] and [*k] != key_set['nums'][2]:
                        key_set['nums'][3] = [*k]

            # 'e' only unknown left in 2 after cancelling out with 3 and removing knowns
            for c in key_set['nums'][2]:
                if c not in key_set['nums'][3]:
                    key_set['chars']['e'] = c
            

            # Assign 6 digit sequences to numbers
            for k in keys:
                if len(k) == 6:
                    if k.count(key_set['chars']['c']) == 0:
                        key_set['nums'][6] = [*k]
                    elif k.count(key_set['chars']['e']) == 0:
                        key_set['nums'][9] = [*k]
                    else:
                        key_set['nums'][0] = [*k]

            # 'd' is last character in 8 that isn't in 0
            for c in key_set['nums'][8]:
                if c not in key_set['nums'][0]:
                    key_set['chars']['d'] = c

            # 'b' is last unknown in 4 (c d f are knowns)
            for c in key_set['nums'][4]:
                knowns = [key_set['chars']['c'],key_set['chars']['d'],key_set['chars']['f']]
                if c not in knowns:
                    key_set['chars']['b'] = c

            # 'g' is last unknown in 8
            for c in key_set['nums'][8]:
                if c not in key_set['chars'].values():
                    key_set['chars']['g'] = c

            # read, decode, and store displays
            display_digits = ""
            for digit in display:
                digit_set = set([*digit])
                for k,v in key_set['nums'].items():
                    if len(digit_set - set(v)) == 0 and len(set(v) - digit_set) == 0:
                        display_digits = f"{display_digits}{k}"
                        if k == 1 or k == 4 or k == 7 or k == 8:
                            unique_digit_count_instances = unique_digit_count_instances + 1
            feed_data.append({'keys': keys, 'displays': {'encoded': display, 'decoded': int(display_digits)}, 'key_set': key_set})
            display_total = 0
            for feed in feed_data:
                display_total = display_total + feed['displays']['decoded']
            
        #print(feed_data)
        print(f"Total unique instances: {unique_digit_count_instances}")
        print(f"Decoded displays total: {display_total}")
if __name__ == "__main__":
    day8a.run()


"""
Ordered by segment count followed by alphabetical order of sequence
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