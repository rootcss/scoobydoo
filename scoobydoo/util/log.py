import logging
from logging import handlers
import sys

def setup_custom_logger(name, log_file='scoobydoo.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    logger.addHandler(ch)

    fh = handlers.RotatingFileHandler(log_file, maxBytes=(1048576 * 5), backupCount=7)
    fh.setFormatter(format)
    logger.addHandler(fh)

    return logger