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
    CostaRica, Panama, Colombia, Venezuela, Guyana, Suriname, GuyaneFr, Ecuador, Peru, Brasil, Bolivia, Paraguay, Chile, Argentina, Uruguay = 'CostaRica', 'Panama', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'GuyaneFr', 'Ecuador', 'Peru', 'Brasil', 'Bolivia', 'Paraguay', 'Chile', 'Argentina', 'Uruguay'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [CostaRica, Panama, Colombia, Venezuela, Guyana, Suriname, GuyaneFr, Ecuador, Peru, Brasil, Bolivia, Paraguay, Chile, Argentina, Uruguay]
    domains = {
        CostaRica: values[:],
        Panama: values[:],
        Colombia: values[:],
        Venezuela: values[:],
        Guyana: values[:],
        Suriname: values[:],
        GuyaneFr: values[:],
        Ecuador: values[:],
        Peru: values[:],
        Brasil: values[:],
        Bolivia: values[:],
        Paraguay: values[:],
        Chile: values[:],
        Argentina: values[:],
        Uruguay: values[:]
    }
    neighbours = {
        CostaRica : [Panama],
        Panama : [CostaRica, Colombia],
        Colombia : [Panama, Venezuela, Ecuador, Peru, Brasil],
        Venezuela : [Colombia, Guyana, Brasil],
        Guyana : [Venezuela, Suriname, Brasil],
        Suriname : [Guyana, GuyaneFr, Brasil],
        GuyaneFr : [Suriname, Brasil],
        Brasil : [GuyaneFr, Suriname, Guyana, Venezuela, Colombia, Peru, Bolivia, Paraguay, Argentina, Uruguay],
        Uruguay : [Brasil, Argentina],
        Argentina : [Uruguay, Paraguay, Chile, Bolivia],
        Chile : [Argentina, Bolivia, Peru],
        Bolivia : [Chile, Argentina, Paraguay, Peru],
        Paraguay : [Bolivia, Argentina, Uruguay, Brasil],
        Peru : [Bolivia, Chile, Brasil, Ecuador, Colombia],
        Ecuador : [Peru, Colombia]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        CostaRica: constraint_function,
        Panama: constraint_function,
        Colombia: constraint_function,
        Venezuela: constraint_function,
        Guyana: constraint_function,
        Suriname: constraint_function,
        GuyaneFr: constraint_function,
        Brasil: constraint_function,
        Uruguay: constraint_function,
        Argentina: constraint_function,
        Chile: constraint_function,
        Bolivia: constraint_function,
        Paraguay: constraint_function,
        Peru: constraint_function,
        Ecuador: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html


