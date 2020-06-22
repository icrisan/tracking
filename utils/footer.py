
import logging
import os


logger = logging.getLogger(__name__)


class ReportFooter:

    def __init__(self, app, total_tests_run, passed_tests, failed_tests, skipped_tests, errors, total_time, failures):
        self.platform = "mac"
        self.app = app
        self.total_tests_run = total_tests_run
        self.failed_tests = failed_tests
        self.passed_tests = passed_tests
        self.skipped_tests = skipped_tests
        self.error_tests = errors
        self.total_duration = total_time
        self.failures = failures

    def print_report_footer(self):
        """Print report footer in a nice format."""
        total = self.passed_tests + self.failed_tests + self.skipped_tests + self.error_tests
        header = '\n' + 'Test Report'.center(os.get_terminal_size().columns, '-') + '\n'
        separator = '\n' + ''.center(os.get_terminal_size().columns, '-') + '\n'
        failure_str = ''

        if len(self.failures) > 0:
            failure_str = '\n\nThe following tests did not pass:\n'
            for failed_tests in self.failures:
                failure_str += os.path.basename(failed_tests) + '\n'
                failure_str += '\n'

        test_results_str = 'Passed: %s, Failed: %s, Skipped: %s, Errors %s  -- Total: %s' \
                           % (self.passed_tests, self.failed_tests, self.skipped_tests, self.error_tests, total)
        total_time_str = 'Total time: %s second(s)' % self.total_duration

        test_results = (header +  '\n' + test_results_str + ' ' *
                        (os.get_terminal_size().columns - (len(test_results_str) + len(total_time_str))) +
                        total_time_str + failure_str + separator)

        print(test_results)
        return test_results


def create_footer(app):
    """Generate report footer object.
    :param app: Target Application 
    :return: ReportFooter object
    """
    skipped = 0
    failed = 0
    passed = 0
    errors = 0
    total_duration = 0

    failed_tests = []

    for test in app.completed_tests:

        if test.outcome == 'FAILED':
            failed = failed + 1
            failed_tests.append(test.file_name)
        elif test.outcome == 'PASSED':
            passed = passed + 1
        elif test.outcome == 'SKIPPED':
            skipped = skipped + 1
        elif test.outcome == 'ERROR':
            failed_tests.append(test.file_name)
            errors = errors + 1

        total_duration = total_duration + test.test_duration

    total_tests = passed + skipped + failed + errors
    return ReportFooter(app, total_tests, passed, failed, skipped, errors, total_duration, failed_tests)


def _get_additional_info(values):

    additional_info = ''
    if values:
        for key in values:
            additional_info += ', ' + key + ': ' + values[key]
    return additional_info