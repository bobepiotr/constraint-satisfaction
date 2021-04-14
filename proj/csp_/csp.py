
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


def select_unassigned_variable(assignments, variables):
    for variable in variables:
        if variable not in assignments:
            return variable


def is_consistent_with(assignments, constraints):
    for constraint in constraints:
        if not constraint.satisfied(assignments):
            return False
    return True
