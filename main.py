import time
from types import DynamicClassAttribute, new_class
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

np.set_printoptions(suppress=True)


class Framework:

    def __init__(self, board_sizes):

        self.board_sizes = board_sizes
        self.state = np.zeros(board_sizes, dtype=np.uint8)
        self.agents = np.array([], dtype=np.int16)

    def add_agents(self, new_agents):

        if self.agents.size > 0:

            self.agents = np.vstack((self.agents, new_agents), dtype=np.int16)

        else:

            self.agents = new_agents

    def update_state(self):
        self.state = np.zeros(self.board_sizes, dtype=np.uint8)
        for coord in self.agents:
            self.state[*coord] += 1

    def update_agents(self, algo, directions):

        self.agents = algo(self.agents, self.board_sizes, directions)

    def simulate(self, n_steps, algo, verbose=False):

        directions = np.array(
            [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)], dtype=np.int16)

        if verbose:
            self.update_state()
            print(f"current state:\n{self.state}")

        for k in range(n_steps):
            self.update_agents(algo, directions)
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

        directions = np.array(
            [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)], dtype=np.int16)

        for k in range(n_steps):

            total = np.zeros(self.board_sizes)

            for i in range(n_iterations):

                iteration_agents[i] = algo(
                    iteration_agents[i], self.board_sizes, directions)
                for agent_coord in iteration_agents[i]:
                    total[*agent_coord] += 1

            steps_densities.append(total/n_iterations)

            if verbose:
                print(
                    f"step {k+1} out of {n_steps}: \n{np.round(total/n_iterations, 2)}\n")

            else:
                print(f"step {k+1} out of {n_steps}", end="\r")

        return steps_densities


def si_algo(agents, board_sizes, directions):

    random_indices = np.random.choice(len(directions), len(agents))

    return (agents + directions[random_indices]) % board_sizes


framework = Framework((20, 20))

framework.add_agents([(r, c) for r in range(6, 14) for c in range(6, 14)])

n_steps = 100
n_iterations = 10000

start = time.time()
steps_si = framework.monte_carlo(n_steps, n_iterations, si_algo)
print(f"took: {time.time() - start} seconds")
