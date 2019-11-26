import os
import sys
import logging
from logging import handlers
import datetime

logger = logging.getLogger('MesssageLog')
logger.setLevel(logging.DEBUG)
rf_handler = handlers.TimedRotatingFileHandler('test.log', when='midnight', interval=5, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s-%(thread)d - [%(filename)s] -%(levelname)s - %(message)s"))
logger.addHandler(rf_handler)

logger.debug("debug message") 
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
