from sim.board import Board
from sim.objects import Agent
import numpy as np
import random


class Framework:
    def __init__(self, board: Board) -> None:
        self.init_board = board
        self.state = board

    def simulate(self, num_steps: int = 0):

        objects = self.init_board.get_objects()

        agent_positions = [np.array(obj_list[i].pos)
                           for obj_list in objects.values() for i in range(len(obj_list)) if isinstance(obj_list[i], Agent)]

        agent_positions = np.row_stack(agent_positions, dtype=np.int16)

        # Define the possible movement vectors
        movement_vectors = np.array([
            [0, 0],
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ], dtype=np.int16)

        # Randomly select a movement vector for each agent
        random_indices = random.choices(
            range(len(movement_vectors)), k=agent_positions.shape[0]*num_steps)

        l = agent_positions.shape[0]

        for k in range(num_steps):

            # Get the selected movement vectors
            movements = movement_vectors[random_indices[k * l: (k+1)*l]]

            # Update the positions
            agent_positions += movements
