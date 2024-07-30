import numpy as np


class Framework:

    def __init__(self, board_sizes):

        self.board_sizes = board_sizes
        self.state = np.zeros(board_sizes, dtype=np.uint8)
        self.agents = {}
        self.steps = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    def add_agents(self, new_agents):
        for agent in new_agents:
            id = len(self.agents)
            for i in range(len(self.agents)):
                if i not in self.agents:
                    id = i
                    break
            self.agents[id] = agent

    def update_agents(self, algo):

        self.agents = algo(self.agents, self.board_sizes)

    def update_state(self):
        self.state = np.zeros(self.board_sizes, dtype=np.uint8)
        for agent_coord in self.agents:
            self.state[*agent_coord] += 1

    def simulate(self, n_steps, algo, verbose=False):

        steps = [self.agents.copy()]

        if verbose:
            self.update_state()
            print(f"current state:\n{self.state}")

        for k in range(n_steps):
            self.update_agents(algo)
            steps.append(self.agents.copy())
            if verbose:
                self.update_state()
                print(f"step: {k+1} out of {n_steps} \n{self.state}")

        return steps

    # def monte_carlo(self, n_steps, n_iterations, algo, verbose=False):

    #     # Assuming board_sizes is a tuple (height, width)
    #     board_height, board_width = self.board_sizes
    #     steps_densities = np.zeros(
    #         (n_steps + 1, board_height, board_width))

    #     for i in range(n_iterations):
    #         if i % 1000 == 0:
    #             print(f"{i} out of {n_iterations}", end="\r")
    #         agents = self.agents.copy()

    #         for k in range(1, n_steps + 1):
    #             # Update agents positions (vectorized)
    #             agents = algo(agents, self.board_sizes, self.steps)

    #             v_agents = np.array(list(agents.values()))

    #             # Update steps_densities using numpy advanced indexing
    #             steps_densities[k, v_agents[:, 0], v_agents[:, 1]] += 1
    #         steps_densities[k] /= np.sum(steps_densities[k])

    #     return steps_densities

    def monte_carlo(self, n_steps, n_iterations, algo, verbose=False):

        steps_densities = []
        for k in range(n_steps + 1):
            steps_densities.append({})

        for i in range(n_iterations):
            if i % 1000 == 0:
                print(f"{i} out of {n_iterations}", end="\r")
            agents = self.agents.copy()

            for agent in agents.values():
                if agent in steps_densities[0]:
                    steps_densities[0][agent] += 1
                else:
                    steps_densities[0][agent] = 1

            for k in range(1, n_steps + 1):
                # Update agents positions (vectorized)
                agents = algo(agents, self.board_sizes, self.steps)
                for agent in agents.values():
                    if agent in steps_densities[k]:
                        steps_densities[k][agent] += 1
                    else:
                        steps_densities[k][agent] = 1

        matrices = []

        for k in range(n_steps+1):
            mat = np.zeros(self.board_sizes)
            for agent in steps_densities[k]:
                mat[agent] = steps_densities[k][agent]
            matrices.append(mat)

        return matrices
