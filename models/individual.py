import numpy as np
import logging

class Individual:
    def __init__(self, path: list[int], initial_position: int, final_position: int):
        if(len(path) == 0):
            raise ValueError("The path must have at least one value")

        self.path = path
        self.path_size = len(path)
        self.initial_position = initial_position
        self.final_position = final_position
        self.muteted = False
        self.fitness = self.get_fitness()

    def get_fitness(self):                
        distance = 1 + np.abs(self.path[0] - self.initial_position)
        for position in range(1, self.path_size):
            distance += 1 + np.abs(self.path[position - 1] - self.path[position])
        distance += np.abs(self.path[-1] - self.final_position)
        return distance

    def combine(self, other: 'Individual', mutation_rate: float) -> list['Individual']:
        crossover_point = int(len(self.path) / 2)

        first_child_path = np.concatenate((self.path[:crossover_point], other.path[crossover_point:]))        
        first_child = Individual(first_child_path, self.initial_position, self.final_position)
        if(self.__should_mutate__(mutation_rate)):
            first_child.mutate()

        second_child_path = np.concatenate((other.path[:crossover_point], self.path[crossover_point:]))        
        second_child = Individual(second_child_path, self.initial_position, self.final_position)
        if(self.__should_mutate__(mutation_rate)):
            second_child.mutate()

        return [first_child, second_child]

    def mutate(self) -> 'Individual':
        mutation_point = np.random.randint(0, self.path_size - 1)
        self.path[mutation_point] = np.random.randint(0, self.path_size - 1)
        self.muteted = True
        return self

    def __should_mutate__(self, mutation_rate: float) -> bool:
        return np.random.random() <= mutation_rate
    