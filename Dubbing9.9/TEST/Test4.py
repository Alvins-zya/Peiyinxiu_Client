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
import unittest
class test(unittest.TestCase):
    def test1(self):
        '''
        111111
        '''
        a = '哈哈哈'
        b = '哈哈哈'
        self.assertEqual(a,b,msg="文案错误")


if __name__=="__main__":
    unittest.main()