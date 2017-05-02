
class Validator:
    INFINITY = 999999

    def __init__(self):
        self.matrix = list()

    def set_subject(self, matrix):
        self.matrix = matrix

    def validate_values(self):
        for row in self.matrix:
            for item in row:
                if item < 0:
                    return False
        return True

    def validate_cycles(self):
        for i in range(len(self.matrix)):
            if not self.matrix[i][i] == self.INFINITY:
                return False
        return True

    def validate_size(self):
        rows = len(self.matrix)
        for row in self.matrix:
            if len(row) != rows:
                return False
        return True

    def validate(self):
        return self.validate_size() and self.validate_values() and self.validate_cycles()
