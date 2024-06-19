# Poisson Disk Sampling

# Description

This script generates a Poisson disk sampling of points in a 300x300 grid using Pygame for visualization. The approach is inspired by Daniel Shiffman's video [Coding Challenge #33: Poisson-disc Sampling](https://thecodingtrain.com/CodingChallenges/033.1-poisson-disc-sampling.html) and based on the paper ["Fast Poisson Disk Sampling in Arbitrary Dimensions" by Robert Bridson (2007).](https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf)

Although the implementation might differ from the video, the underlying idea remains the same.

# Features

- Generates a Poisson disk sampling of points within a 300x300 grid.
- Visualizes the points using Pygame.
- Measures and displays the time taken to generate the points.

# Requirements

- Python 3.x
- Pygame
- NumPy

# Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/poisson-disk-sampling.git
    cd poisson-disk-sampling
    ```

2. Install the required packages:
    ```sh
    pip install numpy pygame
    ```

# Usage

Run the script to generate and visualize the Poisson disk sampling points:

```sh
python script.py
```
# How It Works
## Initialization:

   - Define the parameters for the Poisson disk sampling algorithm.
   - Initialize the grid and the active list. 
## Poisson Disk Sampling:
- Randomly select a point and add it to the grid and active list.
          Iteratively generate new points around the active points and check if they can be added to the grid based on the distance criteria.
          Visualization:

- Use Pygame to draw the generated points in a 300x300 window.
     Timing:

-  Measure and print the time taken to generate the points.


# Acknowledgments
Inspired by [Coding Challenge #33: Poisson-disc Sampling](https://thecodingtrain.com/CodingChallenges/033.1-poisson-disc-sampling.html)

Based on the paper ["Fast Poisson Disk Sampling in Arbitrary Dimensions" by Robert Bridson (2007).](https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf)