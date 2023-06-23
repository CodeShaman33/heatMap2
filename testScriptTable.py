import csv
import pandas
import numpy as np




# Create a 3x3 grid of empty lists
grid = [[[] for _ in range(3)] for _ in range(4)]

# Printing the grid
for row in grid:
    print(row)

print('----------------------------------------------------------------')

print((grid))

grid[0][1].append(33)
grid[2][1].append(33)
grid[3][1].append(33)

print((grid))