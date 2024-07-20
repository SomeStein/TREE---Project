import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

np.set_printoptions(suppress=True)


class Framework:

    def __init__(self, board_sizes):

        self.board_sizes = board_sizes
        self.state = np.zeros(board_sizes, dtype=np.uint8)
        self.agents = {}

    def add_agent(self, agent):

        for i in range(len(self.agents)+1):
            if i not in self.agents:
                self.agents[i] = agent

    def add_agents(self, agents):

        m = 0
        for agent in agents:
            for i in range(m, len(self.agents)+1):
                if i not in self.agents:
                    self.agents[i] = agent
                    m = i+1

    def update_agents(self, algo):

        self.agents = algo(self.agents, self.board_sizes)

    def update_state(self):
        self.state = np.zeros(self.board_sizes, dtype=np.uint8)
        for agent_coord in self.agents.values():
            self.state[agent_coord] += 1

    def simulate(self, n_steps, algo, verbose=False):

        if verbose:
            self.update_state()
            print(f"current state:\n{self.state}")

        for k in range(n_steps):
            self.update_agents(algo)
            if verbose:
                self.update_state()
                print(f"step: {k+1} out of {n_steps} \n{self.state}")

    def monte_carlo(self, n_steps, n_iterations, algo, verbose=False):

        self.update_state()
        steps_densities = [self.state.copy()]

        if verbose:
            print(f"initial state: \n{self.state}\n")

        iteration_agents = []

        for i in range(n_iterations):
            iteration_agents.append(self.agents.copy())

        for k in range(n_steps):

            if not verbose:
                print(f"step {k+1} out of {n_steps}", end="\r")

            total = np.zeros(self.board_sizes)

            for i in range(n_iterations):

                iteration_agents[i] = algo(
                    iteration_agents[i], self.board_sizes)
                for agent_coord in iteration_agents[i].values():
                    total[agent_coord] += 1

            steps_densities.append(total/n_iterations)

            if verbose:
                print(
                    f"step {k+1} out of {n_steps}: \n{np.round(total/n_iterations, 2)}\n")

        return steps_densities


def si_algo(agents, board_sizes):

    n_rows, n_cols = board_sizes

    steps = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    new_agents = {}

    ids = list(agents.keys())
    random.shuffle(ids)

    for id in ids:
        r, c = agents[id]
        a, b = random.choice(steps)
        new_agents[id] = (r+a) % n_rows, (c+b) % n_cols

    return new_agents


def seq_se_algo(agents, board_sizes):

    n_rows, n_cols = board_sizes

    steps = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    new_agents = {}

    ids = list(agents.keys())
    random.shuffle(ids)

    for id in ids:
        r, c = agents[id]
        a, b = random.choice(steps)
        new_pos = (r+a) % n_rows, (c+b) % n_cols

        if new_pos in new_agents.values():

            new_agents[id] = agents[id]

        else:

            new_agents[id] = new_pos

    return new_agents


framework = Framework((20, 20))

framework.add_agents([(r, c) for r in range(6, 14) for c in range(6, 14)])

n_steps = 100
n_iterations = 10000

start = time.time()
steps_si = framework.monte_carlo(n_steps, n_iterations, si_algo)
print(f"took: {time.time() - start} seconds")

start = time.time()
steps_si = framework.monte_carlo(n_steps, n_iterations, seq_se_algo)
print(f"took: {time.time() - start} seconds")
# steps_se = framework.monte_carlo(n_steps, n_iterations, seq_se_algo)

# arrays = []


# for i in range(n_steps+1):
#     arrays.append(np.abs(steps_se[i] - steps_si[i]))


# fig, ax = plt.subplots()
# cax = ax.matshow(arrays[0], vmax=0.1)

# # Step 4: Create the update function


# def update(frame):
#     cax.set_array(arrays[frame])
#     return [cax]


# # Step 5: Create the animation object
# ani = FuncAnimation(fig, update, frames=len(arrays), blit=True)

# ani.save('matshow_animation.gif', writer='imagemagick')
