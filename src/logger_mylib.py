import logging


def do_something():
    # create logger, formatting inherited from the root logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 'application' code
    logger.debug("mylib debug message")
    logger.info("mylib info message")
    logger.warning("mylib warn message")
    logger.error("mylib error message")
    logger.critical("mylib critical message")
