from functools import partial
from problems import knapsack
from algorithms import bruteforce, genetic
from utils.analyze import timer

print("\n0/1 Knapsack Packing")

things = knapsack.generate_things(50)
#things = knapsack.example

# show available items
print("\nAvailable Items :   (Name, Value, Weight)\n")
for var in things:
	print(f"\t\t\t\t\t{var.name,var.value,var.weight}")

weight_limit = 3000

print("\nKnapsack Weight Limit: %d kg" % weight_limit)
# print("")
# print("BRUTEFORCE")
# print("----------")

#with timer():
result = bruteforce(things, weight_limit)

#knapsack.print_stats(result[1])

print("")
print("GENETIC ALGORITHM")
print("-------------")

# Perform evolution
with timer():
	population, generations = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)),
		fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
		fitness_limit=result[0],
		generation_limit=100
	)

# formed things list packed into knapsack
sack = knapsack.from_genome(population[0], things)
knapsack.print_stats(sack)

# print genome
print("")
print("GENOME")
print("------")
print(population[0])