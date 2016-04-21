

def grep_me(pattern, filename, count):
    with open(filename) as fp:
        i = 0
        while True:
            line = fp.readline()
            if not line:
                raise StopIteration()

            if re.search(pattern, line, re.I):
                temp = yield line

                while i < count:
                    line = fp.readline()
                    temp = yield line
                    if temp:
                        count = temp
                    i += 1
                else:
                    i = 0

if __name__ == '__main__':
    g = grep_me('^root', '/etc/passwd', 3)
    for line in g:
        print line,
        g.send(5)



