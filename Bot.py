##############################################################################################################################################



#################################################################################################################
import ch
import random
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
import re
import getWhois
import json
import time
import datetime
import os
import urllib
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
from time import localtime, strftime
from xml.etree import cElementTree as ET
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
from getWhois import whois
from socket import gethostname, gethostbyname
ip = gethostbyname(gethostname())

botname = 'Earshavina'  ##isi idnya
botpass = 'angganteng19' ##isi paswordnya

startTime = time.time()
lockdown = False
fapfap = True
activated = True
locked = True
game = True
bankstats = dict()
waktu0 = dict()
waktu1 = dict()
waktu2 = dict()
waktu3 = dict()
waktu4 = dict()
waktu5 = dict()
waktu10 = dict()
waktu11 = dict()
waktu12 = dict()
waktu13 = dict()
waktu14 = dict()##mine jack men##
lvlstats = dict()
lvlstats1 = dict()
timers = dict()
blackrooms = []
jack = False 

##nick names
def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user

#### Returns the number of seconds since the program started.
################################################################
def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    # do return startTime if you just want the process start time
    return time.time() - startTime

def reboot():
    output = ("rebooting server . . .")
    os.popen("sudo -S reboot")
    return output

#### SYSTEM UPTIME
def uptime():
 
     total_seconds = float(getUptime())
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
     return string;

## DEFINITIONS
dictionary = dict() 
f = open("definitions.txt", "r")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name = json.loads(line.strip())
      dictionary[word] = json.dumps([definition, name])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()
##nicks
nicks=dict()#empty list
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()
##Rooms
rooms = []
f = open("rooms.txt", "r") # read-only
for name in f.readlines():
  if len(name.strip())>0: rooms.append(name.strip())
f.close()
##RB
def rainbow(word):
    length = len(word)
    #set rgb values
    r = 255 #rgb value set to red by default
    g = 0
    b = 0
    sub = int(765/length)
    counter = 0
    string = ""
    for x in range(0, length):
        letter = word[counter]
        s = '<f x12%02X%02X%02X="arial">%s' % (r, g, b, letter)
        string = string+s
        counter+=1
        if (r == 255) and (g >= 0) and (b == 0): #if all red
            g = g+sub
            if g > 255: g = 255
        if (r > 0) and (g == 255) and (b == 0): #if some red and all green
            r = r-sub #reduce red to fade from yellow to green
            if r<0: r = 0 #if red gets lower than 0, set it back to 0
        if (r == 0) and (g == 255) and (b >= 0):
            b = b+sub
            if b>255:
                b = 255
                trans = True
        if (r == 0) and (g > 0) and (b == 255):
            g = g-sub
            if g<0: g = 0
        if (r >= 0) and (g == 0) and (b == 255):
            r = r+sub
            if r>255: r = 255
    return string
