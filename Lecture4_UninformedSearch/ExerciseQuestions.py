'''
Exercise Questions

1. Succesor nodes are inserted at front of the fringe(successor list)
as a node is expanded. Is this a breadth (LIFO) or depth-first search
(FIFO)

Seeing as this would mean that we keep exploring down the first path
we have chosen. And keeping exploring deeper down the nodes we
constantly keep exploring this is Depth-first-search or LIFO, the
latest to go in are also the quickest to get out

'''


'''
Exercise Questions 

2. For goal j, give the fringe (successor list) after expanding each
node in a LIFO (Depth-first-search) manner

DepthFirstSearch
fringe: [State: B - Depth: 1, State: C - Depth: 1]
fringe: [State: B - Depth: 1, State: F - Depth: 2, State: G - Depth: 2]
fringe: [State: B - Depth: 1, State: F - Depth: 2, State: H - Depth: 3, State: I - Depth: 3, State: J - Depth: 3]
Solution path:
State: J - Depth: 3
State: G - Depth: 2
State: C - Depth: 1
State: A - Depth: 0

'''

'''
Exercise Questions 

3. What is the effect of inserting successor nodes at the end of the 
fringe as node is expanded? A depth or breadth-first search?

It is effectively a breadth-first search, because we will constantly explore
those nodes which has been in the fringe for longest amount of time first

'''

'''
Exercise Questions 

3. For goal j, give the fringe (successor list) after expanding each
node if a FIFO manner (breadth-first-search).

BreathFirstSearch
fringe: deque([State: B - Depth: 1, State: C - Depth: 1])
fringe: deque([State: C - Depth: 1, State: D - Depth: 2, State: E - Depth: 2])
fringe: deque([State: D - Depth: 2, State: E - Depth: 2, State: F - Depth: 2, State: G - Depth: 2])
fringe: deque([State: E - Depth: 2, State: F - Depth: 2, State: G - Depth: 2])
fringe: deque([State: F - Depth: 2, State: G - Depth: 2])
fringe: deque([State: G - Depth: 2])
fringe: deque([State: H - Depth: 3, State: I - Depth: 3, State: J - Depth: 3])
fringe: deque([State: I - Depth: 3, State: J - Depth: 3])
fringe: deque([State: J - Depth: 3])
Solution path:
State: J - Depth: 3
State: G - Depth: 2
State: C - Depth: 1
State: A - Depth: 0


'''