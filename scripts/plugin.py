import shutil
import time

import pytest

from reports.email_report import EmailReport
from utils import args
from utils.args import results
from utils.footer import create_footer
from utils.logger_util import *
from utils.test_result import test_result_list

logger = logging.getLogger(__name__)


class Plugin:

    completed_tests = []
    values = {}
    passed = []
    failed = []

    def __init__(self):
        logger.info("Initialize Pytest Plugin")

    def pytest_sessionstart(self, session):
        """Called after the 'Session' object has been created and before performing test collection.
        :param _pytest.main.Session session: the pytest session object.
        """
        self.start_time = time.time()
        logger.info(
            "\n"
            + "Test session {} started".format(session.name).center(
                shutil.get_terminal_size().columns, "-"
            )
        )

    def pytest_sessionfinish(self, session):
        """ called after whole test run finished, right before returning the exit status to the system.
        :param _pytest.main.Session session: the pytest session object.
        :param int exitstatus: the status which pytest will return to the system.
        """
        self.end_time = time.time()

        footer = create_footer(self)
        footer.print_report_footer()

        if results.email is not None:
            logger.info("Sending email report")
            # try:
            #     EmailReport("asdasda")
            # except SyntaxError:
            #     logger.error(
            #         "Problem with email report - check config file for correct values."
            #     )
        


    def pytest_runtest_setup(self, item):
        pass

    def pytest_runtest_teardown(self, item):
        pass

    def pytest_runtestloop(self, session):
        pass

    def pytest_runtest_logstart(self, nodeid, location):
        pass

    def pytest_runtest_call(self, item):

        pass

    def pytest_runtest_logfinish(self, nodeid, location):
        pass

    @pytest.fixture
    def option(self, pytestconfig):
        """
        fixture for ovewriting values in pytest.ini file
        :return: Option Object
        """

        new_value = {}

        class Options:
            @staticmethod
            def get(name):
                return new_value.get(name, pytestconfig.getini(name))

        return Options()

  

    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_makereport(self, item, call):

        """ return a :py:class:`_pytest.runner.TestReport` object
            for the given :py:class:`pytest.Item <_pytest.main.Item>` and
            :py:class:`_pytest.runner.CallInfo`.
            Stops at first non-None result
            """

        if call.when == "call" and call.excinfo is not None:

            if str(item.__dict__.get('fspath')) in str(call.excinfo):
                logger.debug('Test failed with assert')
                outcome = "FAILED"
            else:
                logger.debug('Test failed with error')
                outcome = "ERROR"

            assert_object = (item, outcome, call.excinfo)

            test_result = test_result_list(assert_object, call.start, call.stop)

            self.completed_tests.append(test_result)

        elif call.when == "call" and call.excinfo is None:
            outcome = 'PASSED'
            test_instance = (item, outcome, None)

            test_result = test_result_list(test_instance, call.start, call.stop)

            self.completed_tests.append(test_result)

        # elif call.when == "setup" and item._skipped_by_mark:
        #     outcome = 'SKIPPED'
        #     test_instance = (item, outcome, None)
        #
        #     test_result = test_result_list(test_instance, call.start, call.stop)
        #
        #     self.completed_tests.append(test_result)

    def add_test_result(self, test_result):
        if len(self.completed_tests) > 0:

            # If a result for this test already exists, and we have run it again:
            # 1. Keep track of the test and how many times it was rerun.
            # 2. Remove the previous result.
            # 3. Add the new result.

            prev_test_path = str(self.completed_tests[-1].file_name)
            test_path_1 = str(test_result.file_name)
            test_path_2 = str(test_result.node_name)

            if prev_test_path != "None":
                if prev_test_path == test_path_1 or prev_test_path == test_path_2:
                    if self.rerun_tests.get(prev_test_path) is not None:
                        self.rerun_tests[prev_test_path] += 1
                    else:
                        self.rerun_tests[prev_test_path] = 1

                    if test_result.outcome == "PASSED":
                        self.flaky_tests.append(
                            (prev_test_path, self.rerun_tests[prev_test_path])
                        )

                    logger.debug("Previous test: %s" % prev_test_path)
                    logger.debug("Current test file name: %s" % test_path_1)
                    logger.debug("Current test node name: %s" % test_path_2)
                    removed_test = self.completed_tests.pop()
                    logger.debug("\nRemoved test: %s" % removed_test.file_name)
        self.completed_tests.append(test_result)


def reason_for_failure(report):
    if report.outcome == "passed":
        return ""
    else:
        return report.longreprtext
