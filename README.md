# Triangle Visualizer

A simple Python tool that visualizes a triangle along with its incircle and circumcircle using Matplotlib.  
While the plot shows the geometric shapes, all computed triangle properties—such as angles, side lengths, area, inradius, incenter, circumradius, and circumcenter—can be saved into a log file.

---

## Features

- Plots the triangle, its incircle, and circumcircle
- Calculates and stores triangle properties:
  - Angles (A, B, C)
  - Side lengths (a, b, c)
  - Area
  - Perimeter (2P)
  - Inradius and incenter
  - Circumradius and circumcenter
- Saves all these properties into a `LOG.txt` file upon calling `.save()`

---

## Usage

1. **Create your triangle object** (assuming your class is named `Triangle`):

```python
Tri = Triangle(A, B, C)  # where A, B, C are tuples like (x, y)
```


2. **Visualize the triangle with incircle and circumcircle:**
![Triangle with Incircle and Circumcircle](https://github.com/TheCanineProgrammer/triangle-incircle-circumcircle/blob/main/Images/Right.png)

3. **Save triangle data to file:**

You can save all the calculated triangle information to a log file by calling:

```python
tri.save()
```

## Sample `LOG.txt` content

```
A = 90.0°, B = 53.13010235415599°, C = 36.86989764584401°
a = 5.0, b = 4.0, c = 3.0
Area = 6.0
2P = 12.0
Inradius: 1.0
Incenter: (1.0, 1.0)
Circumradius: 2.5
Circumcenter: (1.5, 2.0)
```

## Dependencies

- numpy
- matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```
