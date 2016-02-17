
# -*- coding: utf-8 -*-

import os
import logging
import logging.handlers
# import config file
from config import LOG_FILE_DIRECTORY
from config import LOG_LEVEL


def create_logger(name):

    logger = logging.getLogger(name)
    logger.level = LOG_LEVEL
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..',
                           LOG_FILE_DIRECTORY)
    log_file = "%s/%s.log" % (log_dir, name)
    os.system("sudo touch %s" % log_file)
    os.system("sudo chmod 777 %s" % log_file)
    timed_handler = logging.handlers.TimedRotatingFileHandler(log_file,
                                                              when='midnight',
                                                              backupCount=5)
    formatter = logging.Formatter('%(asctime)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    timed_handler.setFormatter(formatter)
    logger.addHandler(timed_handler)
    logger.propagate = False
    logger.has_handlers = True

    return logger
