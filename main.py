from service.genetic_algorithm import GeneticAlgorithm
import logging
import numpy as np

def best_result_expected(ga: GeneticAlgorithm):
    return np.abs(ga.final_position - ga.initial_position) + ga.individual_size
    

def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
    ga = GeneticAlgorithm(individual_size=10, initial_population_size=100)
    logging.info(f'Best result expected: {best_result_expected(ga)}')
    bests = ga.run(cross_rate=0.8, mutation_rate=0.1, max_generations=300, max_generations_without_improvement=10, death_rate=0.2, n_returning_individuals=10)
    logging.info(f'The best result with {bests[0].fitness} fitness: {bests[0].path}')
main()