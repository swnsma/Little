from Structures.Pair import Pair


class ListPair:
    def __init__(self):
        self.data = list()
        self.pointer = 0

    def __iter__(self):
        return self.data

    def append(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def __getitem__(self, key):
        return self.data[key]

    def max(self):
        max_pair = Pair(0, 0, 0)
        for pair in self.data:
            if pair.rate >= max_pair.rate:
                max_pair = pair

        return max_pair

    def min(self):
        min_pair = Pair(0, 0, 0)
        for pair in self.data:
            if pair.rate < min_pair.rate:
                min_pair = pair

        return min_pair
