from individual import Individual
import random

def select_two_individual_for_crossover(individual_list: list[Individual], population_size: int) -> tuple[Individual, Individual]:
    # Step 1: Randomly select two individuals from the population
    ind1 = random.choice(individual_list)
    ind2 = random.choice(individual_list)

    # Step 2: Return the two selected individuals
    return ind1, ind2
