##
## SecurePass CLI tools utilities
##
## This code is released under GPLv2
##
## (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
##          GARL Sagl (www.garl.ch)
##

import logging
import ConfigParser
import os
import sys


def loadConfig():
    """loadConfig returns cassandra servers"""

    conffiles = ['/etc/securepass.conf',
                 '/usr/local/etc/securepass.conf',
                 os.getcwd() + '/securepass.conf']
    #conffiles.append(os.path.join(os.path.expanduser("~"), ".securepass"))

    ## Virtual Environment handling
    # VIRTUAL_ENV is not reliable, switching to sys.real_prefix
    if hasattr(sys, 'real_prefix'):
        conffiles.append(sys.prefix + "/securepass.conf")
        conffiles.append(sys.prefix + "/etc/securepass.conf")

    conf_found = 0

    ## Get Config File
    for conf in conffiles:
        if not os.path.isfile(conf):
            logging.debug("Unable to open config file %s!" % conf)
        else:
            logging.debug("Config file found at %s!" % conf)
            conf_found = 1

    if conf_found == 0:
        logging.error("Unable to find configuration files")
        sys.exit(1)

    config = ConfigParser.ConfigParser()
    config.read(conffiles)

    ## Default config
    myconfig = {}
    myconfig['endpoint'] = "https://beta.secure-pass.net/"

    try:
        ## Get required configuration
        myconfig['app_id'] = config.get("default", "app_id")
        myconfig['app_secret'] = config.get("default", "app_secret")

    except:
        logging.debug("Unable to load config file")
        return {}

    ## Get endpoint, if specified
    try:
        myconfig['endpoint'] = config.get("default", "endpoint")
    except:
        pass

    # Get realm, if specified
    try:
        myconfig['realm'] = config.get("nss", "realm")
    except:
        pass

    # SSH behaviour
    try:
        myconfig['root'] = config.get("ssh", "root")
        myconfig['strip_windows_domain'] = config.get("ssh", "strip_windows_domain")
    except:
        pass


    # Return array with config
    return myconfig