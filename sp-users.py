#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Users list
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##


import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""List users in SecurePass

%prog [options]""")


parser.add_option('-d', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-D', '--details',
                  action='store_true', dest="detail_flag",
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

## List all users
if opts.detail_flag:
    print "%-30s %-30s" % ("User ID", "Name and Surname")
    print "=========================================================================="

try:
    for user in sp_handler.user_list(realm=opts.realm):
        if opts.detail_flag:
            user_detail = sp_handler.user_info(realm=opts.realm, user=user)
            print "%-30s %s %s" % (user, user_detail['name'], user_detail['surname'])
        else:
            print user


except Exception as e:
    print e






