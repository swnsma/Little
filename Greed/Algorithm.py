from Validator import Validator
from Structures.Result import Result
import numpy


class Algorithm:

    INFINITY = 999999

    def __init__(self, matrix):
        self.validator = Validator()
        self.subject = matrix
        self.results = list()
        self.matrixes = list()

    def run(self):
        self.validator.set_subject(self.subject)
        if not self.validator.validate():
            print('Validation error. Please check source file.\n')
            return

        for i in range(len(self.subject)):
            m = list()
            for row in self.subject:
                m.append(list(row))
            self.matrixes.append(m)
        self.processMatixes()

    def processMatixes(self):
        i = 0
        for m in self.matrixes:
            way = list()
            rate = 0
            current = i
            for j in range(len(m) - 1):
                for k in range(len(m)):
                    m[k][current] = self.INFINITY
                way.append(current)
                v = min(m[current])
                current = numpy.argmin(m[current])
                rate += v
            self.results.append(Result(way, rate))
            i += 1

    def findMinResult(self):
        m = self.results.pop()
        while len(self.results):
            p = self.results.pop()
            if p.rate < m.rate:
                m = p

        return m

    def print_result(self):
        o = self.findMinResult()
        print('Length: ' + str(o.rate) + '\n')
        result = ''
        for i in o.path:
            result += str(i + 1) + ' -> '
        result += str(o.path[0] + 1)
        print(result)
