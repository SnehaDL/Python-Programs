


class CustomFile(file):
    def __rshift__(self, other):
        self.seek(0, 0)
        content = self.readlines()[-other:]
        return ''.join(content)

    __rrshift__ = __rshift__

    def __lshift__(self, other):
        self.seek(0, 0)
        content = self.readlines()[:other]
        return ''.join(content)

with CustomFile('/etc/passwd') as fp:
    print fp << 2
    print
    print fp >> 2
    print
    print 2 >> fp


def getfiles(*filenames):
    return (open(filename) for filename in filenames)

def readlines(fds):
    for fd in fds:
        for line in fd:
            if 30 <= len(line) <= 60:
                yield "{}: {}".format(fd.name, line)


for ln in readlines(getfiles('/etc/passwd', '/etc/group')):
    print ln

def demo():
    while True:
        value = yield "string content in python"
        print value
g = demo()
content = g.next()
print content
g.send(content.upper())


