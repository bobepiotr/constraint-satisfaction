
class Csp:
    def __init__(self, variables, domain, constraints):
        self.variables = variables
        self.domain = domain
        self.constraints = constraints

    def backtracking_search(self, assignment, ls):
        if len(assignment) == len(self.variables):
            ls.append(assignment)
            return assignment

        variable = select_unassigned_variable(assignment, self.variables)
        for value in self.domain[variable]:
            local_assignment = assignment.copy()
            local_assignment[variable] = value
            if is_consistent_with(local_assignment, self.constraints):
                self.backtracking_search(local_assignment, ls)

        return ls

    def forward_checking(self, domain, assignment, ls):
        if len(assignment) == len(self.variables):
            ls.append(assignment)
            return assignment

        variable = select_unassigned_variable(assignment, self.variables)
        neighbours = find_neighbours(assignment, self.constraints, variable)
        print(neighbours)
        for value in domain[variable]:
            local_assignment = assignment.copy()
            local_assignment[variable] = value
            local_domain = domain.copy()
            if is_consistent_with(local_assignment, self.constraints):
                for neighbour in neighbours:
                    for n_value in local_domain[neighbour]:
                        local_assignment[neighbour] = n_value
                        if not is_consistent_with(local_assignment, self.constraints):
                            local_domain[neighbour].remove(n_value)
                    if neighbour in local_assignment:
                        del local_assignment[neighbour]
                self.forward_checking(local_domain, local_assignment, ls)

        return ls


def select_unassigned_variable(assignments, variables):
    for variable in variables:
        if variable not in assignments:
            return variable


def is_consistent_with(assignments, constraints):
    for constraint in constraints:
        if not constraint.satisfied(assignments):
            return False
    return True


def find_neighbours(assignments, constraints, variable):
    connected = set()
    for c in constraints:
        if variable in c.variables:
            for v in c.variables:
                if v != variable and v not in assignments:
                    connected.add(v)

    return connected
