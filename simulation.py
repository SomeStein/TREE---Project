
from agent_algos import *
from helping_functions import *
import numpy as np


class Framework:

    def __init__(self, size, init=[], n_steps=100):

        self.size = np.array(size, dtype=np.uint16)
        self.init = np.array(init, dtype=np.uint16)
        self.n_steps = n_steps

    def merge_iterations(self, array_list):

        # Concatenate all arrays into a single 2D array
        concatenated_array = np.concatenate(
            array_list, axis=0, dtype=np.int32)

        # Create a coo_matrix directly without searching for unique coordinates
        sparse_matrix = coo_matrix((
            np.ones(concatenated_array.shape[0], dtype=np.uint8),  # data
            (concatenated_array[:, 0],                              # rows
             concatenated_array[:, 1])),                            # columns
            dtype=np.uint32,
            shape=self.size)

        # Convert the coo_matrix to csr_matrix if needed (sums duplicates automatically)
        return sparse_matrix.tocsr()

    def monte_carlo(self, algo, n_iterations=100):

        start_time = time.time()

        self.pos_array_list = []
        self.next_pos_array_list = []
        self.sparse_matrices_list = []

        # init (step 0 init sparse matrix for every iteration)
        sparse_matrix_step0 = self.merge_iterations(
            [self.init]*n_iterations)
        self.sparse_matrices_list.append(sparse_matrix_step0)

        # first step saved in next_pos_lists
        for i in range(n_iterations):
            self.next_pos_array_list.append(algo(self.init, self.size))

        self.sparse_matrices_list.append(
            self.merge_iterations(self.next_pos_array_list))

        self.pos_array_list = self.next_pos_array_list

        # step 2 to n_steps
        for k in range(2, self.n_steps+1):

            # for all iterations calculate all new position arrays
            for i in range(n_iterations):
                position_array = self.pos_array_list[i]
                self.next_pos_array_list[i] = algo(position_array, self.size)

            # merge to a frequency list and store
            sparse_matrix = self.merge_iterations(self.next_pos_array_list)
            self.sparse_matrices_list.append(sparse_matrix)

            # switch next and current position array lists
            self.pos_array_list = self.next_pos_array_list

            print_progress_bar(k, self.n_steps + 1, start_time)

        return self.sparse_matrices_list, time.time() - start_time
