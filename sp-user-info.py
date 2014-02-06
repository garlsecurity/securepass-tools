#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Detail of a user
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##


import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""Get user details in SecurePass

%prog [options] userid""")


parser.add_option('-d', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

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
        print "Missing username. Try with --help"
        exit(1)
except IndexError:
    print "Missing username. Try with --help"
    exit(1)


## Display info
try:
    myuser = sp_handler.user_info(user=args[0], realm=opts.realm)

    print "User details for %s" % args[0]
    print "================================================\n"
    print "Name.........: %s" % myuser['name']
    print "Surname......: %s" % myuser['surname']
    print "E-mail.......: %s" % myuser['email']
    print "Mobile nr....: %s" % myuser['mobile']
    print "National ID..: %s" % myuser['nin']
    print "RFID tag.....: %s" % myuser['rfid']
    print "Token type...: %s" % myuser['token']

    print "PIN status...:",

    if myuser['pin']:
        print "Enabled"
    else:
        print "Disabled"


except Exception as e:
    print e
