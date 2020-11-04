import random
import math

p_mutation = 0.2
num_of_generations = 30

def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if(fittest_individual == (1,3,0,2)):
            print ""

        if minimal_fitness >= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):

    motherList = list(mother)
    fatherList = list(father)

    #Generate slices... Take the range

    momSlice = motherList[0]
    dadSlice = fatherList[0]

    motherList[0] = dadSlice
    fatherList[0] = momSlice

    boyOrGirl = random.randint(0, 1)

    if boyOrGirl == 0:
        return tuple(motherList)
    elif boyOrGirl == 1:
        return tuple(fatherList)

def mutate(individual):

    rnCol = random.randint(0, 3)

    mutation = random.randint(0, 3)

    indList = list(individual)

    indList[rnCol] = mutation

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

    coordinates = []

    if(individual == (1,3,0,2)):
        print ""

    coordinateCol = 0
    for coor in individual:
        coordinates.append((coordinateCol, coor))
        coordinateCol = coordinateCol + 1

    conflicts = 0

    numbers = [0,0,0,0]

    for int in individual:
        numbers[int] = numbers[int] + 1

    # Check - Each row
    for number in numbers:
        if number != 0:
            conflicts = conflicts + number - 1

    # Check diagonals
    index = 0
    conflictPaths = []

    for coordinate in individual:

        #Run at the southeast diagonal line until we encounter a conflict or we go out of bounds
        SECol = index
        SERow = coordinate

        southEastConflictPath = []
        didEncounterConflict = False
        southEastConflictPath.append((SECol, SERow))
        while SECol < 4 and SERow < 4:
            SECol = SECol + 1
            SERow = SERow + 1

            southEastConflictPath.append((SECol, SERow))

            if coordinates.__contains__((SECol, SERow)):
                conflicts = conflicts + 1
                break

        #If didEncounterConflict we should add the conflict path to the conflictPath so that it may be recorded as a conflict path

        #Run at the southWest diagonal line until we encounter a conflict or we go out of bounds
        SWCol = index
        SWRow = coordinate

        southWestConflictPath = []
        SWDidEncounterConflict = False
        southWestConflictPath.append((SWCol, SWRow))

        while SWCol >= 0 and SWRow < 4:
            SWCol = SWCol - 1
            SWRow = SWRow + 1

            southWestConflictPath.append((SWCol, SWRow))

            if coordinates.__contains__((SWCol, SWRow)):
                conflicts = conflicts + 1
                break

        index = index + 1

    return conflicts


def get_fittest_individual(iterable, func):
    return min(iterable, key=func)


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
    minimal_fitness = 0

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (0, 1, 2, 3),
        (3, 2, 1, 0),
        (0, 0, 1, 1),
        (1, 1, 0, 0)
    }
    #initial_population = get_initial_population(3, 4)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


if __name__ == '__main__':
    pass
    main()
