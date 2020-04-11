#coding = utf-8
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='log.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("T")
logger.debug('DEBUG')
logger.warning('warning')
logger.info('Finish')