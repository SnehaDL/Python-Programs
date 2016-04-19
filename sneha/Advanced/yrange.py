__author__ = 'sneha'

class yrangeiterator(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

class yrange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return yrangeiterator(self.n)

if __name__ == '__main__':
    for i in yrange(5):
        print i