import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from matplotlib.animation import PillowWriter

# Assuming you have a list of numpy arrays called matrices
# Example:
# matrices = [np.random.rand(10, 10) for _ in range(10)]

# Function to animate the matrices and save as GIF


def create_gif_from_matrices(matrices, output_file='animation.gif', interval=200):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.matshow(matrices[frame], vmax=1.2, vmin=0)
        ax.set_title(f'Frame {frame + 1}')
        ax.axis('off')

    ani = matplotlib.animation.FuncAnimation(
        fig, update, frames=len(matrices), interval=interval
    )

    ani.save(output_file, writer=PillowWriter(fps=1000 / interval))
    plt.close(fig)

