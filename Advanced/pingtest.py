

class PingTest(object):
    def __init__(self):
        self.ping_result = {}

    def do_ping(self, hostname):
        try:
            print "pinging .. {}".format(hostname)
            result = ping.do_one(hostname, 2, 2)
            if result:
                self.ping_result[hostname] = result
            else:
                self.ping_result[hostname] = 'down'
        except:
            self.ping_result[hostname] = 'down'

def main():
    p = PingTest()
    for hostname in input(files=['hostname']):
        p.do_ping(hostname.rstrip())

    for hostname in p.ping_result:
        print "{} : {}".format(hostname, p.ping_result.get(hostname))

if __name__ == '__main__':
    main()




class PingTest(object):
    def __init__(self):
        self.ping_result = {}

    def do_ping(self, hostname):
        try:
            print "pinging .. {}".format(hostname)
            result = ping.do_one(hostname, 2, 2)
            if result:
                self.ping_result[hostname] = result
            else:
                self.ping_result[hostname] = 'down'
        except:
            self.ping_result[hostname] = 'down'

@timeit
def main():
    p = PingTest()
    for hostname in input(files=['hostname']):
        t = threading.Thread(target=p.do_ping, args=(hostname.rstrip(), ))
        t.start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    for hostname in p.ping_result:
        print "{} : {}".format(hostname, p.ping_result.get(hostname))

if __name__ == '__main__':
    main()







