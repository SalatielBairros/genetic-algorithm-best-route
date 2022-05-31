# Genetic Algorithm for best route

## The problem
Imagine there is a rat in the first line of a matrix and a cheese in the last line, both randomly positioned. The rat only move forward, up and down and the room is a square. Use a genetic algorithm to find the shortest route to get the cheese.

## Codificating the problem
For performance reasons, the problem is codificated using a single dimenson array instead of a matrix. Since the room is a square, the array is a square of size N representing the size of the room and the value of each cell is the row of that path.

|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |  C  |
|     |     |&#124;|----|-----|-----|-----|-----|-----|&#124;|
|     |     |&#124;|    |     |     |     |     |     |     |
|     |     |&#124;|    |     |     |     |     |     |     |
|  R  |-----|&#124;|    |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |

The path above can has initial position (the rat) equals to 7 and final position (the cheese) equals to 3. The path is represented by an array of size 10 as follows:
```
[7, 7, 4, 4, 4, 4, 4, 4, 4, 4]
```

## Calculating the fitness
Each column of the array represents one step foward and the value of each cell is the row of the next step, so the fitness calculation can be represented as:

$$\sum_{i=0}^{n-2} |p[i] - p[i + 1]| + 1$$

The python implementation of the fitness calculation is:

```python
    def get_fitness(self):                
        distance = 1 + np.abs(self.path[0] - self.initial_position)
        for position in range(1, self.path_size):
            distance += 1 + np.abs(self.path[position - 1] - self.path[position])
        distance += np.abs(self.path[-1] - self.final_position)
        return distance
```

## Crossing rules
The rules applied to cross the individuals (routes) are:

1. For the selected individuals to cross, divide the array in two parts randomly.
2. Create pairs of individuals with the two arrays.
3. For each pair, select the middle position.
4. Swap the two arrays from the middle position to the end, creating two derived individuals.
5. Apply a mutation rule to the derived individuals.

## Parameters

| Parameter | Location | Default | Description |
|-----------|----------|---------|-------------|
| initial_population_size | `GeneticAlgorithm` | `100` | The initial size of the population. |
| individual_size | `GeneticAlgorithm` | `10` | The size of the room. |
| cross_rate | `GeneticAlgorithm.run()` | `0.8` | Defines the proportion of the population that will reproduce. |
| mutation_rate | `GeneticAlgorithm.run()` | `0.8` | Defines the proportion of the derived individuals that will mutate. |
| max_generations | `GeneticAlgorithm.run()` | `300` | Max iterations (generations) to solve the problem. |
| max_generations_without_improvement | `GeneticAlgorithm.run()` | `10` | Defines how many generations without improvments of the best individual to stop the search. |
| death_rate | `GeneticAlgorithm.run()` | `0.2` | The proportion of individuals to die in each iteration. |
| n_returning_individuals | `GeneticAlgorithm.run()` | `10` | N best individuals to return at the end. |

## Runnnig

