# main.py
# Entry point of the Disk Scheduling Simulator application

import tkinter as tk
from ui import DiskSchedulingApp

def main():
    root = tk.Tk()
    app = DiskSchedulingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
