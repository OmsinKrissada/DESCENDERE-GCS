import coloredlogs
import logging

logger = logging.getLogger()
coloredlogs.install(level='DEBUG', logger=logger,
                    fmt='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%m-%d-%Y %H:%M:%S')


if __name__ == '__main__':
    logger.error('This is an ERROR message')
    logger.warning('This is a WARNING message')
    logger.info('This is an INFO message')
    logger.debug('This is a DEBUG message')
