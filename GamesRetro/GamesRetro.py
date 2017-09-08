#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,re,requests,urllib,urllib2,mechanize,time,ntpath,zipfile,gzip,cookielib,subprocess

help = '''Entre com um emulador suportado:

    Windows :
	    Snes9K
            Snes9x
	    zsnesw
    Android :
	    Snes9x EX+ (Android)
	    SuperRetro16 (Android)
	    MD.emu (Android)
	    PPSSPP (Android)
	    ePSXe (Android)
	'''

print '\n' + help

dir = os.getcwd()

server = 'https://www.loveroms.com/'

emulador = raw_input('\nDigite o nome do emulador que deseja jogar: ')
    
Snes9x = dir + '/emuladores/SNES9x/snes9x.exe'
zsnesw = dir + '/emuladores/zsnesw/zsnesw.exe'
Snes9K = dir + '/emuladores/snes9k009z/Snes9K.exe'

if emulador == '':
    print '\nEmulador não definido,para prosseguir defina um emulador'
    sys.exit()

elif emulador == 'Snes9x EX+ (Android)':
    emulator = 'super-nintendo'

elif emulador == 'SuperRetro16 (Android)':
    emulator = 'super-nintendo'	

elif emulador == 'zsnesw':
    emulator = 'super-nintendo'

elif emulador == 'Snes9x':
    emulator = 'super-nintendo'

elif emulador == 'Snes9K':
    emulator = 'super-nintendo'
    
elif emulador == 'MD.emu (Android)':
    emulator = 'sega-genesis'
	
elif emulador == 'PPSSPP (Android)':
    emulator = 'playstation-2'
	
elif emulador == 'ePSXe (Android)':
    emulator = 'playstation'

else:
    print '\nEmulador não reconhecido,para prosseguir defina um emulador válido!!!'
    sys.exit()	
    
def get_html(url):
	req = urllib2.Request(url)
	#req.add_header('referer', server)
	req.add_header('User-Agent', 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')	
	response = urllib2.urlopen(req)
	html = response.read()
	#print html
	response.close()
	return html

def browser(link,dest,dp):
    print '\n'; print '========================================================='; print 'Efetuando download em : ' + dir; print '========================================================='
    time.sleep(1)	
    br = mechanize.Browser()
    time.sleep(1)
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)	
    br.set_handle_equiv(True)
    br.set_handle_gzip(False)
    br.set_handle_redirect(True)	
    br.set_handle_referer(True)	
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),('Referer', server)]
    f = br.retrieve(link,dest)
    progress(10)	
    print 'Download realizado com sucesso !!!'	
	
def download(url,dest,dp=None):
    if not dp:
    	dp = 'GamesRetro,Downloading & Copying File'
    time.sleep(2)
    #urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
    browser(url,dest,dp)	
	
def _pbhook(numblocks,blocksize,filesize,url,dp):
    try:
	    percent=min((numblocks*blocksize*100)/filesize, 100); dp.update(percent)
    except:
	    percent=100; dp.update(percent)
    if dp.iscanceled():
	    raise Exception("Canceled"); dp.close()

def all(_in,_out,dp=None):
	if dp:
	    return allWithProgress(_in, _out, dp)
	return allNoProgress(_in, _out)
	
def allNoProgress(_in,_out):
    try:
	    zin=zipfile.ZipFile(_in,'r'); zin.extractall(_out)
    except Exception, e:
	    print str(e); return False
    return True
	
def allWithProgress(_in,_out,dp):
    zin=zipfile.ZipFile(_in,'r'); nFiles=float(len(zin.infolist())); count=0
    try:
        for item in zin.infolist(): count+=1; update=count / nFiles * 100; dp.update(int(update)); zin.extract(item,_out)
    except Exception, e:
	    print str(e); return False
    return True    

