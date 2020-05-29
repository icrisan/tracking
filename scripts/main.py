import pytest
from scripts.plugin import Plugin


def main():
    my_plugin = Plugin()
    pytest.main(get_pytest_args(), plugins=[my_plugin])


def get_pytest_args():
    pytest_args = ['-vs', './tests']

    return pytest_args
