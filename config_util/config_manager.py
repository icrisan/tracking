from configparser import ConfigParser
from utils.logger_util import *

logger = logging.getLogger(__name__)
config = ConfigParser()


def read_config_file():
    config_file = 'config.ini'
    config.read(config_file)

    return config.sections()


def parse_config_file(section):
    dictionary = {}

    options = config.options(section)

    for option in options:
        try:
            dictionary[option] = config.get(section, option)
            if dictionary[option] == -1:
                logger.debug("skip: %s" % option)
        except:
            logger.debug("exception on %s!" % option)
            dictionary[option] = None

    return dictionary
