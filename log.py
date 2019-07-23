import coloredlogs
import logging
LOGGER_NAME = 'root'
logger = logging.getLogger(LOGGER_NAME)
coloredlogs.install(level='DEBUG', logger=logger)
