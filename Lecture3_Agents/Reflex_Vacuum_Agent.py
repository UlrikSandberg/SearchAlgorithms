'''
Ignores percept history only respond to current percept(location and status)

Instead of a table it works with condition based rules such as if and else

if condition then return action --> if status = Dirty then return suck

'''

#Environment - Originally there was only A, B but homework assigment extended the lab
#to enclude C, D as well.
A = 'A'
B = 'B'
C = 'C'
D = 'D'

#Initialization of environment location status
Environment = {
    A : 'Dirty',
    B : 'Dirty',
    C : 'Dirty',
    D : 'Dirty',
    'Current' : A
}

# Takes a location and respective status in the form of (A, 'Dirty') and returns an action
def REFLEX_VACUUM_AGENT(loc_st):
    #Firstly determine if the status is dirty, if so return the action suck
    if loc_st[1] == 'Dirty':
        return 'Suck'
    ##Original we would determine to go right or left on index 0 which is the location
    #if loc_st[0] == A:
    #    return 'Right'
    #if loc_st[0] == B:
    #    return 'Left'

    ##Homework week 1 - Reflex-Vacuum Agent with 4 locations
    ##No point in going either left or right when there are 4 locations just keep turning.
    return 'Right' #If it is not dirty, keep turning right to combat the 4 different squares

#Returns the location in the environment and the respective status of that location
def Sensors():
    location = Environment['Current']
    return (location, Environment[location])

#Takes an action parameter and carries out that action
def Actuators(action):
    #Retreive the location for specific rules based on the location
    location = Environment['Current']

    #If the action is suck, the the location to clean
    if action == 'Suck':
        Environment[location] = 'Clean'

    ##Original - Moving respective to location and action
    #elif action == 'Right' and location == A:
    #    Environment['Current'] = B
    #elif action == 'Left' and location == B:
    #    Environment['Current'] = A

    ##Homework week 1 - Reflex-Vacuum Agent with 4 locations - Move the vacuum cleaner respective to the location and action
    if action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Right' and location == B:
        Environment['Current'] = C
    elif action == 'Right' and location == C:
        Environment['Current'] = D
    elif action == 'Right' and location == D:
        Environment['Current'] = A

#Run the reflex_vacuum_agent(loc_st) method n times
def run(n, make_agent):
    print('     Current         new')
    print('location     status  action  location    status')
    for i in range (1, n):
        #Perceive the environment and return the current location and that locations status
        (location, status) = Sensors()
        print("{:12s}{:8s}".format(location, status))
        #Based on the current location and status determine an appropriate action
        action = make_agent(Sensors())
        #Make the actuators respond to the chosen action
        Actuators(action)

        #Print out the new location and status after the actuators performed movement
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(20, REFLEX_VACUUM_AGENT);