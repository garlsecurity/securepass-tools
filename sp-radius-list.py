#!/usr/bin/python
##
## SecurePass CLI tools utilities
## Radius list
##
## (c) 2014 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##


import utils
import securepass
import logging
from optparse import OptionParser


parser = OptionParser(usage="""List RADIUS devices in SecurePass

%prog [options]""")


parser.add_option('-D', '--debug',
                  action='store_true', dest="debug_flag",
	              help="Enable debug output",)

parser.add_option('-d', '--details',
                  action='store_true', dest="detail_flag",
	              help="Enable debug output",)

parser.add_option('-r', '--realm',
                  action='store', dest="realm",
                  default=None,
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


## List all apps
if opts.detail_flag:
    print "%-45s %-30s" % ("RADIUS", "FQDN")
    print "============================================================================="

try:
    for radius in sp_handler.radius_list(realm=opts.realm):
        if opts.detail_flag:
            radius_detail = sp_handler.radius_info(radius=radius)
            print "%-45s %-30s" % (radius, radius_detail['name'])
        else:
            print radius


except Exception as e:
    print e







