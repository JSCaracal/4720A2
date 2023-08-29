# Import necessary libraries
import pygame as pg
from OpenGL.GL import *
import numpy as np
from objLoaderV1 import ObjLoader
# Initialize pygame
'''
pg.init()

# Set up OpenGL context version
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)

# Create a window for graphics using OpenGL
width = 640
height = 480
pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF)

# Todo: Part 1
# Set the background color (clear color)
# glClearColor takes 4 arguments: red, green, blue, alpha. Each argument is a float between 0 and 1.
glClearColor(1.0, 0.0, 0.0, 1.0)
'''

# Todo: Part 2
object = ObjLoader(".\\objects\\raymanModel.obj")
print("The position Coords for the Object:")
print(object.v)
print("The texture coords for the object:")
print(object.vt)
print("The normals for the object:")
print(object.vn)
print("And finally the vertices")
print(object.vertices)
# Todo: Part 3
def extent(o):
    print("Max Values for each Coord")
    maxVales = o.max(axis=0)
    print("X: " + str(maxVales[0]) + " Y: " + str(maxVales[1]) + " Z: "+str(maxVales[2]))
    print("Min Values for each Coord")
    minVales = o.min(axis=0)
    print("X: " + str(minVales[0]) + " Y: " + str(minVales[1]) + " Z: "+str(minVales[2]))
extent(object.v)
# Todo: Part 4


# Run a loop to keep the program running
draw = False
while draw:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            draw = False

    # Clear the screen (or clear the color buffer), and set it to the background color chosen earlier
    glClear(GL_COLOR_BUFFER_BIT)

    # Refresh the display to show what's been drawn
    pg.display.flip()


pg.quit()   # Close the graphics window
quit()      # Exit the program