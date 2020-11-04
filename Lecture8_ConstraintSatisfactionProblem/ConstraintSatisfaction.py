from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result != None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html

'''

1. What is returned by create_australia_csp()?
    
    returns the CSP class with instantiated domain this is seen on line 94

2. What is returned by backtracking_search()?
    The complete coloring map. It calls itself recursively figuring out which maps part can be colored what. It returns a dictionary
    
3. What is the purpose of assignment variable?
    The assignment is a dict which holds the final possible output. Fx -->
    {} = {'NW' : 'Blue', 'Q' : 'Red'}

4. What is the purpose of variable variable?
    The purpose of var is to store all the possible variable or locations we are able to color
    When calling we get a location which has not yet been colored

5. What is the purpose of the following statement?
    for value in self.order_domain_values(variable, assignment)
    
    For each location iterate the colors available to that location and check if it is consisten
    
6. What would the following do?
    if self.is_consistent('Q', 'Red', {'NT': 'Blue', 'NSW' : 'green'}):
        assignment[variable] = value
        
    firstly we check if assignment is empty, in which case we return True the color and location is eligible
    Then we check if the value of Red is eligible for location Q given that each of it's neighbours, this is the case and we return true
    
    we then assign red to the location 'Q'
    

7. What would then assignment be?
    {'Q': 'Red', 'NT': 'Blue', 'NSW' : 'green'}

8. What is the effect of del assignment[variable]?
    If a recursive procedure returns with None it means that there is eventually no way to complete
    the coloring with this setup and we thus delete the certain color from a location.

'''