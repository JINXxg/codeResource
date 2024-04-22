#logging
import logging
import time
from logging.handlers import TimedRotatingFileHandler
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler=TimedRotatingFileHandler('time_rhan.log',when='s',interval=5,backupCount=5)
logger.addHandler(handler)

for _ in range(100):
    logger.info('hello fucker')
    time.sleep(5)


''' if you don't know what's excep is use traceback.format_exc()
import logging
import traceback

try:
    b=[4,5,6]
    val2=b[4]
except :
    logging.error('this is error %s',traceback.format_exc())
try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:
    logging.error(e,exc_info=True)
'''

#the ideal like logger is the factory and handler is the staff to deal with different problem(the level, format and so on)
'''with config file more easy
import logging.config
logging.config.fileconfig()
logger=logging.getLogger(__name__)

stram_h=logging.StreamHandler()
file_h=logging.FileHandler('file.log')

#set the handle level
stram_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#set the loggin formater
formater=logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stram_h.setFormatter(formater)
file_h.setFormatter(formater)

#add
logger.addHandler(stram_h)
logger.addHandler(file_h)

logger.warning("you fucker warning")
logger.error('you fucker error')
'''


'''


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%m/%d/%Y %H/%M/%S')#the function basic the paramite you pass
import helper



logging.debug("this is debug")
logging.info("this is infor")
logging.warning("this is warnning")
logging.error("this is error")
logging.critical("this is critical")
'''