To run this example:
```bash
python main.py
```
### Output sample
```javascript
21:03:28: Configurating genetic algorithm...
21:03:28: Initial position: 7
21:03:28: Final position: 3
21:03:28: Individual size: 10
21:03:28: Best result expected: 14
21:03:28: Running genetic algorithm...
21:03:28: Generation 1 created 80 individuals with 6 mutations.
21:03:28: Generation 1 killed 36 individuals
21:03:28: Generation 1 best fitness: 22
21:03:28: Generations without improvement: 0
21:03:28: Generation 2 created 114 individuals with 13 mutations.
21:03:28: Generation 2 killed 51 individuals
21:03:28: Generation 2 best fitness: 20
21:03:28: Generations without improvement: 0
21:03:28: Generation 3 created 164 individuals with 13 mutations.
21:03:28: Generation 3 killed 74 individuals
21:03:28: Generation 3 best fitness: 20
21:03:28: Generations without improvement: 1
21:03:28: Generation 4 created 236 individuals with 24 mutations.
21:03:28: Generation 4 killed 106 individuals
21:03:28: Generation 4 best fitness: 20
21:03:28: Generations without improvement: 2
21:03:28: Generation 5 created 340 individuals with 35 mutations.
21:03:28: Generation 5 killed 153 individuals
21:03:28: Generation 5 best fitness: 20
21:03:28: Generations without improvement: 3
21:03:28: Generation 6 created 490 individuals with 60 mutations.
21:03:28: Generation 6 killed 220 individuals
21:03:28: Generation 6 best fitness: 20
21:03:28: Generations without improvement: 4
21:03:28: Generation 7 created 706 individuals with 70 mutations.
21:03:28: Generation 7 killed 318 individuals
21:03:28: Generation 7 best fitness: 20
21:03:28: Generations without improvement: 5
21:03:28: Generation 8 created 1016 individuals with 102 mutations.
21:03:28: Generation 8 killed 457 individuals
21:03:28: Generation 8 best fitness: 18
21:03:28: Generations without improvement: 0
21:03:28: Generation 9 created 1464 individuals with 144 mutations.
21:03:28: Generation 9 killed 659 individuals
21:03:28: Generation 9 best fitness: 18
21:03:28: Generations without improvement: 1
21:03:28: Generation 10 created 2108 individuals with 220 mutations.
21:03:28: Generation 10 killed 948 individuals
21:03:28: Generation 10 best fitness: 18
21:03:28: Generations without improvement: 2
21:03:28: Generation 11 created 3036 individuals with 302 mutations.
21:03:28: Generation 11 killed 1366 individuals
21:03:28: Generation 11 best fitness: 18
21:03:28: Generations without improvement: 3
21:03:28: Generation 12 created 4372 individuals with 436 mutations.
21:03:28: Generation 12 killed 1967 individuals
21:03:28: Generation 12 best fitness: 18
21:03:28: Generations without improvement: 4
21:03:29: Population cataclysm
21:03:29: Generation 13 created 2129 individuals with 234 mutations.
21:03:29: Generation 13 killed 2000 individuals
21:03:29: Generation 13 best fitness: 16
21:03:29: Generations without improvement: 0
21:03:29: Population cataclysm
21:03:29: Generation 14 created 2000 individuals with 232 mutations.
21:03:29: Generation 14 killed 2000 individuals
21:03:29: Generation 14 best fitness: 16
21:03:29: Generations without improvement: 1
21:03:29: Population cataclysm
21:03:29: Generation 15 created 2000 individuals with 148 mutations.
21:03:29: Generation 15 killed 2000 individuals
21:03:29: Generation 15 best fitness: 16
21:03:29: Generations without improvement: 2
21:03:29: Population cataclysm
21:03:29: Generation 16 created 2000 individuals with 209 mutations.
21:03:29: Generation 16 killed 2000 individuals
21:03:29: Generation 16 best fitness: 16
21:03:29: Generations without improvement: 3
21:03:29: Population cataclysm
21:03:29: Generation 17 created 2000 individuals with 173 mutations.
21:03:29: Generation 17 killed 2000 individuals
21:03:29: Generation 17 best fitness: 16
21:03:29: Generations without improvement: 4
21:03:29: Population cataclysm
21:03:29: Generation 18 created 2000 individuals with 204 mutations.
21:03:29: Generation 18 killed 2000 individuals
21:03:29: Generation 18 best fitness: 16
21:03:29: Generations without improvement: 5
21:03:29: Population cataclysm
21:03:29: Generation 19 created 2000 individuals with 213 mutations.
21:03:29: Generation 19 killed 2000 individuals
21:03:29: Generation 19 best fitness: 14
21:03:29: Generations without improvement: 0
21:03:30: Population cataclysm
21:03:30: Generation 20 created 2000 individuals with 209 mutations.
21:03:30: Generation 20 killed 2000 individuals
21:03:30: Generation 20 best fitness: 14
21:03:30: Generations without improvement: 1
21:03:30: Population cataclysm
21:03:30: Generation 21 created 2000 individuals with 217 mutations.
21:03:30: Generation 21 killed 2000 individuals
21:03:30: Generation 21 best fitness: 14
21:03:30: Generations without improvement: 2
21:03:30: Population cataclysm
21:03:30: Generation 22 created 2000 individuals with 208 mutations.
21:03:30: Generation 22 killed 2000 individuals
21:03:30: Generation 22 best fitness: 14
21:03:30: Generations without improvement: 3
21:03:30: Population cataclysm
21:03:30: Generation 23 created 2000 individuals with 191 mutations.
21:03:30: Generation 23 killed 2000 individuals
21:03:30: Generation 23 best fitness: 14
21:03:30: Generations without improvement: 4
21:03:30: Population cataclysm
21:03:30: Generation 24 created 2000 individuals with 180 mutations.
21:03:30: Population cataclysm
21:03:30: Generation 27 created 2000 individuals with 205 mutations.
21:03:30: Generation 27 killed 2000 individuals
21:03:30: Generation 27 best fitness: 14
21:03:30: Generations without improvement: 8
21:03:31: Population cataclysm
21:03:31: Generation 28 created 2000 individuals with 204 mutations.
21:03:31: Generation 28 killed 2000 individuals
21:03:31: Generation 28 best fitness: 14
21:03:31: Generations without improvement: 9
21:03:31: Population cataclysm
21:03:31: Generation 29 created 2000 individuals with 171 mutations.
21:03:31: Generation 29 killed 2000 individuals
21:03:31: Generation 29 best fitness: 14
21:03:31: Generations without improvement: 10
21:03:31: Process finished with 29 generations and 8000 individuals.
21:03:31: The best result with 14 fitness: [7 7 4 4 4 4 4 4 4 4]
```

## Improvements to make

1. Apply paralelism to the genetic algorithm
2. Add configurations
3. Add a way to save the best result
4. Plot the results