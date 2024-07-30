from timeit import default_timer as timer
import framework
from visuals import create_gif_from_matrices
import numpy as np
from framework import Framework
from algorithms import seq_se_algo, si_algo

# Todos
# optimize monte carlo
# use progress bar from rich

np.set_printoptions(suppress=True)

# framework = Framework((20, 20))

# framework.add_agents([(r, c) for r in range(6, 14) for c in range(6, 14)])

framework = Framework((5, 5))
framework.add_agents([(2, 2)])

n_steps = 10
n_iterations = 10_000_000

start = timer()
si_matrices = framework.monte_carlo(n_steps, n_iterations, si_algo, True)
print(f"took: {str(timer() - start)} seconds")

start = timer()
seq_se_matrices = framework.monte_carlo(
    n_steps, n_iterations, seq_se_algo, True)
print(f"took: {str(timer() - start)} seconds")

create_gif_from_matrices(
    si_matrices, f"graphs/si_matrices_s{n_steps}_i{n_iterations}.gif")
create_gif_from_matrices(
    seq_se_matrices, f"graphs/seq_se_matrices_s{n_steps}_i{n_iterations}.gif")

# l2 norms and abs difference of states of si si, seq_se si, si seq_se, seq_se seq_se 1_000_000 iterations 100 steps for different inits
