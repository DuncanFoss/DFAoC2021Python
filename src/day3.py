from lib import Utility


class day3a:
    def run():
        source = Utility.data_reader(Utility.derive_basename(__file__))
        data = {"g": "", "e": ""}
        digit_counts = [0] * len(source[0])

        # Counts occurences of '1' digits in a binary string
        for line in source:
            for i, b in enumerate(line):
                if int(b) == 1:
                    digit_counts[i] += 1

        for count in digit_counts:
            if count > (len(source) / 2):
                data["g"] = f"{data['g']}1"
            else:
                data["g"] = f"{data['g']}0"

        print(f"Common digit binary: {data['g']}")
        # creates bit flipped copy of the binary sequence stored in data["e"]
        for i, digit in enumerate(data["g"]):
            data["e"] = data["e"] + "0" if data["g"][i] == "1" else data["e"] + "1"

        print(f"Product of g * e: {int(data['g'], 2) * int(data['e'], 2)}")


if __name__ == "__main__":
    script = day3a()
    day3a.run()
