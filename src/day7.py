from lib.Utility import data_reader, derive_basename

class day7a:
    def run():
        source = list(map(int, data_reader(derive_basename(__file__))[0].split(',')))
    
        MAX_POSITION = max(source)
        position = MAX_POSITION
        fuel_costs = {}

        while position >= 0:
            fuel_costs[position] = 0

            for s in source:
                fuel_costs[position] = fuel_costs[position] + abs(position - s)
            position = position - 1

        print(f"RESULT: {min(fuel_costs.items(), key = lambda data: data[1])}")

if __name__ == "__main__":
    day7a.run()
