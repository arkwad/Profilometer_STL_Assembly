from stl import mesh
import stl
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy
import math

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files
first_scan = mesh.Mesh.from_file('probka-1-stl-ascii.stl')
second_scan = mesh.Mesh.from_file('probka-2-stl-ascii.stl')
third_scan = mesh.Mesh.from_file('probka-3-stl-ascii.stl')

# find mins and max to calculate offset over z axis
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(first_scan)
first_scan.z -= ((minz + maxz)/2)-5 # an ugly way to calculate offset

# find mins and max to calculate offset over z axis 
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(second_scan)
second_scan.z -= ((minz + maxz)/2)-5 # an ugly way to calculate offset

# find mins and max to calculate offset over z axis
minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(third_scan)
third_scan.z -= ((minz + maxz)/2)-5 # an ugly way to calculate offset 
 
second_scan.rotate([0.0, 0.5, 0.0], math.radians(120))
third_scan.rotate([0.0, 0.5, 0.0], math.radians(240))

# combine all scans to one stl
together_mesh = mesh.Mesh(numpy.concatenate([first_scan.data, second_scan.data, third_scan.data]))

# save as ascii stl file
together_mesh.save('combined.stl', mode=stl.Mode.ASCII) 
print "New stl saved succesfully!"
