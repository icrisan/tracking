import logging

LOG_FILENAME = 'logs/app.log'

logging.basicConfig(filename=LOG_FILENAME,
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
