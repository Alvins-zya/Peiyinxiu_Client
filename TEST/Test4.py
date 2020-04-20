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
import os
import re
from Public.devices_list import get_conn_dev

class BaseOperate():
    def __init__(self):
        self.dev = get_conn_dev()

    def touch_X(self):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        out = os.popen("adb -s %s shell wm size" % (self.dev[0])).read()
        m = re.search(r'(\d+)x(\d+)', out)
        # y = ("{height}".format(height=m.group(2)))
        x = ("{width}".format(width=m.group(1)))
        print(x)
if __name__=='__main__':
    BaseOperate().touch_X()


