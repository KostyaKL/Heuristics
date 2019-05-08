from Main import lecture2 as l2


class Heuristics:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def euclidean(self):
        return l2.exercise9("euclidean", self.coordinate1, self.coordinate2)

    def manhattan(self):
        return l2.exercise9("manhattan", self.coordinate1, self.coordinate2)

    def chebyshev(self, dx, dy):
        return max(dx, dy)
