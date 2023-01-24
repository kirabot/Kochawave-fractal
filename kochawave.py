from math import sqrt, cos, sin, radians
import matplotlib.pyplot as plt

# Kochawave fractal function, recursive
# x, y: lists of x and y coordinates
# L: length of the line segment
# angle: angle of the line segment
# dim: number of dimensions


# The core Kochawave fractal function
def kochawave_curve_builder(x=[0], y=[0], L=1, angle=0, dim=5, show=False):
    
    if dim == 0:
        x1 = x[-1] + L * cos(radians(angle))
        y1 = y[-1] + L * sin(radians(angle))
        x.append(x1)
        y.append(y1)
    else:
        L /= 3
        kochawave_curve_builder(x, y, L, angle, dim-1)
        
        L *= sqrt(3)
        angle += 30
        kochawave_curve_builder(x, y, L, angle, dim-1)
        
        L /= sqrt(3)
        angle -= 150
        kochawave_curve_builder(x, y, L, angle, dim-1)
        
        angle += 120
        kochawave_curve_builder(x, y, L, angle, dim-1)
        

# Draws and displays a single Kochawave fractal
def kochawave(x=[0], y=[0], L=1, angle=0, dim=5, color="black", show=False):
    
    kochawave_curve_builder(x, y, L, angle, dim, show)
    
    # Plot the fractals
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.plot(x, y,"k", c=color, lw=0.25)
    ax.axis("off")
    ax.set_aspect("equal")
    
    if show:
        plt.show()
    
    return fig


# Draws and displays a Kochawave triangle
def kochawave_triangle(x=[0], y=[0], L=1, angle=0, dim=5, color="black", show=False):
    
    kochawave_curve_builder(x, y, L, angle, dim, show)
    kochawave_curve_builder(x, y, L, angle+120, dim, show)
    kochawave_curve_builder(x, y, L, angle-120, dim, show)
    
    # Plot the fractals
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.plot(x, y,"k", c=color, lw=0.25)
    ax.axis("off")
    ax.set_aspect("equal")
    
    if show:
        plt.show()
    
    return fig


# Store images of each step of the Kochawave fractal
# n: number of dimensions
# path: path to store the images
def record(n, path):
    import os
    
    if not os.path.exists(path):
        os.makedirs(path)
        
    # create the images
    for i in range(n):
        x = [0]
        y = [0]
        fig = kochawave(x=x, y=y, L=1, angle=0, dim=i)
        fig.savefig(path + "kochawave{}.png".format(i))
        plt.close(fig)
        
        
# Example
# kochawave(x=[0], y=[0], L=1, angle=0, dim=10, color="black", show=True)
kochawave_triangle(color="red", dim=10, show=True)