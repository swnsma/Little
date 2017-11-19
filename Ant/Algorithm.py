from Validator import Validator
from Ant.Ant import Ant
from random import shuffle, random


class Algorithm:

    INFINITY = 999999

    def __init__(self, matrix, alpha, beta, p, ants_n, t_max, Q):
        self.validator = Validator()
        self.subject = matrix
        self.alpha = alpha
        self.beta = beta
        self.p = p
        self.Q = Q
        self.L = self.INFINITY
        self.path = list()
        self.ants_n = ants_n
        self.t_max = t_max
        self.cities = len(self.subject)
        self.ants = list()
        for i in range(0, self.ants_n):
            a = Ant(self.cities)
            self.ants.append(a)

        self.pheromones = list()
        for i in range(0, len(self.subject)):
            self.pheromones.append(list())
            for j in range(0, len(self.subject[i])):
                if i == j:
                    self.pheromones[i].append(0)
                else:
                    self.pheromones[i].append(1.0)

    def run(self):
        self.validator.set_subject(self.subject)
        if not self.validator.validate():
            print('Validation error. Please check source file.\n')
            return
        for t in range(0, self.t_max):
            x = [i for i in range(0, self.cities)]
            shuffle(x)
            x = x[0:self.ants_n]

            for a in range(0, self.ants_n):
                ant = self.ants[a]
                ant.clean()
                ant.set_coordinate(x[a])
                while len(ant.allowed_cities) > 1:
                    prob = self.probability_vector(ant)
                    random_number = random()
                    random_rate = 0.0
                    selected_city = 0
                    for key in prob:
                        if random_rate + prob[key] < random_number:
                            random_rate += prob[key]
                        else:
                            selected_city = key
                            break
                    ant.move(selected_city, self.subject[ant.current_city][selected_city])
                selected_city = ant.allowed_cities[0]
                ant.move(selected_city, self.subject[ant.current_city][selected_city])
            self.recalculate_pheromones()
            for a in range(0, self.ants_n):
                if self.ants[a].L < self.L:
                    self.L = self.ants[a].L
                    self.path = self.ants[a].path

    def probability_vector(self, ant):
        probability = {}
        for city in ant.allowed_cities:
            impact = 0
            for c in ant.allowed_cities:
                impact += self.calc_impact(ant.current_city, c)
            probability[city] = self.calc_impact(ant.current_city, city) / impact

        a = 0.0
        for i in probability:
            a += probability[i]
        return probability

    def recalculate_pheromones(self):
        recalculate = {}
        for i in range(0, len(self.subject)):
            for j in range(0, len(self.subject[i])):
                if i != j:
                    if not ((i in recalculate.keys() and j in recalculate[i]) or (j in recalculate.keys() and i in recalculate[j])):
                        delta_tau = 0.0
                        for ant in self.ants:
                            if ant.is_visited(i, j) or ant.is_visited(j, i):
                                delta_tau += float(self.Q) / float(ant.L)
                        self.pheromones[i][j] = (1 - self.p) * self.pheromones[i][j] + delta_tau
                        self.pheromones[j][i] = (1 - self.p) * self.pheromones[j][i] + delta_tau
                        if not i in recalculate.keys():
                            recalculate[i] = list()
                        recalculate[i].append(j)

    def calc_impact(self, start, end):
        return pow(self.pheromones[start][end], self.alpha) * pow(1 / self.subject[start][end], self.beta)

    def print_result(self):
        print('Length: ' + str(self.L) + '\n')
        result = str(self.path[0].i + 1) + ' -> '
        for i in self.path:
            result += str(i.j + 1) + ' -> '
        result += str(self.path[0].i + 1)
        print(result)