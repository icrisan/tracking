import pytest
from scripts.plugin import Plugin

from utils.logger_util import *
logger = logging.getLogger(__name__)


def main():
    my_plugin = Plugin()
    pytest.main(get_pytest_args(), plugins=[my_plugin])
    logger.info('Starting main project!!!!')

def get_pytest_args():
    pytest_args = ['-vs', './tests']

    return pytest_args
