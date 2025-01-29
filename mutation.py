from individual import Individual
import random

def mutation1(individual: Individual):
    genome_length = len(individual)
    # Step 1: Randomly select two positions in the genome
    idx1, idx2 = random.sample(range(genome_length), 2)

    # Step 2: Swap the two genes
    individual.genome[idx1], individual.genome[idx2] = individual.genome[idx2], individual.genome[idx1]
