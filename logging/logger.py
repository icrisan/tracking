import logging

filename = '../api_reports/app.log'

logging.basicConfig(filename=filename,
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
