import cPickle
from propobject import Property
from cPickle import dump

l = [2,1,4,6, 'pypi']
cPickle.dump(l, open('listdata.dat', 'w'))

content = cPickle.load(open('prop.dat'))
content['release'] = 'spherical cow'

for item in content:
    print "[{}] -> {}".format(item, content[item])

def main():
    p1 = Property()
    p1['hostname'] =  'ws1'
    p1['domain'] = 'amadeus.in'
    p1['ipaddr'] = '17.1.1.132'
    p1['platform'] = 'linux2'

    dump(p1, open('prop.dat', 'w'))

    for item in p1:
        print "[{}] -> {}".format(item, p1[item])


if __name__ == '__main__':
    main()