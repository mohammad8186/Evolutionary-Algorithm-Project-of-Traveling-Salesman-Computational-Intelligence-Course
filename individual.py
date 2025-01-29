from numpy import random

class Individual:
    """
    This class is an abstraction of an individual which contains two attributes:
    1- genome: a list of genes (e.g. [0,1,2] for a genome with length 3)
    2- fitness: fitness value of the individual
    """

    def __init__(self, genome_length=30, generate_random_genome=True, genome=None) -> None:
        if genome is not None:
            # Allow custom genome to be passed
            self.genome = genome
        elif generate_random_genome:
            self.genome = _generate_uniform_random_permutation([x for x in range(genome_length)])
        else:
            self.genome = None
        
        self.fitness = None

    def __len__(self):
        return len(self.genome)

    def __str__(self) -> str:
        return f"fitness: {self.fitness}\nvalue: {self.genome}\n"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        return self.genome == value.genome


def _generate_uniform_random_permutation(valid_delivery_spots):
    return random.permutation(valid_delivery_spots).tolist()
