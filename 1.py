import numpy as np
import matplotlib.pyplot as plt
import random
import pylab


def point_in_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x_, y_ = sorted([random.random(), random.random()])
    s, t, u = x_, y_ - x_, 1 - y_
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])


def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


# vertex = [
#     [0, 0],
#     [1, 0],
#     [1/2, np.cos(np.deg2rad(30))]
# ]

vertex = [
    [1, 0],
    [0.5, np.cos(np.deg2rad(30))],
    [-0.5, np.cos(np.deg2rad(30))],
    [-1, 0],
    [-0.5, -np.cos(np.deg2rad(30))],
    [0.5, -np.cos(np.deg2rad(30))],
]

pylab.ion()
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable='box')

figure_x = [vertex[i][0] for i in range(len(vertex))]
figure_x.append(vertex[0][0])
figure_y = [vertex[i][1] for i in range(len(vertex))]
figure_y.append(vertex[0][1])

pylab.plot(figure_x, figure_y, marker="o", c="r")
pylab.draw()

x_rand = random.random()
point = [0.2, 0.2]
plt.plot([point[0]], [point[1]], marker=".", c="k", markersize=1)
plt.draw()

for i in range(100000):
    sel_vertex = random.choice([x for x in range(len(vertex))])
    sel_vertex_coord = vertex[sel_vertex]
    point = midpoint(sel_vertex_coord, point)

    plt.plot([point[0]], [point[1]], marker=".", c="k", markersize=1)
    # plt.pause(0.00001)
plt.draw()
pylab.ioff()
pylab.show()
