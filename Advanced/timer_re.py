## Timer
def timeit(func):
    def time_wrapper(*args, **kwargs):
        t1 = dt.now()
        result = func(*args)
        t2 = dt.now()
        print "{} : {} seconds".format(func.__name__, (t2-t1).total_seconds())
        return result
    return time_wrapper

@timeit
def power(n):
    if n < 1:
        return 1
    else:
        sleep(random()*2)
        return n * power(n-1)

print power(3)

## Patterns


import re
def rev_file(filename):
    return (l[::-1] for l in open(filename) if len(l))


def grep_me(pattern, filename):
    return (l for l in open(filename) if re.search(pattern, l, re.I))

print grep_me('root', '/etc/passwd')

for line in rev_file('/etc/resolv.conf'):
    print line,


