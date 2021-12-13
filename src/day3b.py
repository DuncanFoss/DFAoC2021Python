from lib import Utility


class day3b:
    def run():
        def sort_list(common_val: bool = True):
            digit_check = 0

            source["presort"] = source["original"]
            while len(source["presort"]) > 1:
                digit_count = 0
                chosen_value = "1"
                # count occurences of digit
                for line in source["presort"]:
                    if line[digit_check] == "1":
                        digit_count += 1

                if digit_count < len(source["presort"]) / 2:
                    chosen_value = "0"

                for line in source["presort"]:
                    if common_val:
                        if line[digit_check] == chosen_value:
                            source["postsort"].append(line)
                    else:
                        if line[digit_check] != chosen_value:
                            source["postsort"].append(line)

                if len(source["postsort"]) > 1:
                    source["presort"] = source["postsort"]
                    source["postsort"] = []
                else:
                    return source["postsort"].pop()

                digit_check += 1

        # end of sort_list

        source: dict[str, list] = {
            "original": Utility.file_reader(Utility.derive_basename(__file__)),
            "presort": [],
            "postsort": [],
        }
        bins: dict[str, str] = {"o": [], "c": []}

        bins["o"] = sort_list()
        bins["c"] = sort_list(False)

        print(f"OXYGEN BINARY: {bins['o']}")
        print(f"CO2 BINARY: {bins['c']}")
        print(f"Product of o * c: {int(bins['o'], 2) * int(bins['c'], 2)}")


if __name__ == "__main__":
    script = day3b()
    day3b.run()
