from logging import DEBUG

print("\nIn order to begin logging, the logging module must be imported. There are 5 different log levels. Debug, Info, "
      "Warning, Error, and Critical. They're used to indicate the severity of the events.")

import logging

# The arguments to set the format can be found in the formal Python documentation.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

print("\nAmong the 5 levels, debug and info do not show up by default. This can be changed by setting the basic "
      "configuration which is usually done right after importing.")
'''
logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')
'''

print("\nIt's best practice to not use the root logger when setting logging in other modules.")
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('Hello from Helper module.')

print("\nCreating a logger will create a hierarchy of loggers that start at the root logger and will by default propagate"
      " their messages all the way to the base level. \nIt is possible to set it to False, but it must be set above the "
      "error messages in the code for it to take effect.")

print("\nHandler objects are responsible to dispatching the correct log message to the correct location when needed.")

# Creating handler objects
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Setting the level and format of the handlers
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning.')
logger.error('This is an error.')