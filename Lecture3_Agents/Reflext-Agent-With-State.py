'''
While reflex-based agents only responds to current percepts not utilizing history.
Model-based reflex agents maintain internal state that depends upon percept history
this model tells the agent how the world works.

It is relevant for the agent to know two types of information.
- How environment evolves independent of the agent. (Clean squares stay clean)
- How the agents actions affect the environment
'''


#Environment locations
A = 'A'
B = 'B'
C = 'C'
D = 'D'

'''
state, a description of the current world state rules,
a sequence, a set of condition-action rules
action, the most recent action, initially none'''
state = {}
action = None
model = {A: None, B: None, C: None, D: None} # Initially ignorant

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (C, 'Dirty'): 1,
    (D, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 2,
    (C, 'Clean'): 2,
    (D, 'Clean'): 2,
    (A, B, C, D, 'Clean'): 4
}
# Ex. rule (if location == A && Dirty then rule 1)

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}

def INTERPRET_INPUT(input) : # No interpretation
    return input

def RULE_MATCH(state, rules): # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule

'''
Takes state={}, action=None, percept=(A, 'Dirty')

and returns and update state based on the input parameters

The state is returned in the form of either input percept or (A, B, C, D, 'Clean')
'''
def UPDATE_STATE(state, action, percept):
    #Sets percepts equal to a location and its respective status
    (location, status) = percept

    #Sets state equal to the same percept Fx. (A, 'Dirty')
    state = percept

    #Original

    #if model[A] == model[B] == 'Clean':
    #    state = (A, B, 'Clean')
    # Homework 2- Reflex-Vacuum-Agent-With-State with 4 locations
    if model[A] == model[B] == model[C] == model[D] == 'Clean':
        state = (A, B, C, D, 'Clean')
    model[location] = status
    return state

'''
Takes a percept in the form of a tuple (A, 'Dirty')
'''
def REFLEX_AGENT_WITH_STATE(percept):
    #Global vars. Initially State={}, action=None
    global state, action
    #Update the models current state, with the percept.
    state = UPDATE_STATE(state, action, percept)

    #Fetch the appropriate rule based on the current state and defined rules
    rule = RULE_MATCH(state, rules)

    #Match the rule to a given action
    action = RULE_ACTION[rule]
    return action

#Returns the current location and that locations status
def Sensors():
    location = Environment['Current']
    return (location, Environment[location])

#Carry out given action
def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    #Original
    #elif action == 'Right' and location == A:
    #    Environment['Current'] = B
    #elif action == 'Left' and location == B:
    #    Environment['Current'] = A
    #Homework 2- Reflex-Vacuum-Agent-With-State with 4 locations
    if action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Right' and location == B:
        Environment['Current'] = C
    elif action == 'Right' and location == C:
        Environment['Current'] = D
    elif action == 'Right' and location == D:
        Environment['Current'] = A


#Run the Reflext_Agent_With_State n times
def run(n):
    print('     Current         new')
    print('location     status  action  location    status')
    for i in range (1, n):
        #Use the sensors to retreive the current location and respective status
        (location, status) = Sensors()
        print("{:12s}{:8s}".format(location, status))
        #Determine the next action based on the current location and state
        action = REFLEX_AGENT_WITH_STATE(Sensors())
        #Use the actuators to carry out action
        Actuators(action)
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))

run(20);