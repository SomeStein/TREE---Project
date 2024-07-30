import random
import numpy as np


def si_algo(agents, board_sizes, steps):

    n_rows, n_cols = board_sizes

    new_agents = agents.copy()

    ids = list(new_agents.keys())
    random.shuffle(ids)
    choices = random.choices(range(len(steps)), k=len(agents))

    for i, id in enumerate(ids):
        r, c = new_agents[id]
        a, b = steps[choices[i]]
        new_pos = (r+a) % n_rows, (c+b) % n_cols
        new_agents[id] = new_pos
    return new_agents


def seq_se_algo(agents, board_sizes, steps):

    n_rows, n_cols = board_sizes

    new_agents = agents.copy()

    ids = list(new_agents.keys())
    random.shuffle(ids)
    choices = random.choices(range(len(steps)), k=len(agents))

    for i, id in enumerate(ids):
        r, c = new_agents[id]
        a, b = steps[choices[i]]
        new_pos = (r+a) % n_rows, (c+b) % n_cols
        if new_pos in new_agents.values():
            new_pos = r, c
        new_agents[id] = new_pos
    return new_agents
