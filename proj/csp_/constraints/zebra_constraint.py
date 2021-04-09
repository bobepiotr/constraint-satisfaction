from proj.csp_.constraints.constraint import Constraint


class ZebraConstraint(Constraint):
    def __init__(self, func, values):
        super().__init__(values)
        self.func = func

    def satisfied(self, assignment):
        if len(self.variables) > 2:
            return self.func(assignment, self.variables)

        params = []
        for v in self.variables:
            if v in assignment:
                params.append(assignment[v])
            else:
                return True
        return self.func(*params)


def all_different(assignment, kind):
    tmp = []
    for k in kind:
        if k in assignment:
            tmp.append(assignment[k])
    return len(tmp) == len(set(tmp))
