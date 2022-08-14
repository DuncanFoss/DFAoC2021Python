from lib import Utility


class day1a:
    def run():
        source = Utility.data_reader(Utility.derive_basename(__file__))
        holder = None
        count = 0

        for i, line in enumerate(source):
            if holder is not None:
                if holder < int(line):
                    count += 1
            holder = int(line)

        print(f"Increment count: {count}")


if __name__ == "__main__":
    script = day1a()
    day1a.run()
