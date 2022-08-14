from lib.Utility import data_reader, derive_basename

class day7a:
    def run():
        source = list(map(int, data_reader(derive_basename(__file__))[0].split(',')))
    
        MAX_POSITION = max(source)
        position = MAX_POSITION
        linear_fuel_costs = {}
        scaling_fuel_costs = {}

        while position >= 0:
            linear_fuel_costs[position] = 0
            scaling_fuel_costs[position] = 0
            for s in source:
                abs_val = abs(position - s)
                linear_fuel_costs[position] = linear_fuel_costs[position] + abs_val
                scaling_fuel_costs[position] = scaling_fuel_costs[position] + sum(range(1,abs_val + 1))
            position = position - 1

        print(f"Single fuel unit per move result: {min(linear_fuel_costs.items(), key = lambda data: data[1])}")
        print(f"Scaling fuel cost per unit result: {min(scaling_fuel_costs.items(), key = lambda data: data[1])}")

if __name__ == "__main__":
    day7a.run()
