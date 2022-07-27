class Somar:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def somar(self):
        return self.x + self.y


if __name__ == '__main__':
    n1 = Somar(1, 2)
    print(n1.somar())

