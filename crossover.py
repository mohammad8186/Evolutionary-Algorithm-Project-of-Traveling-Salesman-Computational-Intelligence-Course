from individual import Individual
import random

def cross_over(parent1: Individual, parent2: Individual):
    genome_length = len(parent1)
    # Step 1: Randomly select a crossover point
    crossover_point_1 = random.randint(0, genome_length - 1)
    crossover_point_2 = random.randint(crossover_point_1, genome_length)

    # Step 2: Create offspring by combining segments from both parents
    offspring_genome = [None] * genome_length

    # Step 3: Copy a segment from the first parent
    offspring_genome[crossover_point_1:crossover_point_2] = parent1.genome[crossover_point_1:crossover_point_2]

    # Step 4: Fill the remaining positions with genes from the second parent
    current_position = 0
    for gene in parent2.genome:
        if gene not in offspring_genome:
            while offspring_genome[current_position] is not None:
                current_position += 1
            offspring_genome[current_position] = gene

    # Step 5: Return the offspring individual
    return Individual(genome_length, generate_random_genome=False, genome=offspring_genome)
