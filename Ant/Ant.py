from Structures.Pair import Pair


class Ant:

    def __init__(self, num):
        self.path = list()
        self.num = num
        self.current_city = 0
        self.L = 0.0
        self.allowed_cities = [i for i in range(0, self.num)]

    def move(self, j, length):
        self.path.append(Pair(self.current_city, j))
        self.current_city = j
        self.allowed_cities.remove(j)
        self.L += length

    def is_visited(self, i, j):
        for i in range(0, len(self.path)):
            point = self.path[i]
            if point.i == i and point.j == j:
                return True

        return False

    def set_coordinate(self, i):
        self.current_city = i
        self.allowed_cities.remove(i)

    def clean(self):
        self.current_city = 0
        self.L = 0.0
        self.allowed_cities = [i for i in range(0, self.num)]