def play_game(url):
    rom = url
    #print rom
    if emulador == '':
        sys.exit(0)
    if emulador == 'Snes9x EX+ (Android)':
        link = os.system('am start --user 0 -n com.explusalpha.Snes9xPlus/com.imagine.BaseActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit(0)		
    elif emulador == 'SuperRetro16 (Android)':
        #link = os.system('am start --user 0 -n com.bubblezapgames.supergnes_lite/.SuperGNES -a android.intent.action.VIEW -d "'+rom+'"')
        link = os.system('am start --user 0 -n com.bubblezapgames.supergnes_lite/.Splash -a android.intent.action.VIEW -d "'+rom+'"')		
        sys.exit(0)
    elif emulador == 'MD.emu (Android)':
        link = os.system('am start --user 0 -n com.explusalpha.MdEmu/com.imagine.BaseActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit(0)
    elif emulador == 'RetroArch (Android)':
        #link = os.system('adb shell & su root am start -n  -a android.intent.action.VIEW -d "'+rom+'"')
        link = os.system('am start --user 0 -n  -a android.intent.action.VIEW -d "'+rom+'"')		
        sys.exit(0)
    elif emulador == 'PPSSPP (Android)':
        link = os.system('am start --user 0 -n org.ppsspp.ppsspp/.PpssppActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit(0)
    elif emulador == 'ePSXe (Android)':
        link = os.system('start --user 0 -n com.epsxe.ePSXe/.ePSXe -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e com.epsxe.ePSXe.isoName "'+rom+'"')
        sys.exit(0)		
    elif emulador == 'Snes9x':
        link = subprocess.call([Snes9x, '-f', '%s' % rom]) == 0	
        sys.exit(0)
    elif emulador == 'Snes9K':
        link = subprocess.call([Snes9K, '-ml', '%s' % rom]) == 0
        sys.exit(0)		
    else:
        link = subprocess.call([zsnesw, '-f', '%s' % rom]) == 0

def progress(seconds):
    print '\nLoading....  ',
    sys.stdout.flush() 
    i = 0 
    while i <= seconds:
        if (i%4) == 0:
            sys.stdout.write('\b/')
        elif (i%4) == 1:
            sys.stdout.write('\b-')
        elif (i%4) == 2:
            sys.stdout.write('\b\\')
        elif (i%4) == 3:
            sys.stdout.write('\b|')			
        sys.stdout.flush()
        time.sleep(0.2)
        i+=1
    #print '\b\b done!'

def load_start():
    url = raw_input('\nCopie e cole aqui o link do jogo: ')    
    codigo_fonte = get_html(server + 'download-amp/' + url)
    match = re.compile(r'<a class=".*?" href="(.*?)"><i class=".*?"></i>.*?</a>').findall(codigo_fonte)
    for i in match:
        link = i.encode('utf-8')
        #print link
        #print ntpath.basename(urllib.unquote(link))
        rom_name = ntpath.basename(urllib.unquote(link))		
        lib = os.path.join(dir,rom_name)		
        download(link,lib)		
        print '\n'; print '================================================'; print 'Extraindo em : ' + dir; print '================================================'		
        all(lib,dir)
        progress(10)
        print 'Extraido com sucesso !!!'
        play_game(lib)

def list_roms():
    print '\nJogos de A-Z'
    time.sleep(2)
    letter = raw_input('Digite uma letra de A-Z: ')
    codigo_fonte = get_html(server + 'roms/' + emulator + '/?letter=' + letter.upper())
    match = re.compile(r'<a href=".*?/download/(.*?)"><span class=".*?"></span> <span>(.*?)</span>').findall(codigo_fonte)
    for i, e in match:
        title = e.encode('utf-8')
        print '\nTITULO: ' + title	
        link = i.encode('utf-8')
        print 'LINK: ' + link
    load_start()		

def query_rom():
    name_rom = raw_input('\nDigite o nome do jogo: ')
    codigo_fonte = get_html(server + 'roms/' + emulator + '/?q=' + urllib.quote(name_rom))
    match = re.compile(r'<a href=".*?/download/(.*?)"><span class=".*?"></span> <span>(.*?)</span>').findall(codigo_fonte)
    for i, e in match:
        title = e.encode('utf-8')
        print '\nTITULO: ' + title	
        link = i.encode('utf-8')
        print 'LINK: ' + link
    load_start()		

if __name__ == '__main__':
    action = raw_input('\nDigite 1 para buscar jogos de A-Z ou 2 para buscar um jogo pelo nome: ')
    if action == '1':
        list_roms()
    elif action == '2':		
        query_rom()
    elif action == 'sair' or action == 'Sair' or action == 'SAIR':	
        print '\nSaindo...'
        time.sleep(2)		
        sys.exit(0)        		
    else:
        print 'Comando inválido,tente novamente!!!'		