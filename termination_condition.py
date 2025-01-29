def terminate1(individual_list) -> bool:
    BEST_FITNESS = -423.741  # The most optimal solution in terms of distance (negative because fitness is reversed)
    # Step 1: Check if any individual has reached the best fitness value
    for individual in individual_list:
        if individual.fitness <= BEST_FITNESS:
            return True
    return False
