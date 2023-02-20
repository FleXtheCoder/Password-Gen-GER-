import os

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init() 

banner = (Fore.MAGENTA + """
 
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░             ░    ░  ░         ░ 
                                                                 ░                                   
""" + Fore.LIGHTCYAN_EX)
print(banner)
from ast import Delete
import random #importiert die libary "random"

import time #importiert die libary "time"

#liste der großen Buchstaben  
big_letters = ("A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

#liste der kleinen Buchstaben
small_letters = ("a", "b", "c","b" ,"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

#liste der Zahlen
strings = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

#liste der Sonderzeichen
symbols = ("!","/", "?", ".", "_", "#", "%", "-","+","*")               

output  = str(big_letters), str(small_letters), str(symbols), str (strings)

# create random shuffles 
time.sleep(1)

print(Fore.LIGHTBLACK_EX + "Dein Passwort wird generiert...")
print('\n')


time.sleep(2)
print(Fore.MAGENTA + "[Dein Passwort:]" ,Fore.LIGHTCYAN_EX + random.choice(big_letters[0:26]), random.choice(small_letters[0:26]), random.choice(symbols[0:26]), random.choice(small_letters[0:26]), random.choice(small_letters[0:26]),random.choice(strings[0:26]), random.choice(big_letters[0:26]), random.choice(small_letters[0:26]), random.choice(symbols[0:26]), random.choice(small_letters[0:26]), random.choice(small_letters[0:26]),random.choice(strings[0:26]) )

#print(random.choice(big_letters[0:26]), random.choice(small_letters[0:26]), random.choice(symbols[0:26]), random.choice(small_letters[0:26]), random.choice(small_letters[0:26]),random.choice(strings[0:26]) )

#print(random.choice(big_letters[0:26]), random.choice(small_letters[0:26]), random.choice(symbols[0:26]), random.choice(small_letters[0:26]), random.choice(small_letters[0:26]),random.choice(strings[0:26]) )



print (Fore.LIGHTBLACK_EX )

#print the output 






for x in output:
    if x in range(0, 64):
        print(output)

   
   
time.sleep(2)    #wartet 3 ca. sekunden


print("Dein Passwort wurde generiert!")


print("Drücke eine beliebige Taste um zu quitten!")



os.system('pause >nul')

