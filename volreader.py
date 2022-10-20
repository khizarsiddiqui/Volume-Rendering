# first commit
# Some of the topics covered in this project:
# • Using GLSL for GPU computations
# • Creating vertex and fragment shaders
# • Representing 3D volumetric data and using the volume ray casting algorithm
# • Using numpy arrays for 3D transformation matrices

# There are various ways to render a 3D data set. In this project, you’ll use the volume ray casting method, 
# which is an image-based rendering technique used to generate the final image from the 2D slice, pixel by pixel.

# You’ll begin by generating a 3D texture from the volumetric data read in from the file. 
# Next you’ll look at a color cube technique for generating rays from the eye that point into the volume, 
# which is a key concept in implementing the volume ray casting algorithm. You’ll look at how to define
# the cube geometry as well as how to draw the back- and front-faces of this cube. 
# You’ll then explore the volume ray casting algorithm and the associated vertex and fragment shaders. 
# Finally, you’ll learn how to implement 2D slicing of the volumetric data.

# The first step is to read the volumetric data from a folder containing images
"""
Utilities for reading 3D volumetric data as a 3D OpenGL texture.
"""

import os
import numpy as np
from PIL import Image

import OpenGL
from OpenGL.GL import *

from scipy import misc

def loadVolume(dirName):
    """read volume from directory as a 3D texture"""
    # list images in directory
    files = sorted(os.listdir(dirName))
    print('loading mages from: %s' % dirName)
    imgDataList = []
    count = 0
    width, height = 0, 0
    for file in files:
        file_path = os.path.abspath(os.path.join(dirName, file))
        try:
            # read image
            img = Image.open(file_path)
            imgData = np.array(img.getdata(), np.uint8)

            # check if all are of the same size
            if count is 0:
                width, height = img.size[0], img.size[1] 
                imgDataList.append(imgData)
            else:
                if (width, height) == (img.size[0], img.size[1]):
                    imgDataList.append(imgData)
                else:
                    print('mismatch')
                    raise RuntimeError("image size mismatch")
            count += 1
            #print img.size            
        except:
            # skip
            print('Invalid image: %s' % file_path)

    # load image data into single array
    depth = count
    data = np.concatenate(imgDataList)
    print('volume data dims: %d %d %d' % (width, height, depth))

    # load data into 3D texture
    texture = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glBindTexture(GL_TEXTURE_3D, texture)
    glTexParameterf(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_3D, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage3D(GL_TEXTURE_3D, 0, GL_RED, 
                 width, height, depth, 0, 
                 GL_RED, GL_UNSIGNED_BYTE, data)
    #return texture
    return (texture, width, height, depth)


# load texture
def loadTexture(filename):
    img = Image.open(filename)
    img_data = np.array(list(img.getdata()), 'B')
    texture = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1], 
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture