#coding = utf-8
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename='log.log',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info("T")
# logger.debug('DEBUG')
# logger.warning('warning')
# logger.info('Finish')
import time
import datetime
def test():
    time1 = datetime.datetime.now()
    time.sleep(5)
    time2 = datetime.datetime.now()
    time_result = time2 - time1
    print('实际播放时间：', time_result)
if __name__=='__main__':
    test()

