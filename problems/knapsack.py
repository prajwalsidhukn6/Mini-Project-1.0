from algorithms.genetic import Genome
from collections import namedtuple

# Declaration of thing tuple
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

# Initialized the things details manually
example = [
                     Thing('Laptop', 500, 2200),
                     Thing('Headphones', 150, 160),
                     Thing('Coffee Mug', 60, 350),
                     Thing('Notepad', 40, 333),
                     Thing('Water Bottle', 30, 192),
                     Thing('Mints', 5, 25),
                     Thing('Socks', 10, 38),
                     Thing('Tissues', 15, 80),
                     Thing('Phone', 500, 200),
                     Thing('Baseball Cap', 100, 70)
            ]
example1 = [
                     Thing('Laptop', 500, 1200),
                     Thing('Headphones', 150, 260),
                     Thing('Coffee Mug', 60, 250),
                     Thing('Notepad', 40, 433),
                     Thing('Water Bottle', 30, 192),
                     Thing('Mints', 5, 250),
                     Thing('Socks', 10, 380),
                     Thing('Tissues', 15, 180),
                     Thing('Phone', 500, 28000),
                     Thing('Baseball Cap', 100, 700)
            ]



# Generated things list automatically
def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num + 1)]

# Get fittest score of the genome list from things
def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value
            if weight > weight_limit:
                return 0
    return value

# Selecting things if genome is 1 in the list (Genome List)
def from_genome(genome: Genome, things: [Thing]) -> [Thing]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]
    return result

# forms a string of thing
def to_string(things: [Thing]):
    return f"[{', '.join([t.name for t in things])}]"

# Get maximized cost of the genome list
def value(things: [Thing]):
    return sum([t.value for t in things])

# Calculate sum of weight of the list items
def weight(things: [Thing]):
    return sum([p.weight for p in things])

# print stats
def print_stats(things: [Thing]):
    print(f"Selected Things: {to_string(things)}")
    print(f"Maximized Value: {value(things)} Rs")
    print(f"Total Weight: {weight(things)} kg")