##owners
owners = []
try:
    file = open("owners.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            owners.append(name.strip())
    print("[INFO]Doushi loaded...")
    file.close()
except:
    print("[ERROR]no file named owners")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

###admin
admin = []
try:
    file = open("admin.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            admin.append(name.strip())	
    print("[INFO]Luzrov loaded...")
    file.close()
except:
    print("[ERROR]no file named admin")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##archknight
archknight = []
try:
    file = open("archknight.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archknight.append(name.strip())
    print("[INFO]Fethmus loaded...")
    file.close()
except:
    print("[ERROR]no file named archknight")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##archwizard
archwizard = []
try:
    file = open("archwizard.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archwizard.append(name.strip())
    print("[INFO]Yurlin loaded...")
    file.close()
except:
    print("[ERROR]no file named archwizard")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##player
player = []
try:
    file = open("player.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archwizard.append(name.strip())
    print("[INFO]player loaded...")
    file.close()
except:
    print("[ERROR]no file named player")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##whitelist
whitelist = []
try:
    file = open("whitelist.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            whitelist.append(name.strip())
    print("[INFO]whitelist loaded...")
    file.close()
except:
    print("[ERROR]no file named whitelist")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

#END#
##IP Whois
ip_whois = dict()
try:
  f = open("ip_whois.txt", "r")
  ip_whois = eval(f.read())
  f.close()
except:pass
unid_ver = dict()
try:
  f = open("unid_ver.txt", "r")
  ip_whois = eval(f.read())
  f.close()
except:pass
 
##SessionId Whois
sid_whois = dict()
try:
  f = open("sid_whois.txt", "r")
  sid_whois = eval(f.read())
  f.close()
except:pass

#IPloc try
userip = dict()
try:
  f = open("userip.txt", "r")
  userip = eval(f.read())
  f.close()
except:pass
 
## Stuff ##
## WHOIS
whois = dict()
try:
  f = open('whois.txt','r')
  whois = eval(f.read())
  f.close()
except:pass
unid_ver = dict()
try:
  f = open("unid_ver.txt", "r")
  whois = eval(f.read())
  f.close()
except:pass
##MONEY
bank=dict()
f = open("bank.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,coin,gold= json.loads(line.strip())
      bank[user] = json.dumps([coin,gold])
  except:
    print("[ERROR]Cant load MONEY: %s" % line)
f.close()


stats=dict()
f = open("stats.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,exp,up= json.loads(line.strip())
      stats[user] = json.dumps([lvl,exp,up])
  except:
    print("[ERROR]Cant load STATS: %s" % line)
f.close()

mcash=dict()
f = open("mcash.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,cash,cp = json.loads(line.strip())
      mcash[user] = json.dumps([cash,cp])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()
##rpgdef
rbank=dict()
f = open("rbank.txt", "r")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,cash,eris= json.loads(line.strip())
      rbank[user] = json.dumps([cash,eris])
  except:
    print("[ERROR]Cant load RPG Bank", True)
f.close()

rstats=dict()
f = open("rstats.txt", "r")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,level= json.loads(line.strip())
      rstats[user] = json.dumps([level])
  except:
    print("[ERROR]Cant load user RPG stats", True)
f.close()
##AFK List##
afks = []
f = open("afks.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: afks.append(name.strip())
f.close()
##Lockroom
locks = []
f = open("locks.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: locks.append(name.strip())
f.close()
#Similock
simlock = []
f = open("simlock.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: simlock.append(name.strip())
f.close()
#Dlist
dlist = []
f = open("dlist.txt", "r") # read-onlyimport
for name in f.readlines():
  if len(name.strip())>0: dlist.append(name.strip())
f.close()
#END#
#SN TRY
sn = dict()
try:
  f = open('note.txt','r')
  sn = eval(f.read())
  f.close()
except:pass

## Send Notes
sasaran = dict()
f = open ("notes.txt", "r") #read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()
# SN Notifs
notif = []
f = open("notif.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

blacklist = []
f = open("blacklist.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: blacklist.append(name.strip())
f.close()

def tube(args):
  """
  #In case you don't know how to use this function
  #type this in the python console:
  >>> tube("pokemon dash")
  #and this function would return this thing:
  {'title': 'TAS (DS) Pokémon Dash - Regular Grand Prix', 'descriptions': '1st round Grand Prix but few mistake a first time. Next Hard Grand Prix will know way and few change different Pokémon are more faster and same course Cup.', 'uploader': 'EddieERL', 'link': 'http://www.youtube.com/watch?v=QdvnBmBQiGQ', 'videoid': 'QdvnBmBQiGQ', 'viewcount': '2014-11-04T15:43:15.000Z'}
  """
  search = args.split()
  url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
  udict = url.read().decode('utf-8')
  data = json.loads(udict)
  rest = []
  for f in data["items"]:
    rest.append(f)
  
  d = random.choice(rest)
  link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
  videoid = d["id"]["videoId"]
  title = d["snippet"]["title"]
  uploader = d["snippet"]["channelTitle"]
  descript = d["snippet"]['description']
  count    = d["snippet"]["publishedAt"]
  return "Result: %s <br/><br/><br/><br/><br/><br/><br/><br/><font color='#ffcc00'><b>%s</b></font><br/><font color='#ff0000'><b>Uploader</b></font>:<b> %s</b><br/><font color='#ff0000'><b>Uploaded on</b></font>: %s<br/><font color='#ff0000'><b>Descriptions</b></font>:<i> %s ...</i><br/> " % (link, title, uploader, count, descript[:200])

def gs(args):
  args = args.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gs:').replace('https://','gs:')
  anjay = re.findall('<h3 class="r">(.*?)</h3>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('<a href="gs:(.*?)" onmousedown="(.*?)">(.*?)</a>', la)
  q = 1
  for link, fak, title in a:
      setter.append('<br/>[%s] %s : http://%s' % (q, title.capitalize(), link))
      q += 1
  return "<br/><br/>".join(setter[0:4])

def newCi():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://cinemaindo.com/#", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<div class="title"><a href="(.*?)"><h2>(.*?)</h2>',resp)
 a = list()
 q = 1
 for link, cls, title in wa:
     a.append("(<b>%s</b>). <b>%s</b>: %s" % (q, title, link))
     q += 1
 return "<br/>".join(a)

def getBGTime(x):
                    total_seconds = float(x - time.time())
                    MIN     = 60
                    HOUR    = MIN * 60
                    DAY     = HOUR * 24
                    YEAR    = DAY * 365.25
                    years   = int( total_seconds / YEAR )      
                    days    = int( (total_seconds % YEAR ) / DAY  )
                    hrs     = int( ( total_seconds % DAY ) / HOUR )
                    min = int( ( total_seconds  % HOUR ) / MIN )
                    secs = int( total_seconds % MIN )
                    string = ""
                    if years > 0: string += "<font color='#00ffff'>" + str(years) + "</font> " + (years == 1 and "year" or "years" ) + ", "
                    if len(string) > 0 or days > 0: string += "<font color='#00ffff'>" + str(days) + "</font> " + (days == 1 and "day" or "days" ) + ", "
                    if len(string) > 0 or hrs > 0: string += "<font color='#00ffff'>" + str(hrs) + "</font> " + (hrs == 1 and "hour" or "hours" ) + ", "
                    if len(string) > 0 or min > 0: string += "<font color='#00ffff'>" + str(min) + "</font> " + (min == 1 and "minute" or "minutes" ) + " and "
                    string += "<font color='#00ffff'>" +  str(secs) + "</font> " + (secs == 1 and "second" or "seconds" )
                    return string;
 
def getSTime(x):
                    total_seconds = float(time.time() - x)
                    MIN     = 60
                    HOUR    = MIN * 60
                    DAY     = HOUR * 24        
                    days    = int( total_seconds / DAY )
                    hrs     = int( ( total_seconds % DAY ) / HOUR )
                    min = int( ( total_seconds  % HOUR ) / MIN )
                    secs = int( total_seconds % MIN )
                    string = ""
                    if days > 0: string += "<font color='#00ffff'>" + str(days) + "</font> " + (days == 1 and "day" or "days" ) + ", "
                    if len(string) > 0 or hrs > 0: string += "<font color='#00ffff'>" + str(hrs) + "</font> " + (hrs == 1 and "hour" or "hours" ) + ", "
                    if len(string) > 0 or min > 0: string += "<font color='#00ffff'>" + str(min) + "</font> " + (min == 1 and "minute" or "minutes" ) + " and "
                    string += "<font color='#00ffff'>" +  str(secs) + "</font> " + (secs == 1 and "second" or "seconds", True)
                    return string;

def bgtime(x):
        try:
                x = user if len(x) == 0 else x
                html = urlreq.urlopen("http://st.chatango.com/profileimg/%s/%s/%s/mod1.xml" % (x.lower()[0], x.lower()[1], x.lower())).read().decode()
                inter = re.compile(r'<d>(.*?)</d>', re.IGNORECASE).search(html).group(1)
                if int(inter) < time.time():
                        lbgtime = getSTime(int(inter))
                        return "that users bg ran out %s ago" % lbgtime
                else: return "bgtime for <b>%s</b>: %s" % (x.lower(), getBGTime(int(inter)))
        except: return 'that user never had a background, or the data was deleted  '

 

def newPoi():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.co.uk/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<f x10ff3399='Arial Bold'><br/>" + "<br/>".join(newset[0:5])

def newPoi2():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.co.uk/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<f x10ff3399='Arial Bold'><br/>" + "<br/>".join(newset[5:10])

def serPoi(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.co.uk/?s="+""+"&post_type=anime".join(args.split()), headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<f x10ff3399='Arial'><br/>" + "<br/>".join(newset[0:5])

def serPoi2(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.co.uk/?s="+"&post_type=anime".join(args.split()), headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<f x10ff3399='Arial'><br/>" + "<br/>".join(newset[5:10])

def gis(cari):
  argss = cari
  args = argss.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1366&bih=623&q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gis:').replace('https://','gis:').replace('.jpg','.jpg:end').replace('.gif','.gif:end').replace('.png','.png:end')
  anjay = re.findall('<div class="rg_meta">(.*?)</div>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('"ou":"gis:(.*?):end","ow"', la)
  q = 1
  for result in a:
    if ".jpg" in result or ".gif" in result or ".png" in result:
     if "vignette" not in result and "mhcdn.net" not in result and "alicdn.com" not in result and "gambardanfoto.com" not in result and "squarespace.com" not in result and "polyvore.com" not in result and "wikia.nocookie" not in result and "blogspot.com" not in result and "wordpress.com" not in result and "minionnation.co.uk" not in result and "twimg.com" not in result and "ohmymag.com" not in result and "waterfrontcinema.co.uk" not in result and "funmobility.netdna-ssl.com" not in result and "images-amazon.com" not in result and "upload.wikimedia.org" not in result: 
      setter.append('<f x11CC33CC="0">[%s] http://%s' % (q, result))
      q += 1
  return "<f x1133FF33=\"0\"></f>Hasil untuk <f x11FFFF33=\"0\"></f>"+cari+" :<br/><br/>"+"<br/>".join(setter[0:3])

def saveRank():
    f = open("owners.txt","w")
    f.write("\n".join(owners))
    f.close()
    f = open("admin.txt","w")
    f.write("\n".join(admin))
    f.close()
    f = open("archknight.txt","w")
    f.write("\n".join(archknight))
    f.close()
    f = open("whitelist.txt","w")
    f.write("\n".join(whitelist))
    f.close()
    
def googleSearch(search):
  try:
    encoded = urllib.parse.quote(search)
    rawData = urllib.request.urlopen("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+encoded).read().decode("utf-8")
    jsonData = json.loads(rawData)
    searchResults = jsonData["responseData"]["results"]
    full = []
    val = 1
    for data in searchResults:
      if "youtube" in data["url"]:
        data["url"] = "http://www.youtube.com/watch?v="+data["url"][35:]
      full.append("<br/>"+"(<b>%s</b> %s -> %s" % (val, data["title"], data['url']))
      val = val + 1
    return '<br/>'.join(full).replace('https://','http://')
  except Exception as e:
    return str(e)

## Check Mods
cek_mods=dict()
# Playa
playa = []
f = open("playa.txt", "r") # read-only
for name in f.readlines():
  if len(name.strip())>0: playa.append(name.strip())
f.close()

inven = dict()
try:
 f = open('inven.txt','r')
 inven = eval(f.read())
 f.close()
except:print("Error")

##MONEY
bank=dict()
f = open("bank.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,coin,gold= json.loads(line.strip())
      bank[user] = json.dumps([coin,gold])
  except:
   print("[ERROR]Cant load MONEY: %s" % line)
f.close()
      


##Setting Pretty Colors

class TestBot(ch.RoomManager):
  
  def onInit(self):
    self.setNameColor("ff3399")
    self.setFontColor("660066")
    self.setFontFace("Arial")
    self.setFontSize(11)
    self.enableBg()
    self.enableRecording()
  ##Connecting Crap

  def onConnect(self, room):
    print("Connected")
  
  def onReconnect(self, room):
    print("Reconnected")
  
  def onDisconnect(self, room):
    print("Disconnected")

  #################################################################
  ### Get user access from the file, and retun lvl of access number
  #################################################################
  def getAccess(self, user):
    if user.name in owners: return 6 # Owners
    elif user.name in admin: return 5 # Admins
    elif user.name in archwizard:return 4 # Arch Wizard
    elif user.name in archknight: return 3 # Arch Knight
    elif user.name in player: return 2 # Player
    elif user.name in whitelist: return 1
    elif user.name in dlist: return 0
    else: return 0
   
##Ignore this, you dont need to worry about this
#Well, you can actually take a little time to look at it and learn something
  
  def onMessage(self, room, user, message):
   try:  
          if room.getLevel(self.user) > 0:
            user_ip.update({user.name:message.ip})
            f = open('userip.txt', "w")
            f.write(str(user_ip))
            f.close
            if user.name not in ip_whois:
              ip_var = message.ip
              ip_whois.update({user.name:[ip_var]})
            if user.name in ip_whois:
              ip_var = message.ip
              if ip_var in ip_whois[user.name]:
                pass
              else:
                ip_whois[user.name].append(ip_var)
            f = open('ip_whois.txt', "w")
            f.write(str(ip_whois))
            f.close
          if user:
              unid = str(message.unid)
              if user.name not in sid_whois:
                sid_whois.update({user.name:[unid]})
              if user.name in sid_whois:
                if unid == "":
                  return
                if unid in sid_whois[user.name]:
                  pass
                else:
                  sid_whois[user.name].append(unid)
              f = open('sid_whois.txt', "w")
              f.write(str(sid_whois))
              f.close
   except:pass
   try:
    msgdata = message.body.split(" ",1)
    if len(msgdata) > 1:
      cmd, args = msgdata[0], msgdata[1]
    else:
      cmd, args = msgdata[0],""
      cmd=cmd.lower() 
    global lockdown
    global newnum
    print(user.name+" - "+message.body)
    if user.name in notif:
        room.message(user.name+", you got ("+str(len(sn[user.name]))+") messages unread. Do irn to read them")
        notif.remove(user.name)
    if user == self.user: return
    if message.body.startswith("vina") or message.body.startswith("Vina") or " vina" in message.body.lower() and not user.name in blacklist:
      if room.name not in simlock:
        if len(args) > 1:
          room.message(__import__("simi").simi(args),True)
        else:
          room.message("Ada apa "+sntonick(user.name)+" ?", True)
    if message.body.startswith("tidur vin"):
      if user.name == "inketsu" or user.name == "yukiineh" or user.name == "lizbeth":
          room.message("Oyasumi *waves*")
          self.setTimeout(1, self.stop, )
    if "vin kamu siapa" in message.body.lower() or "kamu siapa vin" in message.body.lower() and "<" not in message.body[:1] and not user.name in blacklist:
      room.message("Vina itu adek nya ZexScythe ;) @"+user.name, True)
    if message.body.startswith("Test") or message.body.startswith("test") and not user.name in blacklist:
      if room.name not in simlock:
        room.message("<f x10ff3399='1'><br/>@"+user.name+" : Requested a Test<br/>Test Accepted ;)", True)
    if message.body.startswith("oyasumi")or message.body.startswith("Oyasumi"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Oyasumi, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("ohayou")or message.body.startswith("Ohayou"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Ohayou, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("konnichiwa")or message.body.startswith("Konnichiwa"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Konnichiwa, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("malam") or message.body.startswith("Malam"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Tdur bgo besok mulung"]),True)
    if message.body.startswith("afk") or message.body.startswith("AFK") and not user.name in blacklist:
      if room.name not in simlock:
        if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
          room.message (random.choice(["Jangan lama-lama yah @"+user.name+" ;)",]),True)
    if message.body.startswith("back") or message.body.startswith("BACK"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist and not room.name in simlock:
      room.message (random.choice(["Welcome Back, "+sntonick(user.name)+" :x ",]),True)
    if message.body.startswith("brb")or message.body.startswith("BRB") and not user.name in blacklist and not room.name in simlock:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Jangan lama-lama yah @"+user.name+" ;)",]),True)
    if message.body.startswith("off")or message.body.startswith("OFF") and not user.name in blacklist and not room.name in simlock:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Bye "+sntonick(user.name)+" :D ",]),True)
    if message.body == "": return  
    if message.body[0] in ["<"]:   
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""

      ##npcmds
      if cmd == "npcmds":
        room.message("<f x12ff3399='1'>Nekopoi Commands :<f x12ff3399='1'><br/>1.npnew or npnew2 (New Update On Nekopoi.co.uk)<f x12ff3399='1'><br/>2.npsr or npsr2(Nekopoi Search)<f x12ff3399='1'><br/>3.rech(Recommended Hentai)", True)
      if cmd == "rech":
        room.message("Best Recommended Hentai :<f x12ff3399='1'><br/>BOKU NO PICO , Otokonoko Delivery , Euphoria , Kuro No Kyoushitsu , Baka Na Imouto , Please Rape Me! , Rape Rape Rape , Rance01 , Wana Spartansex Spermax , Otome Dori , Sagurare Otome , Saimin Kanojo , Imouto Yuujin , Triple Echi , Hakkoiri Shoujo , Gakuen De Jikan Yo Tomare , Toshi Densetsu , Shiritsu Yarima x Rigakuen , Himekishi Angelica & Olivia , Pretty x Cation , Fella Hame Lips , Aniyome , Miboujin Nikki , ENBO , Yokorenbo , Koiito Kinenbi , Yume Kui , Sei Brunehilde , Wana Hakudaku Mamire , Shiiku x Kanojo , KuroInu , Kanojo x Kanojo x Kanojo , Shin Hitou Meguri , Machi Gurumi , Helter Skelter , JK Series , Kansen Series , Amakano", True)
   
      ##BotStop
      if cmd =="dc":
         if user.name == "yukiineh" or user.name == "inketsu":
          room.message("[Disconnected]")
          self.setTimeout(1, self.stop, )
         else:
           room.message("Maaf siapa ya ?")         
   ## Reg
      if cmd == "reg":
        name = user.name
        name = getUname(room, name)
        if name not in whitelist and name not in player and name not in archwizard and name not in owners and name not in admin and name not in archknight and name not in blacklist:
          room.message(user.name+" ketik <cmds untuk perintah ;)")
          whitelist.append(name)
          f = open("whitelist.txt","w")
          f.write("\n".join(whitelist))
          f.close
        else:
          print("sudah terdaftar")
               
          
    ##check access and ignore
      if self.getAccess(user) == 0: return 
      def pars(args):
        args=args.lower()
        for name in room.usernames:
          if args in name:return name    
      def roompars(args):
        args = args.lower()
        for name in self.roomnames:
          if args in name:return name
      def roomUsers():
          usrs = []
          gay = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          return gay
      
      def getParticipant(arg):
          rname = self.getRoom(arg)
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(rname._userlist) - 1
          for i in rname._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for j in gay:
            if j not in finale:
              finale.append(j)
          return finale
      if cmd == "lockstatus":
        if room.name in locks:
          roomlock = "<f x11FF0000='0'>Command : <b>Locked</b></f>"
        else:
          roomlock = "<f x1133FF33='0'>Command : <b>Unlocked</b></f>"
        room.message("<br/> [Lockstatus] <br/>"+roomlock+"",True)
      
      if lockdown: return
      if user.name in whitelist and user.name in player and room.name in locks: return

      ##COMMANDS!
#Setting up commands for yer bot
 #commands section
#### Invite
      global activated
      global jack
      global convo
      global locked
      global game
      global newnum
      if cmd == "gameon" and self.getAccess(user)>=4:
        if not game:
          game = True
          room.message("Game now is set to <b>on</b>.", True)
      if cmd == "gameoff" and self.getAccess(user)>=4:
        if game:
          game = False
          room.message("Game now is set to <b>off</b>.", True)
      if not game and self.getAccess(user)<=4: return

      if cmd=="register" or cmd=="reg":
         if user.name not in playa:
             playa.append(user.name)
             coin="5000"
             gold="10"
             lvl="1"
             exp="1000"
             up="1"
             cash="10"
             cp="0"
             bank[user.name] = json.dumps([coin,gold])
             stats[user.name] = json.dumps([lvl,exp,up])
             mcash[user.name] = json.dumps([cash,cp])
 
             print("[SAVE] SAVING PLAYER/STATS/MONEY")
             f = open("playa.txt", "w")
             f.write("\n".join(playa))
             f.close()
 
             f = open("mcash.txt", "w")
             for user in mcash:
               cash,cp = json.loads(mcash[user])
               f.write(json.dumps([user,cash,cp])+"\n")
             f.close()
             
             f = open("stats.txt", "w")
             for user in stats:
               lvl,exp,up = json.loads(stats[user])
               f.write(json.dumps([user,lvl,exp,up])+"\n")
             f.close()
             
             f = open("bank.txt", "w")
             for user in bank:
               coin,gold = json.loads(bank[user])              
               f.write(json.dumps([user,coin,gold])+"\n")
             return
      if cmd =="upgrade":
            if self.getAccess(user) >= 1:
              if user.name in waktu2:
                w = json.loads(waktu2[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Please wait for: <b>%s</b>"% string,True)
                  return
              if jack and user.name in waktu11:
                w = json.loads(waktu11[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Please wait for: <b>%s</b>"% string,True)
                  return
              if self.getAccess(user) >= 2:
               if jack:
                coin, gold = json.loads(bank[user.name])
                lvl, exp2, up2 = json.loads(stats[user.name])
                randexp=random.randint(0,1)
                exp=int(exp2)+randexp
                exp=str(exp)
                up=int(up2)+1
                up=str(up)
                string = "[<b>?JACK-MODE!!!?</b>] "+sntonick(user.name)+" upgrade their stats..<b>TOTAL UPGRADE</b>[<b>"+str(up)+"</b>]"
                stats[user.name] = json.dumps([lvl,exp,up])
                room.message(string,True)
                waktu11[user.name] = json.dumps(time.time()+180)
                f = open("mcash.txt", "w")
                for user in mcash:
                  cash,cp = json.loads(mcash[user])
                  f.write(json.dumps([user,cash,cp])+"\n")
                f.close()
                f = open("stats.txt", "w")
                for user in stats:
                  lvl,exp,up = json.loads(stats[user])
                  f.write(json.dumps([user,lvl,exp,up])+"\n")
                f.close()            
                f = open("bank.txt", "w")
                for user in bank:
                  coin,gold = json.loads(bank[user])              
                  f.write(json.dumps([user,coin,gold])+"\n")
               if not jack:
                coin, gold = json.loads(bank[user.name])
                lvl, exp2, up2 = json.loads(stats[user.name])
                randexp=random.randint(0,1)
                exp=int(exp2)+randexp
                exp=str(exp)
                up=int(up2)+1
                up=str(up)
                string = ""+sntonick(user.name)+" upgrade their stats..<b>TOTAL UPGRADE</b>[<b>"+str(up)+"</b>]"
                stats[user.name] = json.dumps([lvl,exp,up])
                room.message(string,True)
                waktu2[user.name] = json.dumps(time.time()+180)
                f = open("mcash.txt", "w")
                for user in mcash:
                  cash,cp = json.loads(mcash[user])
                  f.write(json.dumps([user,cash,cp])+"\n")
                f.close()
                f = open("stats.txt", "w")
                for user in stats:
                  lvl,exp,up = json.loads(stats[user])
                  f.write(json.dumps([user,lvl,exp,up])+"\n")
                f.close()            
                f = open("bank.txt", "w")
                for user in bank:
                  coin,gold = json.loads(bank[user])              
                  f.write(json.dumps([user,coin,gold])+"\n")
              else:
                room.message("Type <reg for playing this game..")
      if cmd =="upgrade":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")
        
      if cmd =="mine":
            user = user.name.lower()
            if user in playa:
              if user in waktu1:
                w = json.loads(waktu1[user])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Please wait for:<b> %s</b>"% string,True)
                  return
              if jack and user in waktu10:
               if self.getAccess(user) >= 2:
                w = json.loads(waktu10[user])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Please wait for:<b> %s</b>"% string,True)
                  return
              if user in playa:
               if jack:
                reward=random.randint(5000,9000)
                reward1=random.randint(5000,9000)
                reward2=random.randint(30,50)
                coin2, gold = json.loads(bank[user])
                lvl, exp2, up = json.loads(stats[user])
                gold2= int(gold)+reward2
                gold2=str(gold2)
                coin= int(coin2)+reward*int(up)
                coin=str(coin)
                exp=int(exp2)+reward1
                exp= str(exp)
                up=int(up)
                string = "[<b>?JACK-MODE!!!?</b>] "+sntonick(user)+" has mined: <b>Gold</b>[<b>+++"+str(reward2)+"</b>], <b>Coins</b>[<b>+++"+str(reward*up)+"</b>], <b>Exp</b>[<b>+++"+str(reward1)+"</b>]</font><br/><b>GAME IS ?<b>BOOSTED</b>?!! GET COINS & EXP 3x THAN USUAL!! AND FASTER!!"
                bank[user] = json.dumps([coin,gold2])
                stats[user] = json.dumps([lvl,exp,up])
                room.message(string,True)
                bank[user] = json.dumps([coin,gold2])
                waktu10[user] = json.dumps(time.time()+240)
                f = open("mcash.txt", "w")
                for user in mcash:
                  cash,cp = json.loads(mcash[user])
                  f.write(json.dumps([user,cash,cp])+"\n")
                f.close()
                f = open("stats.txt", "w")
                for user in stats:
                  lvl,exp,up = json.loads(stats[user])
                  f.write(json.dumps([user,lvl,exp,up])+"\n")
                f.close()            
                f = open("bank.txt", "w")
                for user in bank:
                  coin,gold = json.loads(bank[user])              
                  f.write(json.dumps([user,coin,gold2])+"\n")
               if user in playa and not jack:
                reward=random.randint(1000,3000)
                reward1=random.randint(1000,3000)
                reward2=random.randint(1,20)
                coin2, gold = json.loads(bank[user])
                lvl, exp2, up = json.loads(stats[user])
                gold2= int(gold)+reward2
                gold2=str(gold2)
                coin= int(coin2)+reward*int(up)
                coin=str(coin)
                exp=int(exp2)+reward1
                exp= str(exp)
                up=int(up)
                string = ""+sntonick(user)+" has mined: <b>Gold</b>[+<b>"+str(reward2)+"</b>], <b>Coins</b>[+<b>"+str(reward*up)+"</b>], <b>Exp</b>[+<b>"+str(reward1)+"</b>]</font>"
                bank[user] = json.dumps([coin,gold2])
                stats[user] = json.dumps([lvl,exp,up])
                room.message(string,True)
                bank[user] = json.dumps([coin,gold2])
                waktu1[user] = json.dumps(time.time()+240)
                f = open("mcash.txt", "w")
                for user in mcash:
                  cash,cp = json.loads(mcash[user])
                  f.write(json.dumps([user,cash,cp])+"\n")
                f.close()
                f = open("stats.txt", "w")
                for user in stats:
                  lvl,exp,up = json.loads(stats[user])
                  f.write(json.dumps([user,lvl,exp,up])+"\n")
                f.close()            
                f = open("bank.txt", "w")
                for user in bank:
                  coin,gold = json.loads(bank[user])              
                  f.write(json.dumps([user,coin,gold2])+"\n")
              else:
                room.message("Type <reg for playing this game..",True)
      if cmd =="mine":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")
        
      if cmd =="mgold":
            if self.getAccess(user) >= 1:
              if user.name in waktu0:
                w = json.loads(waktu0[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Wait after : <font color='#9999FF'>%s</font> before you harvest gold again ^o^ "% string,True)
                  return
              if jack and user.name in waktu12:
                w = json.loads(waktu12[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Wait after : <font color='#9999FF'>%s</font> before you harvest gold again ^o^ "% string,True)
                  return
              if self.getAccess(user) >= 2 and not jack:
                randgold = random.randint(1,7)
                coin , gold2 = json.loads(bank[user.name])
                gold = int(gold2) + randgold
                room.message(""+user.name+", get .. <font color='#FF9900'><b>Gold</b>[<b>+"+str(randgold)+"</b>]</font>",True)
                gold = str(gold)          
                bank[user.name] = json.dumps([coin, gold])
                waktu0[user.name] = json.dumps(time.time()+900)
              if self.getAccess(user) >= 2 and jack:
                randgold = random.randint(10,20)
                coin , gold2 = json.loads(bank[user.name])
                gold = int(gold2) + randgold
                room.message("[<b>?JACK-MODE!!!?</b>] "+user.name+", get .. <font color='#FF9900'><b>Gold</b>[+++<b>"+str(randgold)+"</b>]</font>",True)
                gold = str(gold)          
                bank[user.name] = json.dumps([coin, gold])
                waktu12[user.name] = json.dumps(time.time()+500)
              f = open("bank.txt", "w")
              for user in bank:
                coin,gold = json.loads(bank[user])
                f.write(json.dumps([user,coin,gold])+"\n")
              f.close()
            else:
              room.message("You can't do <register first",True)
      if cmd =="mgold":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd == "dice":
            if self.getAccess(user) >= 1:
              if user.name in waktu5:
                w = json.loads(waktu5[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Throw dice at <font color='#9999FF'>%s</font>  (~^o^)~ "% string,True)
                  return
              if self.getAccess(user) >= 1:
                die1=random.randint(1,6)
                die2=random.randint(1,6)
                if str(die1)==str(die2):
                  lvl,exp2,up= json.loads(stats[user.name])
                  x = random.randint(4000,5000)
                  exp= int(exp2)+ x
                  room.message(random.choice(["LUCKY! you got dice with same number - "+str(die1)+" & "+str(die2)+" ("+str(x)+" exp as reward)"]))
                  exp= str(exp)
                  stats[user.name] = json.dumps([lvl,exp,up])
                else:
                  waktu5[user.name] = json.dumps(time.time()+10)
                  room.message(""+user.name+" throw , and got "+str(die1)+" & "+str(die2)+" , Sorry No Reward :( ");return
                f = open("stats.txt", "w")
                for user in stats:
                  lvl,exp,up = json.loads(stats[user])
                  f.write(json.dumps([user,lvl,exp,up])+"\n")
                f.close()
      if cmd =="dice":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd =="mcoin":
        if user.name in waktu14:
                w = json.loads(waktu14[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Wait after : <font color='#9999FF'>%s</font> before you harvest coin again ^o^ "% string,True)
                  return
        if jack and user.name in waktu13:
                w = json.loads(waktu13[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
                  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
                  room.message("Wait after : <font color='#9999FF'>%s</font> before you harvest coin again ^o^ "% string,True)
                  return
        if user.name in playa and not jack:
          randcoin = random.randint(500,1500)
          coin2 , gold = json.loads(bank[user.name])
          coin = int(coin2) + randcoin
          room.message("Vina Give "+str(user.name)+", Coins[<font color='#9999FF'><b>+"+str(randcoin)+"</b></font>]",True)
          coin = str(coin)
          waktu14[user.name] = json.dumps(time.time()+60)
          bank[user.name] = json.dumps([coin, gold])
        if user.name in playa and jack:
          randcoin = random.randint(1500,2000)
          coin2 , gold = json.loads(bank[user.name])
          coin = int(coin2) + randcoin
          room.message("[<b>?JACK-MODE!!!?</b>] Vina gives "+str(user.name)+", Coins FOR[<font color='#9999FF'><b>+++"+str(randcoin)+"</b></font>]",True)
          coin = str(coin)
          waktu13[user.name] = json.dumps(time.time()+180)
          bank[user.name] = json.dumps([coin, gold])
        if user.name not in playa:
          room.message("You can't do <reg first",True)
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING MONEY...")
      if cmd =="mcoin":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")
      if cmd =="bag" and user.name in playa:
        user = user.name.lower()
        if user in inven:
          j = list()
          q = 1
          for i in inven[user]:
            v = inven[user][i]
            j.append("(<b>%s</b>). %s:(<b>%s</b>)" % (q,i,v))
            q += 1
          room.message(sntonick(user)+" have:<br/> "+" ".join(j),True)
        else:
          room.message("Nothing..",True)
      if cmd == "sas":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")
      if cmd == "shop":
        lvl , exp , up = json.loads(stats[user.name])
        coin , gold= json.loads(bank[user.name])
        x=random.randint(1000,4000)
        x1=random.randint(7000,15000)
        fo = int(lvl)*100000
        go = int(50)
        lu = int(lvl)*5000
        co = int(lvl)*25000
        fo2 = int(lvl)*x
        lu2 = int(lvl)*x1
        room.message("<br/>(<b>1</b>). <b>Fortune</b>("+str(fo)+" coins) - Have depressed because of exp? Don't worry just buy me ! [<b><u>Buy get "+str(fo2)+" Exp</u></b>] <br/>(<b>2</b>). <b>Lucky</b>("+str(go)+" golds) - Dont have coin to buy something *bored*? I had it ;D [<b><u>Buy get "+str(lu2)+" Coins</u></b>]  <br/>(<b>3</b>). <b>Cookie</b>("+str(co)+" coins) - Wanna cookie?? I have what you want 8) [<b><u>Buy get 1-7 Golds</u></b>]",True)

      if cmd == "buy" and len(args) >= 1:
        args = args.lower()
        try:
          args, value = args.split(" ", 1)
          if "-" in value:
            room.message("Type The Name Of Items",True);return
        except:
          args = args
          value = "1"
        value = int(value)
 
        coin , gold= json.loads(bank[user.name])
        lvl,exp,up= json.loads(stats[user.name])
        coin , gold = int(coin),int(gold)
        itemlist = ["fortune","lucky","cookie"]
        if args not in itemlist:
          room.message("Invalid item,  ",True);return
        if args== "fortune":
          coin=coin-(int(lvl)*100000*value)
          if coin <= 0:room.message("not enough coin, you need <b><font color='#CCCC66'>%s</font></b> coin"%(75000*value),True);return
 
        if args== "lucky":
          gold=gold-(int(lvl)*50*value)
          if gold <= 0:room.message("not enough golds, you need <b><font color='#CCCC66'>%s</font></b> golds"%(50*value),True);return
 
        if args== "cookie":
          coin=coin-(int(lvl)*25000*value)
          if coin <= 0:room.message("not enough coin, you need <b><font color='#CCCC66'>%s</font></b> coin"%(27836*value),True);return
 
 
        if user.name in inven:            
          if args in inven[user.name]:
            val = inven[user.name][args]
            val = val + value    
            inven[user.name][args] = val
          else:
            inven[user.name].update({args:value})
        else:
          inven.update({user.name:{args:value}})
       
        coin , gold = str(coin),str(gold)
        bank[user.name] = json.dumps([coin,gold])
        room.message(user.name+" has bought <b><font color='#CCCC66'>%s</font></b> %s "%(value,args),True)
      if cmd =="buy":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd == "use" and len(args) >= 1:
        args = args.lower()
        try:
          args, value = args.split(" ", 1)
          if "-" in value:
            room.message("Type The Name Of Items");return
        except:
          args = args
          value = "1"
        value = int(value)
        coin , gold = json.loads(bank[user.name])
        lvl, exp, up = json.loads(stats[user.name])
        coin , gold = int(coin),int(gold)
        lvl , exp , up = int(lvl),int(exp),int(up)
        itemlist = ["fortune","lucky","cookie"]
        if args not in itemlist and inven:
          room.message("Invalid item,  ");return
        string = ""
        if args== "fortune":            
          fo=random.randint(1000,4000)
          a = value*fo
          exp = int(exp) + a
          exp = str(exp)
          stats[user.name] = json.dumps([lvl,exp,up])
          string += " & got <b>Exp</b>[<b>+"+str(a)+"</b>] <b>Total Exp</b>: [<b>"+str(exp)+"</b>]"
        if user.name in inven:            
          if args in inven[user.name]:
            val = inven[user.name][args]
            val = val - value
            if val < 0:
              val = 0
              room.message("no item");return
              
        if args== "lucky":            
          lu=random.randint(7000,15000)
          b = value*lu
          coin = int(coin) + b
          coin = str(coin)
          string += " & got: <b>Coins</b>[<b>+"+str(b)+"</b>] <b>Total Coins</b>: [<b>"+str(coin)+"</b>]"            
        if user.name in inven:            
          if args in inven[user.name]:
            val = inven[user.name][args]
            val = val - value
            if val < 0:
              val = 0
              room.message("no item");return

        if args== "cookie":            
          co=random.randint(1,7)
          c = value*co
          gold = int(gold) + c
          gold = str(gold)
          string += " & got: <b>Golds</b>[<b>+"+str(c)+"</b>] <b>Total Golds</b>: [<b>"+str(gold)+"</b>]"
        if user.name in inven:            
          if args in inven[user.name]:
            val = inven[user.name][args]
            val = val - value
            if val < 0:
              val = 0
              room.message("no item");return
            inven[user.name][args] = val

            room.message(user.name+" has use <b><font color='#CCCC66'>%s</font></b> %s %s"%(value,args,string),True)
          else:room.message("no item");return
        coin , gold = str(coin),str(gold)
        bank[user.name] = json.dumps([coin,gold])
        stats[user.name] = json.dumps([lvl,exp,up])

      if cmd =="use":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd == "jack" and user.name.lower() == "inketsu":
        jack = True
        room.message("JACK mode Activated")


      if cmd == "rjack" and user.name.lower() == "inketsu":
        jack = False
        room.message("Deactivating JACK mode")

      if cmd == "jack" and user.name.lower() == "yukiineh":
        jack = True
        room.message("JACK mode Activated")


      if cmd == "rjack" and user.name.lower() == "yukiineh":
        jack = False
        room.message("Deactivating JACK mode")

      if cmd == "jack" and user.name.lower() == "faptaliti":
        jack = True
        room.message("JACK mode Activated")


      if cmd == "rjack" and user.name.lower() == "faptaliti":
        jack = False
        room.message("Deactivating JACK mode")

      if cmd =="lvlstats"  and self.getAccess(user) >=1:
         for i in stats:
            try:
               lvl , exp , up = json.loads(stats[i])
            except:pass
            lvlstats[i]=int(lvl)
         res = (sorted(lvlstats, key=lvlstats.get, reverse=False))
         j = []
         val = 1
         for k in res:
            up,exp,lvl = json.loads(stats[k])
            j.append('<i> %s </i> (<b>%s</b>:<b>%s</b>: <b>%s</b>)'% (k,lvl,exp,up))
            val = val +1
         room.message("<br/>Awesome Player's <br/>%s"%"<br/>".join(j[:10]),True)

      if cmd == "cgive" and len(args) >= 1:
            args, value = args.split(" ", 1)
            if args not in playa:
                room.message(""+args+" doesn't have bank. tell him to make one by typing <reg",True)
                return
            coin1 , gold1= json.loads(bank[user.name])
            coin2 , gold2= json.loads(bank[args])
            if "-" in value:
                room.message("Type The Value How Much You Want To Transfer ..",True);return
            coin1, coin2, value = int(coin1), int(coin2), int(value)    
            coin1  = coin1 - value  
            coin2 = coin2 + value
            if coin1 < 0:room.message("Not enough coin to transfer",True);return
            room.message(""+user.name+" has given  %s  %s  coins!"%(args, str(value)),True)
            bank[user.name] = json.dumps([coin1,gold1])
            bank[args] = json.dumps([coin2,gold2])
      if cmd =="cgive":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd == "ggive" and len(args) >= 1:
            args, value = args.split(" ", 1)
            if args not in playa:
                room.message(""+args+" doesn't have bank. tell him to make one by typing <reg",True)
                return
            coin1 , gold1= json.loads(bank[user.name])
            coin2 , gold2= json.loads(bank[args])
            if "-" in value:
                room.message("Type The Value How Much You Want To Transfer ..",True);return
            gold1, gold2, value = int(gold1), int(gold2), int(value)    
            gold1  = gold1 - value  
            gold2 = gold2 + value
            if gold1 < 0:room.message("Not enough gold to transfer",True);return
            room.message(user.name+" has give  %s  %s  golds!"%(args, str(value)),True)
            bank[user.name] = json.dumps([coin1,gold1])
            bank[args] = json.dumps([coin2,gold2])
      if cmd == "ggive":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")

      if cmd == "atk":        
            args, value = args.split(" ", 2)
            if args not in playa:
                room.message(""+args+" doesn't have bank. tell him to make one by typing <reg",True)
                return
            coin1 , gold1= json.loads(bank[user.name])
            coin2 , gold2= json.loads(bank[args])
            if "-" in value:
                room.message("Type The Value How Much You Want To Attack ..",True);return
            coin1, coin2, value = int(coin1), int(coin2), int(value)    
            coin1  = coin1 - value  
            coin2 = coin2 - value
            if coin1 < 0:room.message("Not enough coin to Attack , try low value",True);return
            room.message(""+user.name+" has attack  %s for %s  coins!"%(sntonick(args), str(value)),True)
            bank[user.name] = json.dumps([coin1,gold1])
            bank[args] = json.dumps([coin2,gold2])
      if cmd == "atk":
        f = open("stats.txt", "w")
        for user in stats:
          lvl,exp,up = json.loads(stats[user])
          f.write(json.dumps([user,lvl,exp,up])+"\n")
        f.close()
        f = open("bank.txt", "w")
        for user in bank:
          coin,gold = json.loads(bank[user])
          f.write(json.dumps([user,coin,gold])+"\n")
        f.close()
        print("[SAVE] SAVING HALF-MASTERS-LVL-2")
        f = open("playa.txt", "w")
        f.write("\n".join(playa))
        f.close()
        print("[SAVE] SAVING WHITELIST-LVL-1")
        f = open("whitelist.txt", "w")
        f.write("\n".join(whitelist))
        f.close()
        try:
         print("[SAVE] SAVING All Stuff...")
         f = open('inven.txt','w')
         f.write(str(inven))
         f.close()
        except:print("error")
      elif cmd == "report" and len(args) > 0:
            if args[0] == ".":
                args = args[1:]
            elif pars(args) != None and not args[0] == ".":
                args = pars(args)
            name = args.split()[0].lower()
            if name == "inketsu":
                room.message("no way in hell :P")
            else:
                room.flagUser(ch.User(user.name))
                self.getRoom("khususme").message("%s Reporting %s in %s" % (sntonick(user.name), sntonick(name),  room.name),True)
                room.message ("<b>%s</b> has been reported, do not resist the system" % sntonick(name), True)
      if cmd=="gcmds":
        room.message("Game cmd list: gameon[owners], gameoff[owners], dice, stats, lvlstats, money, cgive , ggive, atk, buy, bag, shop, upgrade, mgold, mcoin, mine, register, sas/save game stats. <b> 1st. do register/reg..</b></font>",True)
      if cmd == "gcoff":
        room.message("Game CMD List Di Off In Dolo ;)", True)        
      if cmd =="stats" or cmd=="cstats":
          user = user.name.lower()
          if user in stats:
            lvl,exp,up= json.loads(stats[user])
            left=(int(exp)-int(lvl)*2500)
            left2=int(lvl)*2500
            racost=int(lvl)*2500
            room.message("<br/>-Name: "+ sntonick(user)+"<br/>-Level: <font color='#FF0033'><b>"+str(up)+"</b></font> <br/>-Exp: <font color='#FFCC00'><b>"+str(exp)+" ("+str(left)+"/"+str(left2)+") </b></font><br/>-Cost: <font color='#9999FF'><b>"+str(racost)+"</b></font> Exp To Next Level",True)
          else:        
            room.message("<br/>-Name: "+ sntonick(user)+"<br/>-Level: <font color='#FF0033'><b>"+str(up)+"</b></font> <br/>-Exp: <font color='#FFCC00'><b>0</b></font> <br/>-Cost: No COST .. do register first",True)		  

      if cmd =="money" or cmd=="cmoney":
        if user.name in bank:
          coin, gold = json.loads(bank[user.name])
          room.message("<br/><br/>-Name: "+ sntonick(user.name)+"<br/>-Coin: <font color='#9999FF'><b>"+str(coin)+"</b></font><br/>-Gold: <font color='#FF9900'><b>"+str(gold)+"</b></font>", True)
      
      ##RPG
      if cmd =="rpg" or cmd =="crpg":
        if user.name not in player:
          player.append(user.name)
          cash="500000"
          eris="1000"
          exp="100"
          level="1"
          rbank[user.name] = json.dumps([cash,eris])
          rstats[user.name] = json.dumps([level])
          room.message(" @"+user.name+" you already registered xD", True)

          f = open("player.txt", "w")
          f.write("\n".join(player))
          f.close()

          f = open("rbank.txt", "w")
          for user in rbank:
            cash,eris = json.loads(rbank[user])
            f.write(json.dumps([user,cash,eris])+"\n")
          f.close()

          f = open("rstats.txt", "w")
          for user in rstats:
            level = json.loads(rstats[user])
            f.write(json.dumps([user,level])+"\n")
          f.close()
          return
      if cmd =="info" or cmd =="rstats":
        user = user.name.lower()
        if user in rstats:
          level= json.loads(rstats[user])
          cash, eris= json.loads(rbank[user])
          room.message("<br/><font color='#F6ECD3'>.<br/>-Nickname: "+ sntonick(user)+"<br/>-Level: <font color='#FF0033'><b>"+str(level)+"</b><font> <br/>-Cash : <font color='#FF0033'><b>"+str(cash)+"</b><font> <br/>-Eris : <font color='#FF0033'><b>"+str(eris)+"<b/><font><br/>Created by : Inketsu", True)                         
        else:
         if user not in player:
           room.message("You are not an adventurer use cmd rpg to become a adventurer ;)", True)
      ##AFKlist
      if cmd == "afklist":
        room.message("<br/><f x120000FF='0'><b>Daftar orang Yang sedang AFK:</b></f> %s" % (", ".join(afks)),True)
        
      #Find
      if cmd == "find" and len(args) > 0:
        name = args.split()[0].lower()
        if not ch.User(name).roomnames:
          room.message("aku tidak tau")
        else:
          room.message("kamu dapat menemukan  %s Di %s" % (args, ", ".join(ch.User(name).roomnames)),True)

      ##RB
      elif cmd == "rb":
        if room.name not in locks:
          if args == "":
            rain = rainbow('Rainbow!')
            room.message(rain,True)
          else: 
             rain = rainbow(args)
             room.message(rain,True)

      elif cmd == "rb2":
        if args == "":
          rain = rainbow('Rainbow!')
          room.message(rain)
        else: 
            rain = rainbow(args)
            room.message(rain)
      
      ##cmds
      elif cmd == "cmds":
        if room.name not in locks:
          if user.name in owners and not user.name in admin and not user.name in archknight and not user.name in whitelist:
            room.message("<br/>"+user.name+" Rank<f x12000000='Elephant'>[<f x12FF0000='Elephant'>D<f x12FF7F00='Elephant'>o<f x12FFFE00='Elephant'>u<f x1280FF00='Elephant'>s<f x1201FF00='Elephant'>h<f x1200FF7F='Elephant'>i<f x12000000='Elephant'>] "+"<br/>"+"<f x12FF0000='Ravie'> Commands :<f x12000000='Elephant'><br/>ping , rb , rb2 , wl , cso , pfpic , mini , prof or profile , gs(Google search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote) , join , leave , mydict , nick , staff , setnick , mynick , seenick , profile , setrank , rank , myrank , ranker , c(clear) , del , sf , sfc, snc , sfz , myip , mc , mc2 , lock , unlock , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True) 
          if user.name in admin and not user.name in owners and not user.name in archknight and not user.name in whitelist:
            room.message("<br/>"+user.name+" Rank<f x120000FF='Elephant'>[Luzrov] "+"<br/>"+"<f x12FF0000='Ravie'> Commands :<f x120000FF='Elephant'><br/>ping , rb , rb2 , wl , cso , pfpic , prof or profile , gs(Google search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote) , join , leave , mydict, nick  , staff , setnick , mynick , seenick , profile , setrank , rank , myrank , ranker , c(clear) , del , sf , sfc, snc , sfz , myip , mc , mc2 , lock , unlock , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True) 
          if user.name in archwizard and not user.name in owners and not user.name in admin and not user.name in whitelist:
            room.message("<br/>"+user.name+" Rank<f x12FF0000='Elephant'>[Fethmus] "+"<br/>"+"<f x12FF0000='Ravie'> Commands :<f x12FF0000='Elephant'><br/>ping , rb , rb2 , wl , cso , pfpic , prof or profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote), mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat), lock, unlock , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True)
          if user.name in archknight and not user.name in owners and not user.name in admin and not user.name in whitelist:
            room.message("<br/>"+user.name+" Rank<f x1200cc00='Elephant'>[Yurlin] "+"<br/>"+"<f x12FF0000='Ravie'> Commands :<f x1200cc00='Elephant'><br/>ping , rb , rb2 , wl , cso , pfpic , prof or profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , sn(sendnote) , rn(readnote), mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True)
          if user.name in player and not user.name in owners and not user.name in admin and not user.name in whitelist:
            room.message("<br/>"+user.name+" Rank[Player] "+"<br/>"+" Commands :<br/>ping , rb , rb2 , wl , cso , pfpic , prof or profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , sn(sendnote) , rn(readnote), mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True)
          if user.name in whitelist and not user.name in owners and not user.name in admin and not user.name in archknight:
            room.message("<br/>"+user.name+" Rank[Whitelist] "+"<br/>"+" Commands :<br/>ping , rb , rb2 , wl , cso , pfpic , prof or profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , sn(sendnote) , rn(readnote), mydict , nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lockstatus , bgimg , bgtime.<br/><f x12ff3399='1'>New Commands : npcmds(Nekopoi Commands) , gcmds(game)",True)
          
      ### MultiChat
      elif cmd == "multichat" or cmd == "mc" or cmd == "MultiChat" or cmd == "Mc":
        if args == "":
            room.message("My Default room : www.vina-chat.chatango.com")
        else:
            room.message("Done ! , This is your Room : http://ch.besaba.com/chat/html5/?"+args+"!")
      elif cmd == "multichat2" or cmd == "mc2":
        if args == "":
            room.message("My Default room : http://ch.besaba.com/chat/html5/?hentaipoi!,androh-chat!,zexchat!,vina-chat!")
        else:
            room.message("Done : http://ch.besaba.com/chat/html5/?"+(args)+"!")
      #### MyIp
      elif cmd =="myip" or cmd == "MyIp" or cmd == "MyIP" or cmd == "My IP Adress":
        try:
         room.message("IP address kamu adalah : "+message.ip)
        except:
         room.message("Gagal melihat IP address, Aku bukan mods disini.")
      ##testcmd
      if cmd == "npnew":
        if room.name not in locks:
          room.message(newPoi(), True)
      if cmd == "npnew2":
        if room.name not in locks:
          room.message(newPoi2(), True)
      if cmd == "bgtime":
        if room.name not in locks:
          room.message(bgtime(args), True)
      if cmd == "npsr":
        if room.name not in locks:
          room.message(serPoi(args), True)
      if cmd == "npsr2":
        if room.name not in locks:
          room.message(serPoi2(args), True)
  
      ##List Mods
        #List of Mods and Owner name in the current room you're in
      elif cmd == "mods" or cmd == "Mods":
        args = args.lower()
        if not args:
           room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <u><b>"+(room.ownername)+"</b></u>  <br/><font color='#9999FF'><b>Mods</b></font>: "+", ".join(room.modnames), True)
           return
        if args in self.roomnames:
           moda = self.getRoom(args).modnames
           own = self.getRoom(args).ownername
           room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <b><u>"+(own)+"</u></b>  <br/><font color='#9999FF'><b>Mods</b></font>:  "+",  ".join(moda), True)
        else:
           self.joinRoom(args)
           cek_mods[user.name] = json.dumps([room.name,args])
    
      #### Ban / Unban
      if cmd == "ban":
          if room.getLevel(user) > 0:
            if room.getLevel(self.user) > 0 :
              room.banUser(ch.User(args))
              room.message(args.title()+" has been Banned")
              self.pm.message(ch.User(args.lower()), "You have been banned from %s by %s." % (room.name, user.name))
                 
      if cmd == "unban":
          if room.getLevel(user) > 0:
            if room.getLevel(self.user) > 0:
              room.unban(ch.User(args))
              room.message(args.title()+" has been UnBanned")
              self.pm.message(ch.User(args.lower()), "You have been unbanned from %s by %s." % (room.name, user.name))
       #### Restart
      elif cmd =="restart" or cmd == "Restart" or cmd == "Reconnect" or cmd == "reconnect" and self.getAccess(user) >= 3:
         if user.name in owners:
           room.reconnect()
         else:
           room.message("Ce ??? *lol*")
					
      ## Ban List
      if cmd == "banlist" and self.getAccess(user) >= 1:
        room.message("The banlist is: "+str(room.banlist))
        
  
      ##Setnick
      if cmd == "setnick":
        if self.getAccess(user) < 2:return
        try:
          if args in owners:
            room.message("Ettt,Gaboleh nakal ;)")
          if args:
            user, nick = args.split(" ",1)
            nicks[user]=json.dumps(nick)
            room.message("Sukses")
            f = open("nicks.txt","w")
            for user in nicks:
              nick = json.loads(nicks[user])
              f.write(json.dumps([user,nick])+"\n")
            f.close()
          else:
            room.message("Who?")
        except:
          room.message("The nick please")   
              
      ##Setrank
      if cmd == "setrank": 
        if self.getAccess(user) < 2:return
        try:
          if len(args) >= 3:
            name = args
            if pars(name) == None:
                name = name
            elif pars(name) != None:
                name = pars(name)
            name, rank = args.lower().split(" ", 1)
            if rank == "1":
              owners.append(name)
              f = open("owners.txt", "w")
              f.write("\n".join(owners))
              f.close()
              room.message("[Doushi-Sama]")
              if name in admin:
                admin.remove(name)
                f = open("admin.txt", "w")
                f.write("\n".join(admin))
                f.close()
              if name in archwizard:
                archwizard.remove(name)
                f = open("archwizard.txt", "w")
                f.write("\n".join(archwizard))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in player:
                player.remove(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "2":
              admin.append(name)
              f = open("admin.txt", "w")
              f.write("\n".join(admin))
              f.close()
              room.message("Sukses Rank kamu [Luzrov Rulay]")
              if name in archwizard:
                archwizard.remove(name)
                f = open("archwizard.txt", "w")
                f.write("\n".join(archwizard))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in player:
                player.remove(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "3":
               archwizard.append(name)
               f = open("archwizard.txt", "w")
               f.write("\n".join(archwizard))
               f.close()
               room.message("Sukses Rank kamu [Fethmus Mioma]")
               if name in admin:
                 admin.remove(name)
                 f = open("admin.txt", "w")
                 f.write("\n".join(admin))
                 f.close()
               if name in archknight:
                 archknight.remove(name)
                 f = open("archknight.txt", "w")
                 f.write("\n".join(archknight))
                 f.close()
               if name in player:
                 player.remove(name)
                 f = open("player.txt", "w")
                 f.write("\n".join(player))
                 f.close()
               if name in whitelist:
                 whitelist.remove(name)
                 f = open("whitelist.txt", "w")
                 f.write("\n".join(whitelist))
                 f.close()
            if rank == "4":
                archknight.append(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
                room.message("Sukses Rank kamu [Lukeim Yurlin]")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in player:
                  player.remove(name)
                  f = open("player.txt", "w")
                  f.write("\n".join(player))
                  f.close()
                if name in whitelist:
                  whitelist.remove(name)
                  f = open("whitelist.txt", "w")
                  f.write("\n".join(whitelist))
                  f.close()
            if rank == "5":
                player.append(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
                room.message("Sukses [Player]")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in archknight:
                  archknight.remove(name)
                  f = open("archknight.txt", "w")
                  f.write("\n".join(archknight))
                  f.close()
                if name in whitelist:
                  whitelist.remove(name)
                  f = open("whitelist.txt", "w")
                  f.write("\n".join(whitelist))
                  f.close()
            if rank == "6":
                whitelist.append(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
                room.message("Sukses [Whitelist]")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in archknight:
                  archknight.remove(name)
                  f = open("archknight.txt", "w")
                  f.write("\n".join(archknight))
                  f.close()
                  
        except:
              room.message("something wrong")

     # clear
      elif cmd == "c":
          if room.getLevel(self.user) > 1:
            if self.getAccess(user) >= 2 or room.getLevel(user) == 2:
              room.clearall(),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
            else: room.message("Only rank 2+ or the room owner can do this")
          else:
            room.message("vina bukan mods disini :|")
      ##delete chat  
      elif (cmd == "delete" or cmd == "dl" or cmd == "del"):
            if self.getAccess(user) >= 2 or room.getLevel(user) == 2:
              name = args.split()[0].lower()
              name = getUname(room, name)
              room.clearUser(ch.User(name))
            else:room.message("kamu tidak bisa melakukannya!!")
      ##hentaipoi Spook
      if cmd == "hsp":
        if self.getAccess(user) > 5:
          self.getRoom("hentaipoi").message(args)
          room.message("_shhh ")
        else:
          room.message("Vina tidak ada di room itu")
      ##Anibatch Spook
      if cmd == "sab":
        if self.getAccess(user) > 2:
          self.getRoom("anibatch").message(args)
          room.message("_shhh ")
        else:
          room.message("Can't XD")
      ##Spook
      if cmd == "whois" or cmd == "who" or cmd == "w":
          if not args :
            room.message("FAIL!! Do 'w<space>nick");return
          args = args.lower()
          if args[0] == "+":
            args = args[1:]
          elif pars(args) != None and not args[0] == "+":
            args = pars(args)
          try:
            f = open("ip_whois.txt", "r")
            ip_whois = eval(f.read())
            f.close()
          except:pass
          try:
            f = open("sid_whois.txt", "r")
            sid_whois = eval(f.read())
            f.close()
          except:pass
          ip_ver = getWhois.whois(ip_whois, args)
          sid_ver = getWhois.whois(sid_whois, args)
          if ip_ver == None and sid_ver == None:
            room.message("No alias found.")
            return
          room.message("Currently known alias(es) of %s:<br/>%s: %s.<br/>%s: %s."% (args.title(), "UnID Version", sid_ver, "IP Version", ip_ver), True)
      if cmd == "spook" or cmd == "sp":
        try:
          name, body = args.split(" ", 1)
          if name in self.roomnames :
            self.getRoom(name).message(body)
            room.message("_shhh ")
          else:
            room.message("Vina tidak ada di room itu")
        except:room.message("error")
      ##fax
      if cmd == "fax" or cmd == "Fax":
        try:
          name, body = args.split(" ", 1)
          l = "http://ch.besaba.com/mty.htm?"+room.name+"!"
          if name in self.roomnames :
            self.getRoom(name).message('[<font color="#6699CC"><b>Message</b></font> - %s ] in <a href=\"%s" target=\"_blank\"><u>%s</u></a> : <font color="#66FFFF"><i> %s <i></font>' % (sntonick(user.name), l, room.name, body),True)
            room.message("Sent")
          else:
            room.message("I haven't joined that room")
        except:room.message("error")    
          


      ##Ranker
      if cmd == "ranker":
        if room.name not in locks:
          room.message("<br/><f x12000000='0'><b>♕.Doushi:</b></f> %s<br/><f x120000FF='0'><b>♖.Luzrov Rulay:</b></f> %s<br/><f x12FF0000='0'><b>♗.Fethmus Mioma:</b></f> %s<br/><f x1200cc00='0'><b>♗Lukeim Yurlin♗:</b></f> %s" % (", ".join(owners), ", ".join(admin), ", ".join(archwizard), ", ".join(archknight)),True)
      ##RankBoard
      if cmd == "rankboard":
        room.message("<br/><f x120000FF='0'><b>My Rank Board</b></f><br/><f x12000000='0'><b>♕.Doushi:</b></f> %s<br/><f x120000FF='0'><b>♖.Luzrov Rulay:</b></f> %s<br/><f x12FF0000='0'><b>♗.Fethmus Mioma:</b></f> %s<br/><f x1200cc00='0'><b>♗Lukeim Yurlin♗:</b></f> %s<br/><<f x121BFF00='0'><b>Whitelist:</b></f> %s</br><f x1200FF98><b>Player:</b></f> %s<br/><f x12FF00FF='0'><b>Blacklist:</b></f> %s" % (", ".join(owners), ", ".join(admin), ", ".join(archwizard), ", ".join(archknight), ", ".join(whitelist), ", ".join(player), ", ".join(blacklist)),True)
      ##staff
      if cmd == "staff":
        room.message("<br/><f x120000FF='0'><b>Owner:</b></f> %s<br/><f x12FF0000='0'><b>Admin:</b></f> %s" % (", ".join(owners), ", ".join(admin)),True)

      ##GIS
      if cmd == "gis":
        if room.name not in locks:
          room.message(gis(args),True)
      ##GS
      if cmd == "gs":
        if room.name not in locks:
          room.message(gs(args),True)

      if cmd == "pfpic" or cmd == "pfpict":
        if room.name not in locks:
                link = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                room.message("<br/>"+"User ID : "+args+""+"<br/>Profile Picture :<br/>"+link,True)    
    ##Eval
      if cmd == "ev" or cmd == "eval" or cmd == "e":
        if self.getAccess(user) == 6:
          ret = eval(args)
          if ret == None:
            room.message("Done")
            return
          room.message(str(ret))

      ##Say
      if cmd == "say":
        room.message(args)

      ##Random User
      if cmd == "randomuser":
        room.message(random.choice(room.usernames))
        

          
        ##Check if Mod
	#not really important
      elif cmd == "ismod":
        user = ch.User(args)
        if room.getLevel(user) > 0:
          room.message("yesh")
        else:
          room.message("nope")

      ## Youtube
      elif cmd == "youtube" or cmd == "yt":
        if room.name not in locks:
          if args:
            room.message(tube(args),True)
      ## cso
      if cmd=="cso":
       if len(args)>0:
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+" does not exist on chatango.")
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                print(line)
                offline = True
            if offline:
              room.message(args+" sedang <f x11FF0000='8'>Offline</f>",True)
            if not offline:
              room.message(args+" sedang <f x1133FF33='8'>Online</f>",True)
       else:
          room.message("<f x11FF6600='8'>I need the username of target :)</f>", True)
      ## upTime
      elif cmd == "uptime" or cmd == "ut" and self.getAccess(user) >= 2:
          room.message("Server uptime: %s" % uptime())
      ## Broadcast
      elif cmd=="bc" and self.getAccess(user) >= 4:
          r = room.name
          l = "http://ch.besaba.com/mty.htm?"+r+"+"
          for room in self.rooms:
            room.message("[<font color='#6699CC'><b>Broadcast</b></font>] from - "+sntonick(user.name)+ " : <font color='#33FF33'><i>"+args+"<i></font>", True)              
      elif cmd == "mads" and self.getAccess(user) >= 4:
          r = room.name
          l = "http://ch.besaba.com/mty.htm?"+r+"+"
          for room in self.rooms:
            room.message(args, True)
    #
    ###### Define            
      elif cmd == "define" or cmd == "df" and len(args) > 0:
          try:
            try:
              word, definition = args.split(" as ",1)
              word = word.lower()
            except:
              word = args
              definition = ""
            if len(word.split()) > 4:
              room.message("Fail")
              return
            elif len(definition) > 0:
              if word in dictionary:
                room.message("%s defined already" % user.name.capitalize())
              else:
                dictionary[word] = json.dumps([definition, user.name])
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message("Definition Saved")
            else:
              if word in dictionary:
                definition, name = json.loads(dictionary[word])
                room.message("<br/>ID : %s<br/>Keyword : %s<br/>Definition:<br/>%s" % (name, word, definition),True)
              else:
                room.message(args+" is not defined")
          except:
            room.message("something wrong")
            
                
      elif cmd == "rank":
        if not args:
            if user.name in owners and not user.name in whitelist:
              room.message(user.name+" Kamu Rank 1 [Doushi(OWNER)] ",True)
            elif user.name in admin and not user.name in archwizard and not user.name in player and not user.name in whitelist and not user.name in archknight and not user.name in owners:
              room.message(user.name+" Kamu Rank 2 [Luzrov Rulay(ADMIN)] ",True)
            elif user.name in archwizard and not user.name in player and not user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message(user.name+" Kamu Rank 3 [Fethmus Mioma]",True)
            elif user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message(user.name+" Kamu Rank 4 [Lukeim Yurlin]",True)
            elif user.name in player and not user.name in archwizard and not user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message(user.name+" Kamu Rank 5 [Player]",True)
            elif user.name in whitelist and not user.name in owners:
              room.message(user.name+" Kamu Rank 6 [Whitelist]",True)
            elif user.name not in whitelist and not user.name not in archknight and user.name not in admin and user.name not in owners and user.name not in archwizard and user.name not in player:
              room.message(user.name+" Kamu Belum terdaftar",True)
        if args:
              sss = args
              if sss in owners:
                  room.message(sss.title()+" Rank Dia 1 [Doushi(OWNER)] ",True)
              if sss in admin:
                  room.message(sss.title()+" Rank Dia 2 [Luzrov Rulay(ADMIN)] ",True)
              if sss in archwizard:
                  room.message(sss.title()+" Rank Dia 3 [Fethmus Mioma] ",True)
              if sss in archknight:
                  room.message(sss.title()+" Rank Dia 4 [Lukeim Yurlin] ",True)
              if sss in player:
                  room.message(sss.title()+" Rank Dia 5 [Player] ",True)
              if sss in whitelist:
                  room.message(sss.title()+" rank Dia 6 [Whitelist] ",True)   
              if sss not in owners and sss not in admin and sss not in archknight and sss not in whitelist and sss not in archwizard and sss not in player:
                  room.message(sss.title()+" Tidak ada rank :) ")

      ### Lock/Unlock

      
      ##simi Lock
      if cmd == "mute" and self.getAccess(user) >= 2:
        if args:
          if args in simlock:
            room.message("_shhh")
          if args in self.roomnames:
            simlock.append(args)
            f = open("simlock.txt", "w")
            f.write("\n".join(simlock))
            f.close()
            room.message("Muted: <b>%s<b/>" % args, True)
          else: room.message("Only rank 3+ can do that")
        if not args:
          if room.name not in simlock:
             simlock.append(room.name)
             f = open("simlock.txt", "w")
             f.write("\n".join(simlock))
             f.close()
             room.message("Muted: <b>%s</b>" % room.name,True)
          else:
             room.message(":|")
      ##Simi unlock
      if cmd == "unmute" and self.getAccess(user) >= 2:
        if args:
          if args in simlock and args in self.roomnames:
            simlock.remove(args)
            f = open("simlock.txt", "w")
            f.write("\n".join(simlock))
            f.close()
            room.message("Unmuted: <b>%s<b/>" % args, True)
          if args not in simlock:
            room.message("*lol*")
        if not args:
          if room.name in simlock:
             simlock.remove(room.name)
             f = open("simlock.txt", "w")
             f.write("\n".join(simlock))
             f.close()
             room.message("Unmuted: <b>%s<b/>" % room.name,True)
          else:
             room.message("*lol*")


                  
      ###lock
      if cmd == "lock" and self.getAccess(user) >= 2:
        if user.name in blacklist:
          room.message("You can't do that.. ;D")
          return
        if args in locks:
          room.message("It's already locked.. ;D")
          return
        if args in self.roomnames:
          if user.name in owners or user.name in admin:
            locks.append(args)
            room.message("Locked: <b>%s</b>" % args, True)
            f = open("locks.txt", "w")
            f.write("\n".join(locks))
            f.close()
          else: room.message("Only rank 3 gets to lock rooms remotely")
        if args == "":
          if room.name in locks:
            room.message("It's already locked.. ;D")
            return
          locks.append(room.name)
          room.message("Locked: <b>%s</b>" % room.name, True)
          f = open("locks.txt", "w")
          f.write("\n".join(locks))
          f.close()
        if args not in self.roomnames:
          if args == "": return
          room.message("I haven't joined such room")

        ##unlock      
      if cmd == "unlock" and self.getAccess(user) >= 2:
        if user.name in blacklist: return
        if args in self.roomnames:
          if args in locks:
            if user.name in owners or user.name in admin:
              locks.remove(args)
              room.message("Unlocked: <b>%s</b> :D" % args, True)
              f = open("locks.txt", "w")
              f.write("\n".join(locks))
              f.close()
            else: room.message("")
          else:
            room.message("It's not even locked.. ;D")
            return
        if args == "":
          if room.name in locks:
            locks.remove(room.name)
            room.message("Unlocked: <b>%s</b> :D" % room.name, True)
            f = open("locks.txt", "w")
            f.write("\n".join(locks))
            f.close()
          else:
            room.message("It's not even locked.. ;D")
            return
        if args not in self.roomnames:
          if args == "": return
          room.message("I'm not in that room.. :P")
          return


    ##### Whitelist
      elif cmd == "wl":
        name = args
        name = getUname(room, name)
        if name not in whitelist and name not in archwizard and name not in player and name not in owners and name not in admin and name not in archknight and name not in blacklist:
          room.message(""+args+" ketik <cmds ;) ")
          whitelist.append(name)
          f = open("whitelist.txt","w")
          f.write("\n".join(whitelist))
          f.close
        else:
          room.message("User tersebut sudah terdaftar")

          ###blacklist
      elif cmd == "bl" and self.getAccess(user) >= 4:
        name = args
        if name not in whitelist and name not in owners and name not in admin and name not in archknight:
          room.message("Done")
          blacklist.append(name)
          f = open("blacklist.txt","w")
          f.write("\n".join(blacklist))
          f.close
        else:
          room.message("User tersebut sudah di blacklist")

      #blist
      if cmd == "blacklist" and self.getAccess(user) >= 6:
        room.message("<br/>Blacklisted User : <b> %s" % (", ".join(blacklist), ), True)


      ##ubl
      if cmd == "ubl" and self.getAccess(user) >= 3:
        try:
          if args in blacklist:
            blacklist.remove(args)
            f = open("blacklist.txt","w")
            f.write("\n".join(blacklist))
            f.close()
            room.message("Sukses")
        except:
          room.message("Gagal")
            
      ##uwl
      if cmd == "uwl" and self.getAccess(user) >= 5:
        try:
          if args in owners:
            room.message("Ma'af Vina tidak bisa melakukan itu")
          if args in admin:
            admin.remove(args)
            f = open("admin.txt","w")
            f.write("\n".join(admin))
            f.close()
            room.message("Sukses")
          if args in archwizard:
            archwizard.remove(args)
            f = open("archwizard.txt","w")
            f.write("\n".join(archwizard))
            f.close()
            room.message("Sukses")
          if args in archknight:
            archknight.remove(args)
            f = open("archknight.txt","w")
            f.write("\n".join(archknight))
            f.close()
            room.message("Sukses")
          if args in archwizard:
            archwizard.remove(args)
            f = open("archwizard.txt","w")
            f.write("\n".join(archwizard))
            f.close()
            room.message("Sukses")
          if args in player:
            player.remove(args)
            f = open("player.txt","w")
            f.write("\n".join(player))
            f.close()
            room.message("Sukses")
          if args in whitelist:
            whitelist.remove(args)
            f = open("whitelist.txt","w")
            f.write("\n".join(whitelist))
            f.close()
            room.message("Sukses")  
        except:
          room.message("Gagal")
        
      if cmd== "sbg":
            if self.getAccess(user) >= 5:
              if len(args) > 0:
                  if args == "on":
                    room.setBgMode(1)
                    room.message("Background On")
                    return
                  if args == "off":
                    room.setBgMode(0)
                    room.message("Background Off")
      if cmd== "sf":
            if self.getAccess(user) >= 1:
                  if args:
                    self.setFontFace(args)
                    room.message("Done")

      if cmd== "sfc":
            if self.getAccess(user) >= 1:
                  if args:
                    self.setFontColor(args)
                    room.message("Done")
                    
      if cmd== "sfz":
            if self.getAccess(user) >= 1:
                  if args:
                    self.setFontSize(int(args))
                    room.message("Done")

      if cmd== "snc":
            if self.getAccess(user) >= 1:
                  if args:
                    self.setNameColor(args)
                    room.message("Done")
      elif cmd == "mydict" or cmd == "mydf":
          arr = []
          for i in dictionary:
            if user.name in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("You have defined <b>"+str(len(arr))+"</b> words in your dictionary :<i> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message("kamu tidak memiliki dictionary.")
      if cmd == "tracker":
       try:
        if args:          
         room.message(code(args), True)
             
        else:
         room.message(code(user.name), True)
             
       except:
         room.message("Not found.. :)")

      if cmd == "ping":
        if room.name not in locks:
          args == room.name
          if args == "":
            usrs = []
            gay = []
            finale = []
            prop = 0
            prop = prop + len(room._userlist) - 1
            for i in room._userlist:
              i = str(i)
              usrs.append(i)
            while prop >= 0:
              j = usrs[prop].replace("<User: ", "")
              i = j.replace(">", "")
              gay.append(i)
              prop = prop - 1
            for i in gay:
              if i not in finale:
                finale.append(i)
            if len(finale) > 40:
              room.message("@%s"% (" @".join(finale[:41])), True)
                
            if len(finale) <=40 :
              room.message("@%s"% (" @".join(finale)), True)
                
          if args != "":
             if args not in self.roomnames:
               room.message("I'm not there.")

      if cmd == "udf" and len(args) > 0:
          try:
            word = args
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if name == user.name or self.getAccess(user) >= 5:
                del dictionary[word]
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message(args+" has been removed from Definition database")
                return
              else:
                room.message("<b>%s</b> you can not remove this define only masters or the person who defined the word may remove definitions" % user.name, True)
                return
            else:
               room.message("<b>%s</b> is not yet defined you can define it by typing <b>define %s: meaning</b>" % args, True)
          except:
            room.message("Gagal")
            return
            
      elif cmd == "seedf" or cmd == "seedict":
        if room.name not in locks:
          if not args:
            room.message("Whose dict do you want to see ?")
            return
          args = args.lower()
          if pars(args) == None:
            args = args.lower()
          if pars(args) != None:
            args = pars(args)
          arr = []
          for i in dictionary:
            if args in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<b>"+args.title()+"</b> have defined <b>"+str(len(arr))+"</b> words in his dictionary :<i> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message(args.title()+" defined nothing.")

      if cmd == "seenick":
            try:
              if args in nicks:
                room.message(args+" Nick Dia : "+sntonick(args)+"", True)
              else:
                room.message(args+" Belum membuat nick di aku :|")
            except:
              return      

      elif cmd=="prof" or cmd == "profile":
          try:
            args=args.lower()
            stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
            crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
            age, crap = age.split('<br /></span>', 1)
            crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
            gender, crap = gender.split(' <br /></span>', 1)
            if gender == 'M':
                gender = 'Male'
            elif gender == 'F':
                gender = 'Female'
            else:
                gender = '?'
            crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
            location, crap = location.split(' <br /></span>', 1)
            crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
            mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
            mini=mini.replace("<img","<!")
            picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
            prodata = '<br/> <a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture + '<br/><br/> Age: '+ age + ' <br/> Gender: ' + gender +  ' <br/> Location: ' +  location + '' '<br/> <a href="http://' + args + '.chatango.com" target="_blank"><u>Chat With User</u></a> ' "<br/><br/> "+ mini 
            room.message(prodata.replace("\n","<br/>"),True)
          except:
            room.message(""+args+" doesn't exist o.o ")
      elif cmd=="mini":
        try:
          args=args.lower()
          stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
          crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
          mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
          mini=mini.replace("<img","<!")
          prodata = '<br/>'+mini
          room.message(prodata,True)
        except:
          room.message(""+args+" doesn't exist o.o ")

      if cmd == "bgimg":
        try:
          args=args.lower()
          picture = '<a href="http://st.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg</a>'
          prodata = '<br/>'+picture
          room.message("<br/>"+"User ID : "+args+"<br/>Background :"+prodata,True)
        except:
          room.message(""+args+" doesn't exist o.o ")

   

    ### Private Messages
      elif cmd=="pm":
        data = args.split(" ", 1)
        if len(data) > 1:
          name , args = data[0], data[1]
          self.pm.message(ch.User(name), "[Private.Message] By - "+user.name+" : "+args+" ")
          room.message("Sent to "+name+"")
    ### Sentnote
      elif cmd == "inbox":
          if user.name in sn:
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] messages in your inbox. To read it, do irn")
          else:
            sn.update({user.name:[]})
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] messages in your inbox. To read it, do irn")


        #send notes
      elif cmd == "sn" or cmd == "sendnote":
          args.lower()
          untuk, pesan = args.split(" ", 1)
          if untuk[0] == "+":
                  untuk = untuk[1:]
          else:
                  if pars(untuk) == None:
                    room.message("Who is "+untuk+" ?? if user not in this room please add + before username")
                    return
                  untuk = pars(untuk)
          if untuk in sn:
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          else:
            sn.update({untuk:[]})
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          room.message('Sent to %s'% (untuk)+"'s inbox" , True)
				


        #Read Notes
      elif cmd =="rn" or cmd =="readnote":
          if user.name not in sn:
            sn.update({user.name:[]})
          user=user.name.lower()
          if len(sn[user]) > 0:
            messg = sn[user][0]
            dari, pesen, timey = messg
            timey = time.time() - int(timey)
            minute = 60
            hour = minute * 60
            day = hour * 24
            days =  int(timey / day)
            hours = int((timey % day) / hour)
            minutes = int((timey % hour) / minute)
            seconds = int(timey % minute)
            string = ""
            if days > 0:
              string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
            if len(string) > 0 or hours > 0:
              string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
            if len(string) > 0 or minutes > 0:
              string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
            string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
            room.message("[<font color='#6699CC'><b>Private Message</b></font>] from - "+sntonick(dari)+" : "+pesen+"  (<font color='#9999FF'>"+string+" ago </font>)", True)
            try:
              del sn[user][0]
              notif.remove(user)
            except:pass
          else:room.message('%s'%(user)+" you don't have any messages in your inbox" , True)
   ###### leave + room 
      elif cmd == "leave"  and self.getAccess (user) >= 4:
        if not args:args=room.name
        room.message("Baik aku out "+args+" ...")
        self.leaveRoom(args)
        print("[SAVE] SAVING Rooms...")
        f = open("rooms.txt", "w")
        f.write("\n".join(self.roomnames))
        f.close()

    ###### join room + roomname

      if cmd == "join" and len(args) > 1:
          if self.getAccess (user) >= 4:
              if args not in self.roomnames:
                room.message("Baik aku join ke "+args+" ...")
                self.joinRoom(args)
              else:
                room.message("aku sudah ada disana ...")
              print("[SAVE] SAVING Rooms...")
              f = open("rooms.txt", "w")
              f.write("\n".join(self.roomnames))
              f.close()
      elif cmd == "userlist" or cmd == "ul":
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> users in this room: %s"% (len(finale), ", ".join(finale[:41])), True)
          if len(finale) <=40 :
            room.message("Current <b>%s</b> users of this room: %s"% (len(finale),", ".join(finale)), True)
         if args != "":
           if args not in self.roomnames:
             room.message("I'm not there.")
             return
           users = getParticipant(str(args))
           if len(users) > 40:
             room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> current users in <b>%s</b>: %s"% (len(users), args.title(), ", ".join(users[:41])), True)
           if len(users) <=40:
             room.message("Current <b>%s</b> users in <b>%s</b>: %s"% (len(users), args.title(), ", ".join(users)), True) 
    ##### bot rooms
      elif cmd == "rooms" : 
        j = [] 
        for i in self.roomnames: 
          j.append(i+'[%s]' % str(self.getRoom(i).usercount)) 
          j.sort() 
        room.message("aku bermain Di "+'[%s] rooms: '%(len(self.roomnames))+", ".join(j))
    ####nick
      elif cmd == "nick":
        ## if user.name in reg or user.name in friends or user.name in trusted or user.name in owners:
            if room.name not in locks:
              if args:
                  nick = args 
                  user = user.name 
                  nicks[user] = json.dumps(nick)
                  room.message(user +' Oke, mulai sekarang aku panggil '+str(args)+'', True)
                  try: 
                      print("[SAVING] NICKS...")
                      f = open("nicks.txt", "w")
                      for user in nicks:
                          nick = json.loads(nicks[user])
                          f.write(json.dumps([user,nick]) + "\n")
                  except:
                         room.message("Gagal membuat Nick baru..");return
              else:
                room.message('Ketik >nick <spasi> nama yang di inginkan', True)

    
    ##mynick
      elif cmd == "mynick" :
          user=user.name.lower()
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message(user+" is nicked : "+nick,True)
          else:
            room.message("buat nick dulu yah?! :D ", True)


   except Exception as e:
      try:
        et, ev, tb = sys.exc_info()
        lineno = tb.tb_lineno
        fn = tb.tb_frame.f_code.co_filename
        room.message("[Expectation Failed] %s Line %i - %s"% (fn, lineno, str(e)))
        return
      except:
        room.message("Undescribeable error detected !!")
        return


  ##Other Crap here, Dont worry about it
  
  def onFloodWarning(self, room):
    room.reconnect()
  
  def onJoin(self, room, user, puid=None):
   print(user.name + " joined the chat!")
   if room.name == "vina-chat":
     room.message("Selamat datang di vina-chat @"+user.name+" :D")
  
  def onLeave(self, room, user, puid=None):
   print(user.name + " left the chat!")
  
  
def getUname(room, uname):
    # [x.name for x in room._userlist if "pero" in x.name]
    uname = uname.lower()
    for un in room._userlist:
        if uname in un.name.lower(): return un.name
    return uname


if __name__ == "__main__":
  TestBot.easy_start(rooms, botname, botpass)
