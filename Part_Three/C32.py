class C32:

    def __init__(self):
        self.state = 'A'

    def send(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'B'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise RuntimeError

    def cull(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'G'
            return 7
        elif self.state == 'H':
            self.state = 'A'
            return 11
        else:
            raise RuntimeError

    def carve(self):
        if self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'B':
            self.state = 'F'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise RuntimeError
