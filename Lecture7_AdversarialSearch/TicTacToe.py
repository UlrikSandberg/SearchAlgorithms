'''
Minimax decision tree
'''

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')

    action, newState = argmax(successors_of(state), lambda a: min_value(a[1]))

    return action


def is_terminal(state):

    if utility_of(state) == 0:
        for i in state:
            if (i != "X" and i != "O"):
                return False
    return True


def utility_of(state):

    WinnerHasBeenFound = False
    result = 0

    xWinner = ("X", "X", "X")
    oWinner = ("O", "O", "O")

    for c in [0, 3, 6]:

        horizontal = []
        horizontal.append(state[c + 0])
        horizontal.append(state[c + 1])
        horizontal.append(state[c + 2])

        horTuple = tuple(horizontal)

        if horTuple == xWinner:
            result = 1
            WinnerHasBeenFound = True
        elif horTuple == oWinner:
            result = -1
            WinnerHasBeenFound = True

    if not WinnerHasBeenFound:
        for x in [0, 1, 2]:
            vertical = []
            vertical.append(state[x + 0])
            vertical.append(state[x + 3])
            vertical.append(state[x + 6])

            verTuple = tuple(vertical)

            if verTuple == xWinner:
                result = 1
                WinnerHasBeenFound = True
            elif verTuple == oWinner:
                result = -1
                WinnerHasBeenFound = True

    if not WinnerHasBeenFound:

        diagonal1 = []
        diagonal2 = []
        diagonal1.append(state[0])
        diagonal1.append(state[4])
        diagonal1.append(state[8])
        diagonal2.append(state[2])
        diagonal2.append(state[4])
        diagonal2.append(state[6])

        diaTup1 = tuple(diagonal1)
        diaTup2 = tuple(diagonal2)

        if diaTup1 == xWinner:
            result = 1
        elif diaTup1 == oWinner:
            result = -1

        if diaTup2 == xWinner:
            result = 1
        elif diaTup2 == oWinner:
            result = -1

    return result

def successors_of(state):

    list = []
    player = ""
    numberOfTurns = 0
    for i in state:
        if(i == "X" or i == "O"):
            numberOfTurns += 1

    if numberOfTurns % 2 == 0:
        #Do player turns
        player = "X"
    else:
        #Do enemy AI turns
        player = "O"


    index = -1
    for i in state:
        index = index + 1
        if i != "X" and i != "O":
            move = []
            for x in state:
                move.append(x)

            move[index] = player

            tup = (index, move)

            list.append(tup)

    return list

def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    display(board)
    #board[int(input('Your move? '))] = 'O'
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
