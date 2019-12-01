from urllib.request import urlopen
from os import *
from subprocess import check_output
from platform import system as sysos, architecture
from wget import download
from Defs.Languages import *
import os
import ctypes

RED, GREEN, DEFAULT = '\033[91m', '\033[32m', '\033[0m'

installGetText()
languageSelector()
try:
    urlopen('https://8.8.8.8', timeout=10)
    print(GREEN+'[connection:alive]'+DEFAULT)
except:
    print(RED+'[connection:dead]'+DEFAULT)
    exit(0)
def cres(): #check resources
    if not path.isfile('Server/ngrok'):
        download('https://bin.equinox.io/c/4VmDzA7iaHb/'+('ngrok-stable-linux-arm.zip'if'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname','-a')))else'ngrok-stable-{0}-{1}.zip'.format(sysos().lower(),'amd64'if architecture()[0]=='64bit'else'386')))
        system('unzip ngrok*.zip;mv ngrok Server/ngrok;rm -Rf ngrok*.zip;clear')
    if system('lt > /dev/null')!=256:system('apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel')
    if not path.isfile('WebPages/'):system('tar xf WebPages.tar.xz; rm WebPages.tar.xz')
def checkPermissions():
        if sysos()=='Linux' and os.getuid():raise PermissionError("{0}[run as {1}superuser{0}]".format(RED, GREEN)) 
        elif sysos()=='Darwin' and os.getuid():raise PermissionError("{0}[run as {1}superuser{0}]".format(RED, GREEN))
