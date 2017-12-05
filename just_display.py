from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy
import math

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files
combined = mesh.Mesh.from_file('combined.stl')

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(combined.vectors))

# Auto scale to the mesh size
scale = combined.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
