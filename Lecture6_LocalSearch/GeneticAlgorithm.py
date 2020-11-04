'''

Using a genetic algorithm to find the optimal solution or in this case the highest bit string of 3 bits

'''

import random
import math

p_mutation = 0.0
num_of_generations = 200

#Run the genetic algorithm a finite number of generation to try and find a viable solution
def genetic_algorithm(population, fitness_fn, minimal_fitness):

    #Run the mating procedure num_of_generations times
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        #Create new empty population
        new_population = set()

        #Foreach member in the current population, select to members to create a child from
        #Select from the population based on the a fitness function
        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            #Create child from mother and father
            child = reproduce(mother, father)

            #Sometime mutate the child inorder to counter local optimum
            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            #Add the new child to the population
            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        #Get the fittest individual
        fittest_individual = get_fittest_individual(population, fitness_fn)

        #If the fittest individual is as good or better as the minimal fitness value return that individual
        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


#Create a new child from a mother and a father
def reproduce(mother, father):

    motherList = []
    fatherList = []

    for interger in mother:
        motherList.append(interger)

    for integer in father:
        fatherList.append(integer)

    rn = random.randint(0,2)

    momSlice = motherList[rn]
    dadSlice = fatherList[rn]

    #Swap the slices
    motherList[rn] = dadSlice
    fatherList[rn] = momSlice

    boyOrGirl = random.randint(0, 1)

    if boyOrGirl == 0:
        return tuple(motherList)
    elif boyOrGirl == 1:
        return tuple(fatherList)

def mutate(individual):

    rn = random.randint(0, 2)

    indList = list(individual)

    if indList[rn] == 1:
        indList[rn] = 0
    else:
        indList[rn] = 1

    return tuple(indList)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)

    wheelOfFortunation = []

    for citizen in population:
        for i in range(0, int(fitness_fn(citizen))):
            wheelOfFortunation.append(citizen)

    mother = random.randint(0, len(wheelOfFortunation) - 1)
    father = random.randint(0, len(wheelOfFortunation) - 1)

    return wheelOfFortunation[mother], wheelOfFortunation[father]

    #return selected


def fitness_function(individual):
    index = 0
    fitness = 0

    for integer in enumerate(reversed(individual)):

        if integer[1] == 1:
            fitness += math.pow(2, index)
        index = index + 1

    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    #Defines the minimal fitness value accepted for a perfect speciment
    minimal_fitness = 64

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (1,0,1,0,0,1),
        (0,0,1,1,0,1),
        (1,0,0,0,1,1),
        (0,0,1,0,0,0),
        (0,0,0,0,1,0)
    }
    #initial_population = get_initial_population(3, 4)

    #Find the fittest geneticAlgorithm, take the initial population, the determing fitness function and the desired minimul fitness acceptable
    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


if __name__ == '__main__':
    pass
    main()
