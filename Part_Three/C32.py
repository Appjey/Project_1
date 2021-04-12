class C32:
    state = []

    def __init__(self):
        self.state = [None]

    def send(self):
        if self.state[-1] is None:
            self.state[-1] = 0
            return 0
        elif self.state[-1] == 2:
            self.state.append(2)
            return 2

    def cull(self):
        if self.state[-1] == 0:
            self.state.append(2)
            return 1

    def carve(self):
        if self.state[-1] is None:
            self.state[-1] = 0
            return 0
        elif self.state[-1] == 0:
            self.state.append(2)
            return 2