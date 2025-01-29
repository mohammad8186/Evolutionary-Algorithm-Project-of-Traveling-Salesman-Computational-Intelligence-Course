import random
from individual import Individual
from evaluation import evaluate_all
from selection import select_two_individual_for_crossover
from mutation import mutation1
from termination_condition import terminate1
from crossover import cross_over

def run_algorithm(distance_matrix, population_size=20, generation_size=30):
    MUTATION_RATE = 0.3
    best_fitness_list = []
    avg_fitness_list = []
    best_individual = None  # تغییر: تعریف بهترین فرد اولیه
    genome_size = len(distance_matrix)

    # Create primary population
    population = primary_population_creator(population_size, genome_size)

    prev_best_fitness = float('inf')  # برای تشخیص توقف زودهنگام

    # شمارش تعداد نسل‌ها
    iteration = 0
    
    while True:
        iteration += 1
        print(f"Generation: {iteration}")

        # Crossover
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            parent1, parent2 = select_two_individual_for_crossover(population, population_size)
            offspring = cross_over(parent1, parent2)
            generated_individuals.append(offspring)

        # Mutation
        for individual in generated_individuals:
            if random.random() < MUTATION_RATE:
                mutation1(individual)

        # Evaluate generated individuals
        evaluate_all(generated_individuals, distance_matrix)

        # Evaluate population as well
        evaluate_all(population, distance_matrix)

        # Select next generation
        population = next_generation_selection(population, generated_individuals)

        # Track the best fitness and check for early stopping
        current_best_fitness = best_fitness(population)
        best_fitness_list.append(current_best_fitness)
        avg_fitness_list.append(avg_fitness(population))

        # **تغییر: به‌روزرسانی بهترین فرد**
        current_best_individual = min(population, key=lambda x: x.fitness)
        if best_individual is None or current_best_individual.fitness < best_individual.fitness:
            best_individual = current_best_individual

        # چاپ وضعیت پیشرفت برای مشاهده بهتری از الگوریتم
        print(f"Best Fitness (Generation {iteration}): {current_best_fitness}")
        print(f"Average Fitness: {avg_fitness(population)}")

        if abs(prev_best_fitness - current_best_fitness) < 1e-6:  # تغییرات ناچیز در فیتنس
            print("Stopping early as fitness has not improved significantly.")
            break

        prev_best_fitness = current_best_fitness

        random.shuffle(population)
       
    return best_individual, best_fitness_list, avg_fitness_list


def primary_population_creator(population_size: int, genome_size: int) -> list[Individual]:
    population = []
    for _ in range(population_size):
        population.append(Individual(genome_size))
    return population

def avg_fitness(population:list[Individual]) -> float:
    return sum(individual.fitness for individual in population) / len(population)

def next_generation_selection(population, generated_individuals):
    # Combine current population and generated offspring
    combined_population = population + generated_individuals

    # Filter out individuals whose fitness is None (if any)
    combined_population = [ind for ind in combined_population if ind.fitness is not None]

    # Sort the population by fitness (descending order)
    combined_population.sort(key=lambda x: x.fitness, reverse=True)

    # Return the best 'population_size' individuals
    return combined_population[:len(population)]


def best_fitness(population:list[Individual]) -> float:
    return min(individual.fitness for individual in population)

