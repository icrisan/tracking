import logging

LOG_FILENAME = 'utils/app.log'

logging.basicConfig(filename=LOG_FILENAME,
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
