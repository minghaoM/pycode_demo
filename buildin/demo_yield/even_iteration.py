# -*- coding: utf-8 -*-


class EvenRange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return EvenIterator(self.n)


class EvenIterator(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 2
            return i
        else:
            raise StopIteration()


if __name__ == "__main__":
    print("even iteration demo")
    num = 11
    for i in EvenRange(11):
        print(i)
