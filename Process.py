from Reader import Reader
from Little import Little
from Profiler import Profiler


class Process:
    def __init__(self):
        self.reader = Reader()
        self.profiler = Profiler()

    def execute(self):
        source = self.reader.read_source()
        while source:
            self.profiler.start_tracking()
            little = Little(source)
            little.run()
            little.print_result()
            self.profiler.end_tracking()
            print(self.profiler.get_time_delta_message())
            source = self.reader.read_source()


process = Process()
process.execute()
