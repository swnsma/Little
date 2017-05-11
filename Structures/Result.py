class Result:
    def __init__(self, path, rate):
        self.path = path
        self.rate = rate

    def get_path_string(self):
        from_p = 0
        to_p = self.path[0]
        res = '(' + str(from_p + 1) + '; ' + str(to_p + 1) + ') '
        from_p = to_p
        while from_p != 0:
            to_p = self.path[from_p]
            res += '(' + str(from_p + 1) + '; ' + str(to_p + 1) + ') '
            from_p = to_p

        return res
