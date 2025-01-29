import numpy as np

def create_distance_matrix(input_path: str):
    # Step 1: Read the coordinates from the file
    cities = []
    with open(input_path, 'r') as file:
        for line in file.readlines():
            x, y = map(int, line.strip().split(','))
            cities.append((x, y))

    # Step 2: Create the distance matrix using Euclidean distance
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                distance_matrix[i][j] = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance_matrix
