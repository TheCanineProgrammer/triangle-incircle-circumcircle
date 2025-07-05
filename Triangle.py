import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from Classes import Triangle

P1 = tuple(map(float, input().split()))                    # A
P2 = tuple(map(float, input().split()))                    # B
P3 = tuple(map(float, input().split()))                    # C

Tri = Triangle(P1, P2, P3)
Tri.save()


fig, ax = plt.subplots()

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

tri = plt.Polygon([P1, P2, P3], closed = True, facecolor = "lightblue", edgecolor = "black")

positions = Tri.vertices()

in_c = Circle(Tri.calculate_I(), Tri.calculate_r(), color = "orange")
ex_c = Circle(Tri.calculate_circumcenter(), Tri.calculate_R(), color = "purple")
ex_c.set_alpha(0.5)

ax.grid(True)
ax.add_patch(tri)
ax.add_patch(in_c)
ax.add_patch(ex_c)
ax.set_aspect('equal')
ax.autoscale_view()
plt.show()