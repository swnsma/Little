import glob
from Structures.LittleMatrix import LittleMatrix


class Reader:
    def __init__(self):
        self.files = glob.glob('source/*.little')

    def get_all_files(self):
        return self.files

    def get_file(self):
        if not len(self.files):
            return False

        return self.files.pop()

    def read_source(self):
        try:
            file = self.get_file()
            if file:
                print('Read file: ' + file + '\n')
            else:
                return False
            source = open(file, 'r')
            line = source.readline()
            matrix = list()
            while line:
                row = line.split(' ')
                row = [int(num) for num in row]
                matrix.append(row)
                line = source.readline()
            matrix = LittleMatrix(matrix, 999999)
            return matrix
        except (FileNotFoundError, IOError, OSError) as e:
            return False
