from django.test import TestCase

# Create your tests here.
import log_
import logging
class TestLogger(TeskCase):
    def testLog(self):
        self.assertEqual('1','1')
        logging.info('测试 1=1 成功！')

