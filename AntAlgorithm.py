from Reader import Reader
from Ant.Algorithm import Algorithm
from Profiler import Profiler


class Process:
    def __init__(self):
        self.reader = Reader()
        self.profiler = Profiler()

    def execute(self, a, b, p, ant_n, t_max, q):
        source = self.reader.read_source()
        while source:
            self.profiler.start_tracking()
            alg = Algorithm(source.matrix, a, b, p, ant_n, t_max, q)
            alg.run()
            alg.print_result()
            self.profiler.end_tracking()
            print(self.profiler.get_time_delta_message())
            source = self.reader.read_source()
            break


process = Process()

a = 1
b = 1
p = 0.05
ant_n = 7
t_max = 50
q = 5

process.execute(a, b, p, ant_n, t_max, q)
