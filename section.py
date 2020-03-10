class Section:

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def len(self):
        return abs(self.x2 - self.x1)
