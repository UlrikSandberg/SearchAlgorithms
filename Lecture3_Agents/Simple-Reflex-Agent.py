'''

As an extension to the reflex_vacuum_agent.py this reflex agent has the addition
of rules and actions which map to those rules. Instead of the if-else conditional approach
to choosing actions this, agent works on rules. If the environment men is A and the status is dirty
then it has a rule action for (A, 'Dirty') --> 1 and 1 maps to the action Suck.

'''

#Environment locations
A = 'A'
B = 'B'

#Mapping from rule to action
RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

#Definition of location and respective status and which rule that maps to.
rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}
# Ex. rule (if location == A && Dirty then rule 1)

#Initialize environment locations and status
Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}

def INTERPRET_INPUT(input): #No interpretation
    return input

#Match a location and an approriate status to a given rule from the rules table
def RULE_MATCH(state, rules):
    rule = rules.get(tuple(state))
    return rule

#Take a percept in the form of (location, status) -> (A, 'Dirty') and
#returns an action based on its internal rule table
def SIMPLE_REFLEX_AGENT(percept):
    #Interpret the input
    state = INTERPRET_INPUT(percept)
    #Uses the tuple (A, 'Dirty') to match for rules
    rule = RULE_MATCH(state, rules)
    #After reading an approriate rule, figure which action maps to the current rule
    action = RULE_ACTION[rule]
    return action

#Returns the current location and its respective status
def Sensors():
    location = Environment['Current']
    return (location, Environment[location])

def Actuators(action):
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A

#Run the simple_reflex_agent(percept) method n times
def run(n):
    print('     Current         new')
    print('location     status  action  location    status')
    for i in range (1, n):
        #Use the sensors to the current location and respective status
        (location, status) = Sensors()
        print("{:12s}{:8s}".format(location, status))
        #Determine the action to be carried out based on current location and status
        action = SIMPLE_REFLEX_AGENT(Sensors())
        #Use the actuators to carry out the determined action
        Actuators(action)
        #Print the new state after action has been carried out
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(9);