# ui.py
# User Interface for Disk Scheduling Simulator

import tkinter as tk
from scheduler import DiskScheduler
from visualization import visualize_movement
from utils import ToolTip

class DiskSchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Simulator")

        self.create_widgets()

    def create_widgets(self):
        # Label
        label = tk.Label(self.root, text="Disk Scheduling Simulator", font=("Arial", 14))
        label.pack(pady=10)

        # Button
        run_button = tk.Button(self.root, text="Run FCFS Algorithm", command=self.run_fcfs)
        run_button.pack(pady=5)

        # Tooltip
        ToolTip(run_button, "Click to run FCFS disk scheduling algorithm")

    def run_fcfs(self):
        requests = [98, 183, 37, 122, 14, 124]
        head = 50
        max_track = 200

        scheduler = DiskScheduler(requests, head, max_track)
        sequence, seek_time = scheduler.fcfs()

        visualize_movement(sequence, "FCFS")
