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

DEFAULT_CONF_FILENAME = "securepass.conf"


def _path_to_conffile(*path):
    return os.path.join(*(path + (DEFAULT_CONF_FILENAME,)))


def _list_conffiles_locations():
    prefix = sys.prefix
    venv_prefix = None
    if hasattr(sys, 'real_prefix'):
        prefix = sys.real_prefix
        venv_prefix = sys.prefix

    conffiles = [
        _path_to_conffile(prefix, "etc"),
        _path_to_conffile(prefix, "usr", "local", "etc"),
        _path_to_conffile(os.getcwd()),
    ]
    if venv_prefix is not None:
        conffiles.extend([
            _path_to_conffile(venv_prefix),
            _path_to_conffile(venv_prefix, "etc"),
        ])

    return conffiles


def loadConfig():
    """loadConfig returns cassandra servers"""

    conffiles = _list_conffiles_locations()

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

    ## GEt optional info
    try:
        myconfig['endpoint'] = config.get("default", "endpoint")
        return myconfig

    except:
        return myconfig
