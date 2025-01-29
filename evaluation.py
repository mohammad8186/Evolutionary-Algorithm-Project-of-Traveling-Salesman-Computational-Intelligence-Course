from individual import Individual

def evaluate_all(individual_list: list[Individual], distance_matrix: list[list[float]]):
    for individual in individual_list:
        evaluate(individual, distance_matrix)

def evaluate(individual: Individual, distance_matrix: list[list[float]]):
    """
    This method computes fitness (based on the TSP problem) and updates the fitness attribute of the individual parameter (individual.fitness=new_fitness)
    """
    # Compute the total distance for the path represented by the genome of the individual
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distance_matrix[individual.genome[i]][individual.genome[i + 1]]
    total_distance += distance_matrix[individual.genome[-1]][individual.genome[0]]  # Return to the starting city

    # Update fitness of the individual (inverse of distance, since lower distance means better fitness)
    individual.fitness = 1 / total_distance if total_distance != 0 else float('inf')
