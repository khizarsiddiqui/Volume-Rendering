# Volume-Rendering
Implementing the volume ray casting algorithm using Python and OpenGL.

Volume rendering is a computer graphics technique used to construct 3D images from this type of volumetric data. 
Although volume rendering is commonly used to analyze medical scans, it can also be used to create 3D scientific visualizations in academic disciplines such as geology, archeology, and molecular biology.

NOTE: In OpenGL, a color can be represented as a strip of 8-bit unsigned values (r, g, b), where r, g, and b are in the range [0, 255].
It can also be represented as a 32-bitfloating-point value (r, g, b), where r, g, and b are in the range [0.0, 1.0]. These representations are equivalent. 
For example, the red color (255, 0, 0) in the former is the same as (1.0, 0.0, 0.0) in the latter.

# Back-Face Culling
In OpenGL, when you draw a primitive like a quad, the order in which you
specify the vertices is important. By default, OpenGL assumes an ordering of
GL_CCW, or counterclockwise. For a primitive with counterclockwise ordering,
the normal vector will point “out” of the polygon. This becomes relevant when
you try to draw geometry with closed areas, such as a cube. To optimize your
rendering, you cannot draw invisible sides by turning on OpenGL back-face
culling to compute the dot product of your view direction vector with the normal
vector of the polygon. For back-facing polygons, the dot product will be negative,
and those faces can be dropped. OpenGL also provides an easy way to
do the inverse—cull the front-faces, which is what you use in your algorithm.

For understanding glTexParameter():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glTexParameter.xhtml

For understanding glTexImage3D():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glTexImage3D.xhtml

# RayCube
The color cube has six faces, each of which can each be drawn as two triangles for a total of 6×6, or 36, vertices. But rather than specify all 36 vertices, you specify the cube’s eight vertices and then define the triangles using an indices array.

For understanding glVertexAttribPointer():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml

For understanding glTexImage2D():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glTexImage2D.xhtml

For understanding glFramebufferTexture2D():https://registry.khronos.org/OpenGL-Refpages/es2.0/xhtml/glFramebufferTexture2D.xml

For understanding glBindRenderbuffer():https://registry.khronos.org/OpenGL-Refpages/es2.0/xhtml/glBindRenderbuffer.xml

For understanding glRenderbufferStorage():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glRenderbufferStorage.xhtml

For understanding glFramebufferRenderbuffer():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glFramebufferRenderbuffer.xhtml

To understand the concept of face-culling:https://learnopengl.com/Advanced-OpenGL/Face-culling

For understanding gl_Position():https://registry.khronos.org/OpenGL-Refpages/gl4/html/gl_Position.xhtml

To understand orthographic & perspective projections:https://www.cprogramming.com/tutorial/opengl_projections.html

# Slice-Render vertex shader
Because you are slicing perpendicular to the x direction, you want a slice parallel to the yz plane. The 3D vertices coming in to the vertex shader also double as the 3D texture coordinates because they are in the range [0, 1], so the texture coordinates are given as (f, Vx, Vy), where f is the fraction of the slice number in the direction of the x-axis and where Vx and Vy are the vertex coordinates. Unfortunately, the resulting image will appear upside down because the OpenGL coordinate system has its origin at the bottom left, with the y direction pointing up; this is the reverse of what you want. To resolve this problem, you change the texture coordinate t to (1 – t) and use (f, Vx, 1 − Vy).

# Volrender
I’m choosing not to pass in the glfw.KEY values directly and using a dictionary to convert these to character values instead, because it’s good practice to reduce dependencies in source files. Currently, the only file in this project that depends on GLFW is volrender.py. If you were to pass GLFW-specific types into other code, they would need to import and depend on the GLFW library, but if you were to switch to yet another OpenGL windowing toolkit, the code would become messy.