import random
from simulation import *
import matplotlib.pyplot as plt


width = 60
height = 60
size = (height, width)
i = 1000
s = 5

init = [(x, y) for x in range(20, 40) for y in range(20, 40)]
print("\ni: ", i, " s: ", s)
framework = Framework(size, init, s)
sparse_matrices_list, took1 = framework.monte_carlo(
    size_exclusion_random_walk_np, i)

print("Took", took1)


for sparse_matrix in sparse_matrices_list:
    matrix = sparse_matrix.toarray()
    plt.matshow(matrix)
    plt.show()
