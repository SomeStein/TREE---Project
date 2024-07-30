from timeit import default_timer as timer
from visuals import create_gif_from_matrices
import numpy as np
from framework import Framework
from algorithms import seq_se_algo, si_algo

# Todos
# optimize monte carlo
# use progress bar from rich

np.set_printoptions(suppress=True)

framework = Framework((40, 40))

framework.add_agents([(r, c) for r in range(6, 14) for c in range(6, 14)])

n_steps = 200
n_iterations = 1_000

start = timer()
si_matrices = framework.monte_carlo(n_steps, n_iterations, si_algo, True)
print(f"took: {str(timer() - start)} seconds")

# start = timer()
# steps_2 = framework.monte_carlo(n_steps, n_iterations, seq_se_algo, True)
# print(f"took: {str(timer() - start)} seconds")

create_gif_from_matrices(si_matrices)


# l2 norms and abs difference of states of si si, seq_se si, si seq_se, seq_se seq_se 1_000_000 iterations 100 steps for different inits
