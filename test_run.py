#-*- coding:utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
from Bindo.common.email_test import Email
from Bindo.common.report import Report
from Bindo.common.log import Logger
import unittest
import time,logging


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "./report/"+now+"result.html"
    logger = Logger('./log/logger_%s.log' % now,loglevel=logging.INFO)
    logging.info('**************测试开始************')
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title=u"this is Bindo test report",description=u'Bindo的测试报告')
    discover = unittest.defaultTestLoader.discover('./test_case',pattern='test_logincase.py')
    runner.run(discover)
    fp.close()
    file_path = Report('./report')
    logging.info('**************测试结束************')
    Email(filename,filename)