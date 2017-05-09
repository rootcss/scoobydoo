from lib import Job
from util import log

def set_logging():
    if 'LOG_FILE' not in locals() and 'LOG_FILE' not in globals():
        log_file = 'scoobydoo.log'
    else:
        log_file = LOG_FILE
    logger = log.setup_custom_logger('ROOT', log_file=log_file)
    logger.debug('Logger initiated..')

set_logging()