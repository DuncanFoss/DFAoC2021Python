from lib.Utility import data_reader, derive_basename

class day6a:
    def run():
        ITERATION_LIMIT = 256
        iteration_count = 0
        fish_population = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        new_fish = 0
        # state = [3,4,3,1,2]
        state = data_reader(derive_basename(__file__))[0].split(',')

        for s in state:
            fish_population[int(s)] = fish_population[int(s)] + 1


        while iteration_count < ITERATION_LIMIT:
            new_fish = fish_population[0]
            roll_over = fish_population[0]
            fish_population[0] = fish_population[1]
            fish_population[1] = fish_population[2]
            fish_population[2] = fish_population[3]
            fish_population[3] = fish_population[4]
            fish_population[4] = fish_population[5]
            fish_population[5] = fish_population[6]
            fish_population[6] = fish_population[7] + roll_over
            fish_population[7] = fish_population[8]
            fish_population[8] = new_fish
            iteration_count = iteration_count + 1

            new_fish = 0

        print(f"Fish after {iteration_count} days:{sum(fish_population.values())}")


if __name__ == "__main__":
    day6a.run()