import proj.csp_.constraints.map_constraint as mc


class Csp:
    def __init__(self, variables, domain, constraints):
        self.variables = variables
        self.domain = domain
        self.constraints = constraints

    def backtracking_search(self, assignment, ls):
        if len(assignment) == len(self.variables):
            ls.append(assignment)
            return assignment

        variable = variable_selection(assignment, self.variables)
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

        variable = variable_selection(assignment, self.variables)
        neighbours = find_neighbours(assignment, self.constraints, variable)
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


def get_unassigned_variable(assignments, variables):
    unassigned = []
    for variable in variables:
        if variable not in assignments:
            unassigned.append(variable)
    return unassigned


def variable_selection(assignments, variables):
    return get_unassigned_variable(assignments, variables)[0]


def variable_selection_mrv(assignments, variables, domain):
    unassigned = get_unassigned_variable(assignments, variables)
    poss_values: dict = {k: v for k, v in domain.items() if k in unassigned}
    lowest = min(poss_values, key=lambda k: len(poss_values[k]))
    return lowest


def variable_selection_degree(assignments, variables, constraints):
    unassigned = get_unassigned_variable(assignments, variables)
    variables_constraints = {}

    for c in constraints:
        for v in c.variables:
            if v in unassigned:
                if v in variables_constraints:
                    variables_constraints[v] += 1
                else:
                    variables_constraints[v] = 1
    biggest = max(variables_constraints, key=lambda k: variables_constraints[k])
    return biggest


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
