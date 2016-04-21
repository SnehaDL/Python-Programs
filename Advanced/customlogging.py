
import logging

log1 = logging.getLogger()
log1.setLevel(logging.ERROR)

log2 = logging.getLogger('WarnLogger')
log2.setLevel(logging.WARN)

fh = logging.FileHandler('messages.log')
sh = logging.StreamHandler()

message = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(message)

sh.setFormatter(formatter)
fh.setFormatter(formatter)

log1.addHandler(sh)
log2.addHandler(sh)
log2.addHandler(fh)

log1.warn('a warning message')
log1.error('an error message')
log1.critical('critical error')
log2.warn('a warning message')
log2.error('an error message')
log2.critical('critical error')


log_file_name = "messages.log"

log1 = logging.getLogger('Rotating Logger')
rfh = RotatingFileHandler(filename=log_file_name, backupCount=5, maxBytes=32)
log1.addHandler(rfh)

log1.setLevel(logging.DEBUG)

for i in range(1, 15):
    log1.debug("{} : {}".format(i, i))

from glob import glob

for lf in glob(log_file_name+"*"):
    print lf

