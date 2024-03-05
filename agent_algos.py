'''
from list of positions to new list of positions in the form of [(,),...,(,)]
'''
import random
import time
import numpy as np

rng = np.random.default_rng()


def size_inclusion_random_walk(agents, size):
    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n = size
    return [((x + dx) % m, (y + dy) % n) for x, y in agents for dx, dy in [random.choice(directions)]]


def size_inclusion_random_walk_np(agents, size):

    directions = np.array(
        [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]).astype(np.int16)

    random_directions = np.random.choice(len(directions), len(agents))

    return (agents + directions[random_directions]) % size


def size_exclusion_random_walk_np(pos_array, size):

    directions = np.array([(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)])

    random_indices = np.random.choice(len(directions), len(pos_array))

    new_pos_array = pos_array.copy()

    for i in range(len(pos_array)):
        new_pos = (pos_array[i, :] + directions[random_indices[i]]) % size
        if not any(np.equal(new_pos_array, new_pos).all(1)):
            new_pos_array[i] = new_pos

    return new_pos_array
