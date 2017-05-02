import random


class Generator:
    def __init__(self, size):
        self.size = size

    def generate(self):
        source = list()
        for i in range(self.size):
            source.append(list())
            for j in range(self.size):
                if i == j:
                    source[i].append(999999)
                else:
                    source[i].append(int(random.random() * 20))
        self.write_source(source)

    def write_source(self, source):
        file_name = '../source/generated-' + str(self.size) + '.little'
        f = open(file_name, 'w')
        for row in source:
            line = ' '.join([str(i) for i in row]) + '\n'
            f.write(line)
        f.close()


g = Generator(100)
g.generate()