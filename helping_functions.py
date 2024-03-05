import sys
import time
import numpy as np
from collections import defaultdict
from scipy.sparse import coo_matrix


# helping function that gives a progressBar in terminal
def print_progress_bar(current_iteration, max_iteration, start_time):
    # Calculate progress percentage
    progress_percentage = ((current_iteration+1) / max_iteration) * 100

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Create the progress bar
    bar_length = 30
    progress = int(bar_length * (current_iteration+1) / max_iteration)
    bar = "[" + "=" * progress + " " * (bar_length - progress) + "]"

    # Print the progress bar and additional information
    sys.stdout.write("\rProgress: {:0.2f}% | {} | Elapsed Time: {:0.6f}s".format(
        progress_percentage, bar, elapsed_time))
    sys.stdout.flush()

# create a sparse matrix from frequency dictionary


def create_sparse_matrix(tuple_frequency):
    rows, cols = zip(*tuple_frequency.keys())
    data = list(tuple_frequency.values())
    matrix = coo_matrix((data, (rows, cols)))
    return matrix


# get frequency dictionary from list of lists of tuples
# def merge_lists_of_tuples(lists_of_tuples):
#     tuple_frequency = defaultdict(int)

#     # Count the frequency of each tuple
#     for lst in lists_of_tuples:
#         for tpl in lst:
#             tuple_frequency[tpl] += 1
#     return tuple_frequency

# def merge_lists_of_tuples(lists_of_tuples):
#     tuple_frequency = defaultdict(int)

#     # Count the frequency of each tuple
#     for lst in lists_of_tuples:
#         for tpl in lst:
#             tuple_frequency[tuple(tpl)] += 1
#     return tuple_frequency

# def merge_lists_of_tuples(list_of_ndarrays):
#     unique_tuples, counts = np.unique(np.concatenate(list_of_ndarrays), axis=0, return_counts=True)
#     # Combine unique tuples and their frequencies into a dictionary
#     return dict(zip(map(tuple, unique_tuples), counts))

# def merge_lists_of_tuples(list_of_ndarrays):
#     return np.concatenate(list_of_ndarrays)

# def merge_lists_of_tuples(list_of_ndarrays):
#     concat = np.concatenate(list_of_ndarrays)
#     concat_tups = [tuple(coords) for coords in concat]
#     tup_set = set(concat_tups)
#     return {tup: concat_tups.count(tup) for tup in tup_set }

# def merge_iterations(list_of_ndarrays):
#     return np.array([])
