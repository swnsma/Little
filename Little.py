from Structures.Pair import Pair
from Structures.ListPair import ListPair
from Validator import Validator
from Structures.Result import Result


class Little:

    INFINITY = 999999

    def __init__(self, matrix):
        self.validator = Validator()
        self.subject = matrix
        self.optima = Result('', self.INFINITY)
        self.matrixes = list()

    def run(self):
        self.validator.set_subject(self.subject.matrix)
        if not self.validator.validate():
            print('Validation error. Please check source file.\n')
            return
        self.matrixes.append(self.subject.simplify())
        while self.matrixes:
            top = self.matrixes.pop()
            pair = self.find_division_pair(top)
            div = self.divide(top, pair)
            if div['first'].rate < self.optima.rate:
                self.matrixes.append(div['first'].simplify())
            if div['second'].is_ready() and div['second'].rate < self.optima.rate:
                div['second'] = div['second'].simplify()
                self.optima = Result(div['second'].harvest(), div['second'].rate)
                self.matrixes = [m for m in self.matrixes if m.rate < self.optima.rate]
            else:
                if div['second'].rate < self.optima.rate:
                    self.matrixes.append(div['second'].simplify())
        return True

    def divide(self, matrix, pair):
        second = matrix.copy()
        second.check_cycles(pair)
        second.append_path(pair)
        second.remove_path(pair)
        matrix.matrix[pair.i][pair.j] = self.INFINITY
        return {'first': matrix, 'second': second}

    def find_division_pair(self, m):
        rates = ListPair()
        matrix = m.matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    c1 = self.INFINITY
                    c2 = self.INFINITY
                    for k in range(len(matrix[i])):
                        if c1 > matrix[i][k] and k != j:
                            c1 = matrix[i][k]
                    for z in range(len(matrix)):
                        if c2 > matrix[z][j] and z != i:
                            c2 = matrix[z][j]
                    rates.append(Pair(i, j, c1 + c2))

        return rates.max()

    def print_result(self):
        print('Length: ' + str(self.optima.rate) + '\n')
        print(self.optima.get_path_string())
