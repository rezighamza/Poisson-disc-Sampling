"""
Description: This script is used to generate a Poisson disk sampling of 1000 points in a 300x300 grid.
thanks to video Coding Challenge #33: Poisson-disc Sampling by Daniel Shiffman for the inspiration
the approach is based on the paper "Fast Poisson Disk Sampling in Arbitrary Dimensions" by Robert Bridson (2007)
it is might be different from the implementation in the video but the idea is the same
"""
# start a timer to see how long it takes to plot 1000 points
import time
import numpy as np
import random
import pygame
start = time.time()
# Start Poisson disk sampling
# Step 0:
r = 10
k = 30
w = r / np.sqrt(2)  # cell width
rows = int(300 / w)
cols = int(300 / w)
grid = [-1] * (rows * cols)

# Step 1:
x = random.randint(0, 300)
y = random.randint(0, 300)
i = int(x / w)
j = int(y / w)
grid[i + j * cols] = (x, y)  # Assign the (x, y) tuple to the grid
active = [(x, y)]


# Helper function to check distance
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Step 2:
while active:
    current = random.choice(active)
    for _ in range(k):
        angle = random.uniform(0, 2 * np.pi)
        d = random.uniform(r, 2 * r)
        new_x = current[0] + d * np.cos(angle)
        new_y = current[1] + d * np.sin(angle)
        if 0 <= new_x < 300 and 0 <= new_y < 300:
            ni = int(new_x / w)
            nj = int(new_y / w)
            # Ensure ni and nj are within the bounds
            if 0 <= ni < cols and 0 <= nj < rows and grid[ni + nj * cols] == -1:
                too_close = False
                for ii in range(max(0, ni - 1), min(cols, ni + 2)):
                    for jj in range(max(0, nj - 1), min(rows, nj + 2)):
                        neighbor = grid[ii + jj * cols]
                        if neighbor != -1 and distance((new_x, new_y), neighbor) < r:
                            too_close = True
                            break
                    if too_close:
                        break
                if not too_close:
                    grid[ni + nj * cols] = (new_x, new_y)
                    active.append((new_x, new_y))
    active.remove(current)

end = time.time()
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Poisson Disk Sampling')
screen.fill((255, 255, 255))

# Draw the points
points = [p for p in grid if p != -1]
for point in points:
    pygame.draw.circle(screen, (0, 0, 255), (int(point[0]), int(point[1])), 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

print("Time taken to plot is: ", end - start, " seconds")
