from lib import Utility


class day2a:
    def run():
        source = Utility.data_reader(Utility.derive_basename(__file__))
        coord = [0, 0]

        for line in source:
            operator, value = line.split(" ")
            value = int(value)

            if operator == "forward":
                coord[0] += value
            elif operator == "up":
                coord[1] -= value
            elif operator == "down":
                coord[1] += value
            else:
                raise KeyError("Improper submarine movement. All hands lost.")

        print(
            f"Product of final x ({coord[0]}) & y ({coord[1]}) coordinates:"
            + f"{coord[0]*coord[1]}"
        )


if __name__ == "__main__":
    script = day2a()
    day2a.run()
