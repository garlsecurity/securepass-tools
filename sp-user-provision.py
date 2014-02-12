#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Provision a given user
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##


import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""Provision SecurePass user

%prog [options] userid""")


parser.add_option('-d', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-t', '--token',
                  action='store', dest="token",
                  type='choice',
                  choices=['iphone', 'android', 'blackberry', 'software',],
                  default='software',
	              help="Select token type (iphone, android, blackberry, software)",)


opts, args = parser.parse_args()

## Set debug
FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
if opts.debug_flag:
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
else:
    logging.basicConfig(format=FORMAT, level=logging.INFO)


## Load config
config =  utils.loadConfig()

## Config the handler
sp_handler = securepass.SecurePass(app_id=config['app_id'],
                                   app_secret=config['app_secret'],
                                   endpoint=config['endpoint'])

## Check
try:
    if args[0].strip() == "":
        print "Missing username. Try with --help"
        exit(1)
except IndexError:
    print "Missing username. Try with --help"
    exit(1)


## Send provisioning request
try:
    sp_handler.user_provision(user=args[0], swtoken=opts.token)

except Exception as e:
    print e