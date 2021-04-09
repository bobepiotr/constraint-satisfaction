from proj.csp_.constraints.constraint import Constraint


class MapConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def satisfied(self, assignment):
        if self.variables[0] not in assignment or self.variables[1] not in assignment:
            return True
        return assignment[self.variables[0]] != assignment[self.variables[1]]


def create_map_constraint_list(point_dict):
    constraint_list = []
    for point, neighbours in point_dict.items():
        for neighbour in neighbours:
            constraint_list.append(MapConstraint((point, neighbour)))

    return constraint_list
