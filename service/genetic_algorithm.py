from models.individual import Individual
from models.population import Population
import logging

class GeneticAlgorithm:
    def __init__(self, individual_size: int = 10, initial_population_size: int = 100, max_individuals_rate: int = 100) -> None:
        logging.info('Configurating genetic algorithm...')
        self.max_individuals = initial_population_size * max_individuals_rate
        self.population = Population(individual_size, initial_population_size, self.max_individuals)        
        self.initial_position = self.population.initial_position
        self.final_position = self.population.final_position
        self.individual_size = self.population.individual_size
        self.results = []
        self.final_individuals_count = 0
        logging.info(f'Initial position: {self.initial_position}')
        logging.info(f'Final position: {self.final_position}')
        logging.info(f'Individual size: {self.individual_size}')

    def run(self, cross_rate: float = 0.8, mutation_rate: float = 0.1, max_generations: int = 300, max_generations_without_improvement: int = 10, death_rate: float = 0.1, n_returning_individuals: int = 10) -> list[Individual]:
        logging.info('Running genetic algorithm...')
        while(self.__should_continue__(max_generations, max_generations_without_improvement)):
            mutated_before = self.population.count_mutations()
            n_created = self.population.cross_population(cross_rate, mutation_rate)            
            mutated_after = self.population.count_mutations()
            mutations = mutated_after - mutated_before
            logging.info(f'Generation {self.population.generation} created {n_created} individuals with {mutations} mutations.')

            n_killed = self.population.kill_worst(death_rate)
            best_fitness = self.population.current_best_fitness
            self.results.append(best_fitness)
            logging.info(f'Generation {self.population.generation} killed {n_killed} individuals')
            logging.info(f'Generation {self.population.generation} best fitness: {best_fitness}')
            logging.info(f'Generations without improvement: {self.population.generations_without_improvement}')

        self.final_individuals_count = self.population.get_size()
        logging.info(f'Process finished with {self.population.generation} generations and {self.final_individuals_count} individuals.')
        return self.population.get_bests(n_returning_individuals)
            

    def __should_continue__(self, max_generations: int, max_generations_without_improvement: int):
        return self.population.generation < max_generations and self.population.generations_without_improvement < max_generations_without_improvement