from lib import Utility


class day1b:
    def run():
        source = Utility.file_reader(Utility.derive_basename(__file__))
        holders = []
        watermark = None
        _window = 3
        count = 0

        for i, line in enumerate(source):
            if len(holders) == _window:
                holders.pop(0)
            holders.append(int(line))

            if watermark is not None and len(holders) == _window:
                if watermark < Utility.add_list(holders):
                    count += 1

            if len(holders) == _window:
                watermark = Utility.add_list(holders)

        print(f"Increment count: {count}")


if __name__ == "__main__":
    script = day1b()
    day1b.run()
