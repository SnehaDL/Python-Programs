

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")

def worker(lock):
    logging.debug('waiting for the lock')
    with lock:
        logging.debug('acquired the lock')
        sleep(random())
        print "at critical section : {}".format(threading.currentThread().name)
        logging.debug('released the lock')


def main():
    #lock = threading.Lock()
    lock = threading.Semaphore(1)

    for i in range(1, 6):
        t = threading.Thread(target=worker, name='t'+str(i), args=(lock,))
        t.start()

    t = threading.Thread(target=worker, name='waitinglong', args=(lock,))
    t.start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    print "main thread ends"

if __name__ == '__main__':
    main()

##semaphore



logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s : %(message)s")

class ActivePool(object):
    def __init__(self, lock):
        self.lock = lock
        self.pool = []

    def make_active(self, thread_name):
        with self.lock:
            logging.debug("joining the pool: {}".format(self.pool))
            self.pool.append(thread_name)
            logging.debug('pool: {}'.format(self.pool))

    def make_inactive(self, thread_name):
        with self.lock:
            self.pool.remove(thread_name)
            logging.debug('left the pool : {}'.format(self.pool))

def worker(s, pool):
    name = threading.currentThread().getName()
    logging.debug("waiting to the pool")

    with s:
        pool.make_active(name)
        sleep(1)
        pool.make_inactive(name)

def main():
    s = threading.Semaphore(3)
    lock = threading.Lock()
    pool = ActivePool(lock)

    for i in range(1, 7):
        t = threading.Thread(target=worker, args=(s, pool), name='t'+str(i))
        t.start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()


if __name__ == '__main__':
    main()

