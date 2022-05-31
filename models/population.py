import logging
import numpy as np
from models.individual import Individual

class Population:
    def __init__(self, individual_size: int, initial_population_size: int, max_indivduals: int) -> None:
        self.individual_size = individual_size
        self.initial_size = initial_population_size
        self.max_individuals = max_indivduals
        self.initial_position = np.random.randint(0, self.individual_size - 1)
        self.final_position = np.random.randint(0, self.individual_size - 1)
        self.individuals = []
        self.generation = 0
        self.generations_without_improvement = 0
        self.current_best_fitness = np.inf
        self.initialize()

    def initialize(self) -> None:
        for _ in range(self.initial_size):
            individual_path = np.random.randint(0, self.individual_size -1, self.individual_size)
            self.individuals.append(Individual(individual_path, self.initial_position, self.final_position))
        self.current_best_fitness = self.get_best_individual().fitness

    def get_best_individual(self) -> Individual:
        return min(self.individuals, key=lambda individual: individual.fitness)

    def get_size(self) -> int:
        return len(self.individuals)

    def cross_population(self, cross_rate: float, mutation_rate: float) -> None:
        to_cross_individuals = self.__select_to_cross__(cross_rate)
        first, second = self.__create_pairs__(to_cross_individuals)
        initial_count = self.get_size()
        
        for individual1, individual2 in zip(first, second):
            new_children = self.__combine_individuals__(individual1, individual2, mutation_rate)
            self.individuals.extend(new_children)
        
        self.generation += 1
        new_best = self.get_best_individual().fitness

        if(new_best == self.current_best_fitness):
            self.generations_without_improvement += 1
        else:
            self.current_best_fitness = new_best
            self.generations_without_improvement = 0

        self.cataclysm()
        final_count = self.get_size()
        return final_count - initial_count

    def kill_worst(self, rate: float) -> None:
        n_individuals = int(self.get_size() * rate)
        self.individuals = sorted(self.individuals, key=lambda individual: individual.fitness)
        self.individuals = self.individuals[:self.get_size() - n_individuals]
        return n_individuals

    def cataclysm(self):
        if(self.get_size() > self.max_individuals):            
            self.individuals = sorted(self.individuals, key=lambda individual: individual.fitness)
            self.individuals = self.individuals[:self.max_individuals]
            logging.info("Population cataclysm")

    def get_bests(self, n = 10):
        return sorted(self.individuals, key=lambda individual: individual.fitness)[:n]

    def count_mutations(self) -> int:
        return len([i for i in self.individuals if i.muteted == True])

    def __select_to_cross__(self, cross_rate: float) -> list[Individual]:
        n_individuals = int(self.get_size() * cross_rate)
        return np.random.choice(self.individuals, n_individuals, replace=False)

    def __create_pairs__(self, selected_individuals: list[Individual]) -> list[Individual]:        
        np.random.shuffle(selected_individuals)
        half = int(len(selected_individuals) / 2)
        first =  selected_individuals[:half]
        second = selected_individuals[half:]        
        return (first, second)
        
    def __combine_individuals__(self, individual1:Individual, individual2:Individual, mutation_rate: float)-> list[Individual]:        
        return individual1.combine(individual2, mutation_rate)    