class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        return super(B, self).__init__()