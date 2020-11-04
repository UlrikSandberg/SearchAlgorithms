'''
TABLE_DRIVEN_AGENT

Contains a table with all possible percepts that can occur -->
So basically all kinds of events in chronological order than can occur
has to be present in the table so that the agent may read what to do next with a current perceived list of percepts

The table contains all possible percept sequences to match with the percept history, for a N-step lifetime
agent this gives 4^n table, which obviously grows way to large

No to good seeing as the pre-configured table grows huge. Fx we would only need 4 entries
in the table if only the current percept was used to select an action instead of the percept history

'''

#Possible environments
A = 'A'
B = 'B'

#Percept history
percepts = []
#Pre-configured percept history
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    ((A,'Clean'),(A,'Clean')): 'Right',
    ((A,'Clean'),(A,'Dirty')): 'Suck',
    ((A,'Clean'),(A,'Clean'), (A, 'Clean')):'Right',
    ((A,'Clean'),(A,'Clean'), (A, 'Dirty')):'Suck',
    ((A,'Clean'),(A,'Dirty'), (B, 'Clean')):'Left',
    ((A,'Clean'),(A,'Dirty'), (B, 'Clean'), (B, 'Dirty')) : 'Suck'
}

'''
Takes a percept history and performs a lookup on the table={} for a matching percept sequence
'''
def LOOKUP(percepts, table):
    action = table.get(tuple(percepts))
    return action

'''
Takes a percept in the form of a tuple (A, 'Clean') and adds it to the
percept history. Afterwards it looks up an action in the percept table
and mathc the current percept history to a preconfigured percept sequence in the percept table
returns that percept
'''
def TABLE_DRIVEN_AGENT(percept):
    percepts.append(percept)
    action = LOOKUP(percepts, table)
    return action

#Run the agent
def run():
    print('Action \tPercepts')
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Dirty')), '\t', percepts)

run()