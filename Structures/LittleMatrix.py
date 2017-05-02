from copy import copy
from Structures.Pair import Pair


class LittleMatrix:
    INFINITY = 999999

    def __init__(self, init, rate, col_index=None, row_index=None, path=None):
        self.matrix = init
        self.rate = rate
        if col_index is None:
            self.col_index = [i for i in range(len(self.matrix))]
        else:
            self.col_index = col_index
        if row_index is None:
            self.row_index = [i for i in range(len(self.matrix))]
        else:
            self.row_index = row_index
        if path is None:
            self.path = {}
        else:
            self.path = path

    def remove_path(self, pair):
        self.col_index = self.col_index[:pair.j] + self.col_index[pair.j + 1:]
        self.row_index = self.row_index[:pair.i] + self.row_index[pair.i + 1:]

        for i in range(len(self.matrix)):
            del self.matrix[i][pair.j]

        del self.matrix[pair.i]

    def append_path(self, pair):
        real_pair = Pair(self.row_index[pair.i], self.col_index[pair.j])
        self.path[real_pair.i] = real_pair.j

    def is_ready(self):
        if len(self.row_index) == 2 and len(self.col_index) == 2:
            return True
        else:
            return False

    def harvest(self):
        if self.matrix[0][0] > self.matrix[0][1]:
            self.path[self.row_index[0]] = self.col_index[1]
            self.path[self.row_index[1]] = self.col_index[0]
        else:
            self.path[self.row_index[0]] = self.col_index[0]
            self.path[self.row_index[1]] = self.col_index[1]

        return self.path

    def copy(self):
        duplicate = list()
        for row in self.matrix:
            duplicate.append(list(row))
        return LittleMatrix(duplicate,
                            copy(self.rate),
                            copy(self.col_index),
                            copy(self.row_index),
                            copy(self.path))

    def simplify(self):
        d = 0
        for i in range(len(self.matrix)):
            min_row = min(self.matrix[i])
            d += min_row
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] -= min_row

        for j in range(len(self.matrix[0])):
            min_col = self.INFINITY
            for i in range(len(self.matrix)):
                if self.matrix[i][j] < min_col:
                    min_col = self.matrix[i][j]
            d += min_col
            for i in range(len(self.matrix)):
                self.matrix[i][j] -= min_col
        if self.rate != self.INFINITY:
            self.rate += d
        else:
            self.rate = d
        return self

    def check_cycles(self, pair):
        real_pair = Pair(self.row_index[pair.i], self.col_index[pair.j])

        if not self.path:
            self.matrix[pair.j][pair.i] = self.INFINITY
            return

        flag = True
        from_entry = real_pair.i
        to_end = real_pair.j
        while flag:
            flag = False
            if to_end in self.path:
                to_end = self.path[to_end]
                flag = True
            if from_entry in self.path.values():
                from_entry = list(self.path.keys())[list(self.path.values()).index(from_entry)]
                flag = True
        self.matrix[self.row_index.index(to_end)][self.col_index.index(from_entry)] = self.INFINITY
