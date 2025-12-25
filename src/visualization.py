# visualization.py
# Disk head movement visualization

import matplotlib.pyplot as plt

def visualize_movement(sequence, algorithm_name):
    """
    Visualizes disk head movement for a given algorithm
    """
    steps = list(range(len(sequence)))

    plt.figure(figsize=(8, 4))
    plt.plot(sequence, steps, marker='o', linestyle='-')
    plt.xlabel("Track Number")
    plt.ylabel("Step")
    plt.title(f"{algorithm_name} Disk Head Movement")
    plt.grid(True)
    plt.show()
