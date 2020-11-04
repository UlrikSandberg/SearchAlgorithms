'''

Greedy Best first is a non complete and non-optimal searching algorithm.

It works by always exploring the next cheapest node. But the cheapest path might get you going around in a loop

In this case we keep choosing the cheapest option in the graph

'''

from collections import deque

class Node:  # Node has only PARENT_NODE, STATE, DEPTH

    def __init__(self, state, parent=None, depth=0, heuristicCost=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTIC = heuristicCost

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH(LIFO):

    fringe = []

    initial_node = Node(INITIAL_STATE, heuristicCost=HEURISTIC_COST[INITIAL_STATE])
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.HEURISTIC = HEURISTIC_COST[child]
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue

'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        queue.append(node)
    return queue


'''
Removes and returns the first element from fringe
This is done in
'''
def REMOVE_FIRST(queue):

    #Find the element with the lowest heuristic value function

    lowestElement = None

    for node in queue:
        if lowestElement is None:
            lowestElement = node
        else:
            if lowestElement.HEURISTIC > node.HEURISTIC:
                lowestElement = node

    queue.remove(lowestElement)

    return lowestElement

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states


    return STATE_SPACE[state]


INITIAL_STATE = 'A'
GOAL_STATE = 'K'

STATE_SPACE = {'A' : ['B', 'C', 'D'],
               'B' : ['F', 'E'],
               'C' : ['E'],
               'D' : ['H','I','J'],
               'E' : ['G', 'H'],
               'F' : ['G'],
               'G' : ['K'],
               'H' : ['K', 'L'],
               'I' : ['L'],
               'J' : [],
               'K' : [],
               'L' : []}

HEURISTIC_COST = {'A' : 6,
                  'B' : 5,
                  'C' : 5,
                  'D' : 2,
                  'E' : 4,
                  'F' : 5,
                  'G' : 4,
                  'H' : 1,
                  'I' : 2,
                  'J' : 0,
                  'K' : 0,
                  'L' : 0
                  }

PATH_COST = {('A', 'B') : 1,
             ('A', 'C') : 2,
             ('A', 'D') : 4,

             ('B', 'F') : 5,
             ('B', 'E') : 4,

             ('C', 'E') : 1,

             ('D', 'H') : 1,
             ('D', 'I') : 4,
             ('D', 'J') : 2,

             ('E', 'G') : 2,
             ('E', 'H') : 3,

             ('F', 'G') : 1,

             ('G', 'K') : 6,

             ('H', 'K') : 6,
             ('H', 'L') : 5,

             ('I', 'L') : 3
             }

'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH(False)
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
