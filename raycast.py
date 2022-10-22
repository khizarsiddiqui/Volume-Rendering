# Volume Ray Casting
"""
This module has the classed and methods related to Volume rendering using the Ray Casting method.
"""

import OpenGL
from OpenGL.GL import *
from OpenGL.GL.shaders import *

import numpy as np
import math, sys 

import raycube, glutils, volreader

class Camera:
    """helper class for viewing"""
    def __init__(self):
        self.r = 1.5
        self.theta = 0
        self.center = [0.5, 0.5, 0.5]
        self.eye = [0.5 + self.r, 0.5, 0.5]
        self.up = [0.0, 0.0, 1.0]

    def rotate(self, clockWise):
        """rotate eye by one step"""
        if clockWise:
            self.theta = (self.theta + 5) % 360
        else:
            self.theta = (self.theta - 5) % 360
        # recalculate eye
        self.eye = [0.5 + self.r*math.cos(math.radians(self.theta)), 
                    0.5 + self.r*math.sin(math.radians(self.theta)), 
                    0.5]

class RayCastRender:
    """class that does Ray Casting"""

    def __init__(self, width, height, volume):
        """RayCastRender constructor"""
        
        # create RayCube object
        self.raycube = raycube.RayCube(width, height)
        
        # set dims
        self.width = width
        self.height = height
        self.aspect = width/float(height)

        # create shader
        self.program = glutils.loadShaders(strVS, strFS)
        # texture(to set the OpenGL 3D texture and dimensions)
        self.texVolume, self.Nx, self.Ny, self.Nz = volume
        
        # initialize camera
        self.camera = Camera()