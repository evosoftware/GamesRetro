#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os,sys,re,urllib,urllib2,mechanize,time,ntpath,zipfile,gzip,cookielib,subprocess

help = '''
        Entre com um emulador suportado:

        Windows :		
	        Snes9K
                Snes9x
	        zsnesw
		Kega_Fusion
		Gens
	        Genesis
	        snes9x2010			
	        ppsspp		
		
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

Snes9x = dir + '/emuladores/SNES9x/snes9x.exe'
zsnesw = dir + '/emuladores/zsnesw/zsnesw.exe'
Snes9K = dir + '/emuladores/snes9k009z/Snes9K.exe'
Fusion = dir + '/emuladores/Fusion364/Fusion.exe'
Gens = dir + '/emuladores/gens2.14/gens.exe'
retroarch = dir + '/emuladores/RetroArch/retroarch.exe'

def console():
    emulador = raw_input('\nDigite o nome do emulador que deseja jogar: ')
    return emulador

def set_emulador(emulador):
	
    if not emulador:
        print '\nEmulador não definido,para prosseguir defina um emulador...'
        start()
		
    if emulador:

        if emulador == 'Snes9x EX+ (Android)':
            emulator = 'super-nintendo'
            return emulator
			
        elif emulador == 'SuperRetro16 (Android)':
            emulator = 'super-nintendo'	
            return emulator
		
        elif emulador == 'zsnesw':
            emulator = 'super-nintendo'
            return emulator
		
        elif emulador == 'Snes9x':
            emulator = 'super-nintendo'
            return emulator
		
        elif emulador == 'Snes9K':
            emulator = 'super-nintendo'
            return emulator
			
        elif emulador == 'Kega_Fusion':
            emulator = 'sega-genesis'
            return emulator
			
        elif emulador == 'Gens':
            emulator = 'sega-genesis'
            return emulator
		    
        elif emulador == 'MD.emu (Android)':
            emulator = 'sega-genesis'
            return emulator
			
        elif emulador == 'GBA.emu (Android)':
            emulator = 'gameboy-advance'	
            return emulator
			
        elif emulador == 'PPSSPP (Android)':
            emulator = 'playstation-2'
            return emulator
			
        elif emulador == 'ePSXe (Android)':
            emulator = 'playstation'
            return emulator
			
        elif emulador == 'Genesis':
            emulator = 'sega-genesis'
            return emulator
			
        elif emulador == 'snes9x2010':
            emulator = 'super-nintendo'
            return emulator
			
        elif emulador == 'ppsspp':
            emulator = 'playstation-2'			
            return emulator
			
        else:
            print '\nEmulador não reconhecido,para prosseguir defina um emulador válido!!!'
            start()		
    
def get_html(url):
	req = urllib2.Request(url)
	req.add_header('Referer', server)	
	response = urllib2.urlopen(req)
	html = response.read()
	response.close()
	return html

def browser(link,dest,url_rom):
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
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'),('Referer', url_rom)]
    br.retrieve(link,dest)
    progress(10)	
    print 'Download realizado com sucesso !!!'	
	
def download(url,dest,url_rom,dp=None):
    if not dp:
    	dp = 'GamesRetro,Baixando e copiando arquivos...'
    time.sleep(2)
    #urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
    browser(url,dest,url_rom)	
	
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
	    #print str(e); return False
	    if e:
	        print '\nArquivo corrompido,impossível extrair rom,voltando ao menu pincipal...'
	        time.sleep(2)
	        start()			
    return True
	
def allWithProgress(_in,_out,dp):
    zin=zipfile.ZipFile(_in,'r'); nFiles=float(len(zin.infolist())); count=0
    try:
        for item in zin.infolist(): count+=1; update=count / nFiles * 100; dp.update(int(update)); zin.extract(item,_out)
    except Exception, e:
	    print str(e); return False
    return True    

def play_game(lib,emulador):
    rom = lib
    #print rom
    if emulador == '':
        sys.exit()
    if emulador == 'Snes9x EX+ (Android)':
        link = os.system('am start --user 0 -n com.explusalpha.Snes9xPlus/com.imagine.BaseActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit()		
    elif emulador == 'SuperRetro16 (Android)':
        #link = os.system('am start --user 0 -n com.bubblezapgames.supergnes_lite/.SuperGNES -a android.intent.action.VIEW -d "'+rom+'"')
        link = os.system('am start --user 0 -n com.bubblezapgames.supergnes_lite/.Splash -a android.intent.action.VIEW -d "'+rom+'"')		
        sys.exit()
    elif emulador == 'MD.emu (Android)':
        link = os.system('am start --user 0 -n com.explusalpha.MdEmu/com.imagine.BaseActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit()
    elif emulador == 'RetroArch (Android)':
        #link = os.system('adb shell & su root am start -n  -a android.intent.action.VIEW -d "'+rom+'"')
        link = os.system('am start --user 0 -n  -a android.intent.action.VIEW -d "'+rom+'"')		
        sys.exit()
    elif emulador == 'PPSSPP (Android)':
        link = os.system('am start --user 0 -n org.ppsspp.ppsspp/.PpssppActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit()
    elif emulador == 'ePSXe (Android)':
        link = os.system('start --user 0 -n com.epsxe.ePSXe/.ePSXe -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e com.epsxe.ePSXe.isoName "'+rom+'"')
        sys.exit()
    elif emulador == 'GBA.emu (Android)':
        link = os.system('am start --user 0 -n com.explusalpha.GbaEmu/com.imagine.BaseActivity -a android.intent.action.VIEW -d "'+rom+'"')
        sys.exit()		
    elif emulador == 'Snes9x':
        link = subprocess.call([Snes9x, '-f', '%s' % rom]) == 0	
        sys.exit(0)
    elif emulador == 'Snes9K':
        link = subprocess.call([Snes9K, '-ml', '%s' % rom]) == 0
        sys.exit(0)
    elif emulador == 'Kega_Fusion':
        link = subprocess.call([Fusion, '-f', '-ml', '-mc', '%s' % rom]) == 0
        sys.exit(0)
    elif emulador == 'Gens':
        link = subprocess.call([Gens, '%s' % rom]) == 0
        sys.exit(0)
    elif emulador == 'Genesis':
        retroarch_core =  dir + '/emuladores/RetroArch/cores/genesis_plus_gx_libretro.dll'	
        link = subprocess.call([retroarch, '-f', '-D', '-L', retroarch_core, '%s' % rom])
        sys.exit(0)
    elif emulador == 'snes9x2010':
        retroarch_core =  dir + '/emuladores/RetroArch/cores/snes9x2010_libretro.dll'	
        link = subprocess.call([retroarch, '-f', '-D', '-L', retroarch_core, '%s' % rom])
        sys.exit(0)
    elif emulador == 'ppsspp':
        retroarch_core =  dir + '/emuladores/RetroArch/cores/ppsspp_libretro.dll'	
        link = subprocess.call([retroarch, '-f', '-D', '-L', retroarch_core, '%s' % rom])
        sys.exit(0)		
    else:
        link = subprocess.call([zsnesw, '-f', '%s' % rom]) == 0
        sys.exit(0)		

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

def load_start(emulador):
    url = raw_input('\nCopie e cole aqui o link do jogo: ')
    #url_rom = (server + 'download/' + url + '#captcha')
    url_rom = (server + 'download-amp/' + url)	
    print url_rom
    codigo_fonte = get_html(server + 'download-amp/' + url)	
    #codigo_fonte = get_html(server + 'download/' + url + '#captcha')	
    match = re.compile(r'<a class=".*?" href="(.*?)"><i class=".*?"></i>.*?</a>').findall(codigo_fonte)
    #match = re.compile(r"var url = '(.*?)';").findall(codigo_fonte)
    #match = re.compile(r'<small>.*? <a href="(.*?)">Click here</a>.*?</small>').findall(codigo_fonte)
    for i in match:
        link = i.encode('utf-8')
        print link
        a = link.split('?id=')
        b = a[0]
        #print b		
        rom_name = ntpath.basename(urllib.unquote(b))		
        lib = os.path.join(dir,rom_name)		
        download(link,lib,url_rom)		
        print '\n'; print '================================================'; print 'Extraindo em : ' + dir; print '================================================'		
        all(lib,dir)
        progress(10)
        print 'Extraído com sucesso !!!'
        progress(10)
        print 'Abrindo Emulador ' + emulador + ' !!!'		
        play_game(lib,emulador)

def list_roms(emulator,emulador):
    try:
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
        load_start(emulador)
    except:
        pass
        question = raw_input('\nBuscar por jogos novamente, Y ou N ??? ')
        if question.upper() == 'Y':
            query_rom(emulator,emulador)
            start()			
        if question.upper() == 'N':
            start()
        else:
            print 'Comando inválido,tente novamente!!!'
            print '\nSaindo...'
            sys.exit()			
    #query_rom(emulator,emulador)		

def query_rom(emulator,emulador):
    try:
        name_rom = raw_input('\nDigite o nome do jogo: ')
        #print(server + 'roms/' + emulator + '/?q=' + urllib.quote(name_rom))
        codigo_fonte = get_html(server + 'roms/' + emulator + '/?q=' + urllib.quote(name_rom))
        match = re.compile(r'<a href=".*?/download/(.*?)"><span class=".*?"></span> <span>(.*?)</span>').findall(codigo_fonte)			
        for i, e in match:
            title = e.encode('utf-8')
            print '\nTITULO: ' + title	
            link = i.encode('utf-8')
            print 'LINK: ' + link
        if link:
            load_start(emulador)
    except:
        pass
        question = raw_input('\nBuscar por jogos novamente, Y ou N ??? ')
        if question.upper() == 'Y':
            query_rom(emulator,emulador)
        if question.upper() == 'N':
            start()
        else:
            print 'Comando inválido,tente novamente!!!'
            print '\nSaindo...'
            sys.exit()			
    #query_rom(emulator,emulador)		

def start():
    emulador = console()
    print emulador
    emulator = set_emulador(emulador)
    print emulator
    action = raw_input('\nDigite 1 para buscar jogos de A-Z ou 2 para buscar um jogo pelo nome: ')
    if action == '1':
        list_roms(emulator,emulador)
    elif action == '2':		
        query_rom(emulator,emulador)
    elif action == 'sair' or action == 'Sair' or action == 'SAIR':	
        print '\nSaindo...'
        time.sleep(2)		
        sys.exit(0)        		
    else:
        print 'Comando inválido,tente novamente!!!'

if __name__ == '__main__':
	start()	