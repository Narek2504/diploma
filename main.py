import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def diamond_square(size, roughness):
    terrain = np.zeros((size, size))
    
    terrain[0, 0] = np.random.rand()
    terrain[0, -1] = np.random.rand()
    terrain[-1, 0] = np.random.rand()
    terrain[-1, -1] = np.random.rand()
    
    step_size = size - 1
    displacement = roughness
    
    while step_size > 1:
        half_step = step_size // 2
        
        for x in range(0, size - 1, step_size):
            for y in range(0, size - 1, step_size):
                avg = (terrain[x, y] + 
                       terrain[x + step_size, y] +
                       terrain[x, y + step_size] + 
                       terrain[x + step_size, y + step_size]) / 4.0
                terrain[x + half_step, y + half_step] = avg + (np.random.rand() - 0.5) * displacement
        
        for x in range(0, size, half_step):
            for y in range((x + half_step) % step_size, size, step_size):
                s = []
                if x - half_step >= 0:
                    s.append(terrain[x - half_step, y])
                if x + half_step < size:
                    s.append(terrain[x + half_step, y])
                if y - half_step >= 0:
                    s.append(terrain[x, y - half_step])
                if y + half_step < size:
                    s.append(terrain[x, y + half_step])
                
                terrain[x, y] = np.mean(s) + (np.random.rand() - 0.5) * displacement
        
        step_size = half_step
        displacement *= 0.5
        
    return terrain

size = 129
roughness = 1.0

terrain = diamond_square(size, roughness)

X = np.arange(0, size)
Y = np.arange(0, size)
X, Y = np.meshgrid(X, Y)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, terrain, cmap='terrain', linewidth=0, antialiased=True)
ax.set_title("3D Fractal Landscape (Diamond-Square)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Height")
plt.show()

