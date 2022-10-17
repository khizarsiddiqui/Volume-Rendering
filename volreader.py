# first commit
# some of the topics covered in this project:
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