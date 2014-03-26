#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Add a RADIUS device
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##

import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""Add a RADIUS in SecurePass

%prog [options] RADIUS_IP_ADDRESS""")


parser.add_option('-D', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-f', '--fqdn',
                  default=None,
                  action='store', dest="fqdn",
	              help="FQDN/Name",)

parser.add_option('-s', '--secret',
                  default=None,
                  action='store', dest="secret",
	              help="Shared Secret",)

parser.add_option('-g', '--group',
                  default=None,
                  action='store', dest="group",
	              help="Group name (restriction)",)

parser.add_option('-R', '--rfid',
                  action='store_true', dest="rfid",
                  default=False,
	              help="Enable RFID tag as username",)

parser.add_option('-r', '--realm',
                  action='store', dest="realm",
	              help="Set alternate realm",)


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
        print "Missing RADIUS ip address. Try with --help"
        exit(1)
except IndexError:
    print "Missing RADIUS ip address. Try with --help"
    exit(1)



## Add the user
logging.debug("Adding RADIUS %s" % args[0])

try:

    result = sp_handler.radius_add(radius=args[0],
                                  name=opts.fqdn,
                                  secret=opts.secret,
                                  rfid=opts.rfid,
                                  group=opts.group,
                                  realm=opts.realm)


except Exception as e:
    print e
