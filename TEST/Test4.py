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
        num = '1'
        num1 ='2'
        if num == num1:
            return True
        else:
            return False
    # role = test1(self=None)
    result = test1(self=None)
    @unittest.skipIf(result,u'True不执行')
    def test2(self):
        print('11111')
    @unittest.skipUnless(result,u'False执行')
    def test3(self):
        print('2222')



if __name__=="__main__":
    unittest.main()

