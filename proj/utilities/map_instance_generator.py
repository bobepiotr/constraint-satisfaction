import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import random as ran
from collections import defaultdict
import os
import datetime


def find_neighbors(tess):
    neighbors = defaultdict(set)
    for simplex in tess.simplices:
        for idx in simplex:
            other = set(simplex)
            other.remove(idx)
            neighbors[idx] = neighbors[idx].union(other)
    return neighbors


def generate_random_points(amount, border):
    random_points = []
    for i in range(amount):
        random_point = [ran.randint(0, border), ran.randint(0, border)]
        while random_point in random_points:
            random_point = [ran.randint(0, border), ran.randint(0, border)]
        random_points.append(random_point)
    return random_points


def triangulation(amount, border):
    random_points_ls = generate_random_points(amount, border)
    points = np.array(random_points_ls)
    tri = Delaunay(points)

    return tri, points


def find_neighbours(tri, point_list):
    neigh_dict = find_neighbors(tri)
    neigh = {}

    for point, neighbours in neigh_dict.items():
        act_point = (point_list[point][0], point_list[point][1])
        neigh[act_point] = []
        for nei in neighbours:
            neigh[act_point].append((point_list[nei][0], point_list[nei][1]))

    return neigh


def create_tri_plot(tri, points):
    plt.triplot(points[:, 0], points[:, 1], tri.simplices)
    plt.plot(points[:, 0], points[:, 1], 'o', c='yellow')
    plt.show()


def display_colored_plot(tri, points, result):
    if result is not None:
        plt.triplot(points[:, 0], points[:, 1], tri.simplices)
        for point, color in result.items():
            plt.plot(point[0], point[1], 'o', c=color, markersize=20)
        plt.show()
    else:
        print('Result is failure')


def save_colored_plot(tri, points, result):
    root_path = os.path.dirname(os.path.abspath('__root__'))
    output_dir_name = datetime.datetime.now().strftime("%d%m%Y_%H%M%S%f")
    output_path = os.path.join(root_path, 'map_colouring_solutions', output_dir_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if result is not None:
        for i, res in enumerate(result):
            plt.triplot(points[:, 0], points[:, 1], tri.simplices)
            for point, color in res.items():
                plt.plot(point[0], point[1], 'o', c=color, markersize=20)
            plt.savefig(output_path+'\\figure'+str(i)+'.png')
            plt.clf()
    else:
        print('Result is failure')


def create_problem_instance(amount, border):
    tri, points = triangulation(amount, border)
    return find_neighbours(tri, points), (tri, points)
