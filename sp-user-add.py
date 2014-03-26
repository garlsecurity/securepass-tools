#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Users add
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##

import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""Add user in SecurePass

%prog [options] userid""")


parser.add_option('-D', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-n', '--name',
                  default=None,
                  action='store', dest="name",
	              help="First name",)

parser.add_option('-s', '--surname',
                  default=None,
                  action='store', dest="surname",
	              help="Last name",)

parser.add_option('-e', '--email',
                  default=None,
                  action='store', dest="email",
	              help="E-mail address",)

parser.add_option('-m', '--mobile',
                  default=None,
                  action='store', dest="mobile",
	              help="Mobile number",)

parser.add_option('--nin',
                  default=None,
                  action='store', dest="nin",
	              help="National Identification Number (optional)",)

parser.add_option('--rfid',
                  default=None,
                  action='store', dest="rfid",
	              help="RFID tag (optional)",)

parser.add_option('--manager',
                  default=None,
                  action='store', dest="manager",
	              help="Manager user id (optional)",)


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

## Name
if opts.name is None:
    print "Missing name. Try with --help"
    exit(1)

if opts.surname is None:
    print "Missing surname. Try with --help"
    exit(1)

if opts.email is None:
    print "Missing e-mail address. Try with --help"
    exit(1)

if opts.mobile is None:
    print "Missing mobile number. Try with --help"
    exit(1)


## Add the user
logging.debug("Adding user %s" % args[0])

try:
    sp_handler.user_add(user=args[0],
                        name=opts.name,
                        surname=opts.surname,
                        email=opts.email,
                        mobile=opts.mobile,
                        nin=opts.nin,
                        rfid=opts.rfid,
                        manager=opts.manager)

except Exception as e:
    print e
