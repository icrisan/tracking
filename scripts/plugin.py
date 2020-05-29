
from utils.logger_util import *
logger = logging.getLogger(__name__)

class Plugin:

    def pytest_sessionstart(self, session=None):
        """Called after the 'Session' object has been created and before performing test collection.
        :param _pytest.main.Session session: the pytest session object.
        """
        logger.info('Session successfully started!')


    def pytest_sessionfinish(self, session=None):
        """Called after whole test run finished, right before returning the exit status to the system.
        :param _pytest.main.Session session: the pytest session object.
        :param int exitstatus: the status which pytest will return to the system.
        """
        logger.info('Session is successfully closed!')

    def pytest_runtest_makereport(self, item=None, call=None):
        """Return a :py:class:`_pytest.runner.TestReport` object
            for the given :py:class:`pytest.Item <_pytest.main.Item>` and
            :py:class:`_pytest.runner.CallInfo`.
            Stops at first non-None result
            """
        logger.info('Reporting is successfully performed!')
