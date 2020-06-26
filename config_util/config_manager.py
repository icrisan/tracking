import os
from configparser import ConfigParser
from pathlib import Path

from utils.logger_util import *

logger = logging.getLogger(__name__)
config = ConfigParser()


def get_project_root() -> Path:
    """Returns project root folder."""
    return os.path.abspath(os.curdir)


# def read_config_file(section):
#     try:
#         config_file = os.path.join(get_project_root(), "config.ini")
#         config.read(config_file)
#         if config.has_section(section):
#             result = dict(config.items(section))
#             return result
# 
#     except:
#         logger.info("Config file not found")
# 
#         logger.info(config_file)
# 
#     config.read(config_file)
# 
# 
# def parse_config_file(section,option):
#     dictionary = read_config_file(section)
# 
#     options = config.options(section)
# 
#     for option in options:
#         try:
#             dictionary[option] = config.get(section, option)
#             if dictionary[option] == -1:
#                 logger.debug("skip: %s" % option)
#         except:
#             logger.debug("exception on %s!" % option)
#             dictionary[option] = None
# 
#     return dictionary


def get_config_section(section):
    """Returns all properties of a section as a dict or None if section does not exist."""
    config_file = get_project_root()+"/config.ini"

    logger.info("Config file location: %s" % config_file)
    file_exists = os.path.isfile(config_file)
    logger.debug("Config file exists: %s" % file_exists)
    config = ConfigParser()
    if file_exists:
        try:
            config.read(config_file)
            if config.has_section(section):
                result = dict(config.items(section))
                return result

        except EOFError:
            logger.warning("Config file error.")
        return None
    logger.warning("Config file not found.")
    return None


def get_config_property(section, prop):
    """Returns the config property for a specific section."""
    logger.debug("Extracting {} for section {}".format(prop, section))
    section_dict = get_config_section(section)
    if section_dict is not None:
        try:
            return section_dict[prop]
        except KeyError:
            logger.warning(
                "Property '{}' not found in section {}".format(prop, section)
            )
            return None
