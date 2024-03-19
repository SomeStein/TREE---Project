from simulation import *
import cProfile


width = 60000
height = 60000
size = (height, width)
i = 10000
s = 30
n = 1000

# Create a cProfile object
profiler = cProfile.Profile()

# Run the simulation method with profiling
profiler.enable()

init = [(2, 2)]*n
print("\ni: ", i, " s: ", s, " n: ", n)
framework = Framework(size, init, s, i)
sparse_matrices_list, took1 = framework.monte_carlo(
    size_inclusion_random_walk_np)

profiler.disable()

# Print the profiling results
profiler.print_stats(sort='tottime')

# for sparse_matrix in sparse_matrices_list:
#     print(sparse_matrix.toarray(), "\n")
