import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e','--email', action='store_true',
                    help= 'Email Report'

                   )
results = parser.parse_args()
