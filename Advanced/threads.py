
def worker(delay):
    sleep(delay)
    #print threading.currentThread().name

def main():
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=worker, name='t'+str(i), args=(random(),))
        t.start()
        threads.append(t)

    t = threading.Thread(target=worker, name='waitinglong', args=(5, ))
    t.start()
    threads.insert(0, t)

    for t in threads:
        print "joining with {}".format(t.getName())
        t.join()

    print "main thread ends"

if __name__ == '__main__':
    main()



def get_checksum(queue, string_content):
    #print string_content
    value = hashlib.md5(string_content).hexdigest()
    queue.put({string_content: value})

def main():
    qu = Queue()
    checksums = []

    for line in open('/etc/resolv.conf'):
        t = threading.Thread(target=get_checksum, args=(qu, line))
        t.start()

    while qu.qsize():
        response = qu.get()
        checksums.append(response)


    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    for result in checksums:
        for key in result:
            print key.rstrip()
            print result.get(key)
            print

if __name__ == '__main__':
    main()


def worker(delay):
    sleep(delay)
    #print threading.currentThread().name

def main():
    for i in range(1, 6):
        t = threading.Thread(target=worker, name='t'+str(i), args=(random(),))
        t.start()

    t = threading.Thread(target=worker, name='waitinglong', args=(5, ))
    t.start()


    for t in threading.enumerate():
        if t is not threading.currentThread():
            print "joining with {}".format(t.getName())
            t.join()

    print "main thread ends"

if __name__ == '__main__':
    main()

