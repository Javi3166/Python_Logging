import logging
from ast import Index
from cgitb import handler
from inspect import trace

# import Helper

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')

print("\nUsing a logging.conf file can offload the configuration of the loggers to another file so there won't"
      " be a need to hard code it into the main code.")
import logging.config

# .dictConfig accomplishes the same thing but requires a different syntax
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message.')

print("\nIt is possible to traceback to where the error occurred using exc_info.")
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

print("\nIf it is unknown what kind of error could occur, there is a way to find out.")
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())

print("\nA rotating file handler can be used to keep track of the most recent loggers in the "
      "case of a very large project.")
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Roll over after 2 KB and keep backing up logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

#for _ in range(10000):
#    logger.info("Hello world!")

print("\nIt is also possible to used a timed rotating file handler.")
from logging.handlers import TimedRotatingFileHandler
import time

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=2, backupCount=3)
logger.addHandler(handler)

for _ in range(5):
    logger.info('Hellow world!')
    time.sleep(5)