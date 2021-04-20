import proj.utilities.map_instance_generator as ig
import proj.csp_.csp as csp
import proj.csp_.constraints.map_constraint as mc
import proj.csp_.constraints.zebra_constraint as zc
import copy


# solve map coloring problem with CSP algorithm
def solve_map_coloring_problem(plot_display='save'):
    problem_instance, triangulation = ig.create_problem_instance(amount=5, border=10)
    variables = problem_instance.keys()
    constraints = mc.create_map_constraint_list(problem_instance)
    map_domain = ['red', 'green', 'blue', 'yellow']
    domain = {}
    for variable in variables:
        domain[variable] = map_domain.copy()

    c = csp.Csp(variables, domain, constraints)
    result = c.forward_checking(domain, {}, [])
    # result = c.backtracking_search({}, [])

    for res in result:
        print(res)

    if plot_display == 'save':
        ig.save_colored_plot(*triangulation, result)

    elif plot_display == 'display':
        for r in result:
            ig.display_colored_plot(*triangulation, r)


# solve einstein's riddle with CSP algorithm
def solve_einsteins_riddle():
    house = [1, 2, 3, 4, 5]
    countries = ['Norwegian', 'English', 'Danish', 'German', 'Swedish']
    colors = ['red', 'green', 'white', 'yellow', 'blue']
    smokes = ['light', 'cigar', 'pipe', 'filterless', 'menthol']
    drinks = ['tea', 'milk', 'water', 'beer', 'coffee']
    pets = ['cats', 'birds', 'dogs', 'horses', 'fish']

    var = countries + colors + smokes + drinks + pets

    dom = {}
    for variable in var:
        dom[variable] = house

    constraint = [
        zc.ZebraConstraint(zc.all_different, countries),   # W każdym domu mieszka inna osoba
        zc.ZebraConstraint(zc.all_different, colors),   # Każdy dom jest innego koloru
        zc.ZebraConstraint(zc.all_different, smokes),   # W każdym domu pali się inne wyroby tytoniowe
        zc.ZebraConstraint(zc.all_different, drinks),   # W każdym domu pija się inne napoje
        zc.ZebraConstraint(zc.all_different, pets),    # W każdym domu hoduje się inne zwierzęta

        zc.ZebraConstraint(lambda n: n == 1, ['Norwegian']),   # 1. Norweg zamieszkuje pierwszy dom
        zc.ZebraConstraint(lambda e, r: e == r, ('English', 'red')),   # 2. Anglik mieszka w czerwonym domu.
        zc.ZebraConstraint(lambda g, w: w - g == 1, ('green', 'white')),    # 3. Zielony dom znajduje się bezpośrednio po lewej stronie domu białego.
        zc.ZebraConstraint(lambda d, t: d == t, ('Danish', 'tea')),   # 4. Duńczyk pija herbatkę.
        zc.ZebraConstraint(lambda lc, c: abs(lc - c) == 1, ('light', 'cats')),   # 5. Palacz papierosów light mieszka obok hodowcy kotów.
        zc.ZebraConstraint(lambda y, ci: ci == y, ('yellow', 'cigar')),   # 6. Mieszkaniec żółtego domu pali cygara.
        zc.ZebraConstraint(lambda g, p: g == p, ('German', 'pipe')),   # 7. Niemiec pali fajkę.
        zc.ZebraConstraint(lambda m: m == 3, ['milk']),   # 8. Mieszkaniec środkowego domu pija mleko.
        zc.ZebraConstraint(lambda l, w: abs(l - w) == 1, ('light', 'water')),   # 9. Palacz papierosów light ma sąsiada, który pija wodę.
        zc.ZebraConstraint(lambda fl, b: fl == b, ('filterless', 'birds')),   # 10.Palacz papierosów bez filtra hoduje ptaki.
        zc.ZebraConstraint(lambda s, d: s == d, ('Swedish', 'dogs')),   # 11.Szwed hoduje psy.
        zc.ZebraConstraint(lambda n, b: abs(n - b) == 1, ('Norwegian', 'blue')),   # 12.Norweg mieszka obok niebieskiego domu.
        zc.ZebraConstraint(lambda h, y: abs(h - y) == 1, ('horses', 'yellow')),   # 13.Hodowca koni mieszka obok żółtego domu.
        zc.ZebraConstraint(lambda m, b: m == b, ('menthol', 'beer')),   # 14.Palacz mentolowych pija piwo.
        zc.ZebraConstraint(lambda g, c: g == c, ('green', 'coffee'))   # 15.W zielonym domu pija się kawę.
    ]

    c = csp.Csp(var, dom, constraint)
    result = c.backtracking_search({}, [])
    print(result)
    print('Fishes are in the house number: '+str(result[0]['fish']))


def has_duplicates(ls):
    no_duplicates = []

    for elem in ls:
        if elem not in no_duplicates:
            no_duplicates.append(elem)
        else:
            return True
    return False


if __name__ == '__main__':
    # solve_einsteins_riddle()
    solve_map_coloring_problem()
