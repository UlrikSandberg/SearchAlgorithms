def alpha_beta_decision(state):
    infinity = float('inf')

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity

        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(
        successors_of(state),
        lambda a: min_value(a, infinity, -infinity))
    return state


def is_terminal(state):

    for i in state:
        if i not in [1, 2]:
            return False
    return True

def utility_of(state):

    turn = len(state) % 2

    if turn == 0:
        #AI turn
        if is_terminal(state):
            return -1
    else:
        #Player turn
        if is_terminal(state):
            return 1

    return 0

def successors_of(state):

    #Calculate the all new states. This is effectively all subsets if the state iteratively -1 until it is == (state / 2) or == 0
    succesors = []

    index = 0
    for i in state:
        if isValidForSplit(i):
            #This means that the value is above 2 in which case it can be split into a subset of none equal size
            copy = state[:]
            valueToBeSpllited = copy[index]
            del copy[index]

            possibleConfiguration = []

            #Split the value and append to the copied array.
            subsetA = valueToBeSpllited
            subsetB = 0
            while (subsetA - subsetB) - 1 > valueToBeSpllited / 2:
                subsetB += 1
                possibleConfiguration.append([subsetA - subsetB, subsetB])

            for i in possibleConfiguration:
                newState = copy[:]
                for j in i:
                    newState.append(j)
                succesors.append(newState)
        index += 1

    return succesors

def isValidForSplit(value):
    return value > 2

def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = alpha_beta_decision(state)

    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [7]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))

    if len(state) % 2 == 0:
        print "Player wins!"
    else:
        print "Ai wins!"


if __name__ == '__main__':
    main()
