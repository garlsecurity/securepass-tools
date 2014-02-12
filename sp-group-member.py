#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Test group membership
## Exits 0 if ok, 1 if not belongs
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##


import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""Test group membership for SecurePass

%prog [options] userid group""")


parser.add_option('-d', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-o', '--no-output',
                  action='store_true', dest="nooutput_flag",
	              help="Suppress output",)


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

## Check user exists
try:
    if args[0].strip() == "":
        print "Missing username. Try with --help"
        exit(1)
except IndexError:
    print "Missing username. Try with --help"
    exit(1)

## Check password exists
try:
    if args[1].strip() == "":
        print "Missing group. Try with --help"
        exit(1)
except IndexError:
    print "Missing group. Try with --help"
    exit(1)


## Test the actual authentication
try:
    if sp_handler.group_member(user=args[0], group=args[1]):
        if not opts.nooutput_flag:
            print "User %s belongs to group %s!" % (args[0], args[1])
        exit(0)
    else:
        if not opts.nooutput_flag:
            print "User %s not in group %s!" % (args[0], args[1])
        exit(1)

except Exception as e:
    if not opts.nooutput_flag:
        print e
    exit(1)