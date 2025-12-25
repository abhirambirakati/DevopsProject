# scheduler.py
# Disk Scheduling Algorithms Module
# Bugfix branch: fixed scheduler logic comment
# Main branch: scheduler baseline comment

class DiskScheduler:
    def __init__(self, requests, head, max_track):
        self.requests = requests
        self.head = head
        self.max_track = max_track

    def fcfs(self):
        """
        First Come First Served Disk Scheduling
        """
        sequence = [self.head] + self.requests
        seek_time = 0

        for i in range(1, len(sequence)):
            seek_time += abs(sequence[i] - sequence[i - 1])

        return sequence, seek_time

    def sstf(self):
        """
        Shortest Seek Time First Disk Scheduling
        """
        sequence = [self.head]
        requests = self.requests.copy()
        head = self.head
        seek_time = 0

        while requests:
            closest = min(requests, key=lambda x: abs(x - head))
            seek_time += abs(closest - head)
            head = closest
            sequence.append(closest)
            requests.remove(closest)

        return sequence, seek_time
