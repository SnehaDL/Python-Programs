
class Demo(object):

    def __call__(self, *args, **kwargs):
        ns = kwargs.get('ns')
        class_info = kwargs.get('class_info')
        if ns :
            print "current namespace : {}".format(__name__)
        elif class_info:
            print "class : {}".format(self.__class__.__name__)



    def __str__(self):
        return "<{} id={}>".format(self.__class__.__name__,
                                  id(self))

if __name__ == '__main__':
    d = Demo()
    d(class_info= True)  #objeact as callable
    #content = str(d)
    #print content


class Property(object):
    def __init__(self):
        self.container = {}

    def __getstate__(self):  #serialize
        return self.container

    def __setstate__(self, state):  #unserialuze
        self.container = state

    def __setitem__(self, key, value):
        self.container[key] = value

    def __getitem__(self, key):
        return self.container.get(key)

    def __iter__(self):
        return iter(self.container)


if __name__ == '__main__':
    p1 = Property()
    p1['hostname'] =  'ws1'
    p1['domain'] = 'amadeus.in'
    p1['ipaddr'] = '17.1.1.132'
    p1['platform'] = 'linux2'


    for item in p1:
        print "[{}] -> {}".format(item, p1[item])


class Window(object):
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return Window(self.size + other.size)

    def __mul__(self, other):
        try:
            if type(other) in [int, float, complex]:
                return Window(self.size * other)
            else:
                return Window(self.size * other.size)
        except Exception, e:
            print e

    __rmul__ = __mul__

    def __str__(self):
        return "{} size={}".format(self.__class__.__name__, self.size)


def main():
    w1 = Window(10)
    w2 = Window(11)
    w3 = w1 + w2
    print 'a' * w3

if __name__ == '__main__':
    main()