import unittest
import proj.csp_.constraints.map_constraint as mc
import proj.csp_.csp as csp


class TestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.constraints = [
            mc.MapConstraint([4, 5]),
            mc.MapConstraint([2, 3]),
            mc.MapConstraint([2, 5]),
            mc.MapConstraint([4, 3]),
            mc.MapConstraint([5, 3])
        ]

        self.domain = {1: [1, 2], 2: [1, 2, 3, 4, 5], 3: [4, 3, 2, 1], 4: [1, 3, 5], 5: [1, 3, 2, 1]}
        self.assignments = {1: '1', 2: '2', 3: '3'}
        self.variables = [1, 2, 3, 4, 5]

    def test_mrv_selection(self):
        res = csp.variable_selection_mrv(self.assignments, self.variables, self.domain)
        self.assertEqual(res, 4)

    def test_degree_selection(self):
        res = csp.variable_selection_degree(self.assignments, self.variables, self.constraints)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
