import argparse
from utils.logger_util import *

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser()

parser.add_argument(
    "-e", "--email", help="Submit email report", action="store_true"
)

results = parser.parse_args()
