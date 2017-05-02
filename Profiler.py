import time


class Profiler:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = time.time()

    def start_tracking(self):
        self.start_time = time.time()

    def end_tracking(self):
        self.end_time = time.time()

    def get_time_delta_message(self):
        return 'Consumed: ' + str(self.end_time - self.start_time) + '\n'

    def get_time_delta(self):
        return self.end_time - self.start_time