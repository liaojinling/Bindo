#-*- coding:utf-8 -*-
import logging


class Logger():

    def __init__(self,logname,loglevel=logging.DEBUG):
        self.logger=logging.getLogger()
        self.logger.setLevel(loglevel)
        hfile=logging.FileHandler(logname)
        hfile.setLevel(loglevel)

        hterm=logging.StreamHandler()
        hterm.setLevel(loglevel)

        formattr=logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d  - %(message)s')

        hfile.setFormatter(formattr)
        hterm.setFormatter(formattr)

        self.logger.addHandler(hfile)
        self.logger.addHandler(hterm)

    def getlog(self):
        return self.logger

if __name__ == '__main__':
        logger = Logger().getlog()
        logger.info('info')
        logger.warn('warn')
        logging.error('this is an error.')