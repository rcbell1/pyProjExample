import logging

import logger_mylib


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(name)s: %(asctime)s | %(levelname)s"
        "| %(filename)s:%(lineno)s | %(process)d] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )

    logging.debug("A debug message")
    logging.info("An info message")
    logging.warning("A warning message")
    logging.error("An error message")
    logging.critical("A critical message")

    logger_mylib.do_something()


if __name__ == "__main__":
    main()
