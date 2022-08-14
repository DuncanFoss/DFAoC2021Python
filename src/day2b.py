from lib import Utility


class day2b:
    def run():
        """
        bearing values
        bearing[0] = x coord
        bearing[1] = y coord
        bearing[2] = aim
        """
        source = Utility.data_reader(Utility.derive_basename(__file__))
        bearing = [0, 0, 0]

        for line in source:
            operator, value = line.split(" ")
            value = int(value)

            if operator == "forward":
                bearing[0] += value
                bearing[1] += value * bearing[2]
            elif operator == "up":
                bearing[2] -= value
            elif operator == "down":
                bearing[2] += value
            else:
                raise KeyError("Improper submarine movement. All hands lost.")

        print(
            f"Product of final x ({bearing[0]}) & y ({bearing[1]}) coordinates: "
            + f"{bearing[0]*bearing[1]}"
        )


if __name__ == "__main__":
    script = day2b()
    day2b.run()
