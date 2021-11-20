# -------------
#| Brew Console
#| By buu#1662
# -------------

#| Import Modules
#| fun stuff

import time
import os
import requests
from requests import get
import colorama
import webbrowser as wb
import random

#| Variables
#| good

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

#| Defining FUnctions
#| very nice

def cprint(string):
    print(yellow + "[:] " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    [:] " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "[#] " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    [#] " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "[?] " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    [?] " + normal + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "[!] " + normal + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    [!] " + normal + string)
# ---------------------------------------------
def wprint(string):
    time.sleep(.02)
    print(yellow + "" + normal + string)
# ---------------------------------------------
def swprint(string):
    time.sleep(.02)
    print(yellow + "    [:] " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)


#| Source Code
#| 100% amazing

version = "v1.00"
dailymessage = ["you are cool",
                "omg hacker! stop it right now!",
                "john doe in real life",
                "i forgot how to program",
                "program = hack 100%",
                "anonymous simps are crazy",
                "100% daily messages, right??",
                "do you simp for me senpai",
                "goku >>> everything",
                "tiktok = worst social media",
                "if you support trump your 100% homophobe (jk)",
                "i wasted my time on these",
                "i made this at 8:28pm lmao",
                "roblox.com/home",
                "pls go to github.com/xbuu",
                "secret github?? | github.com/buuinstalls (felt cute might delete later)",
                "how to speak english 2021 tutorial working no clickbait",
                "how to obfuscate python?! (2021 working)",
                "jjsploit premium with no bitcoin miner > synapse x",
                "among us sussy baka",
                "i literally used fancy text pro for the big (brew) logo",
                "if you see this, this is literally the last message on the table"]

#| Intro
#| very nice bro

os.system("cls")
print(red + f"""         
    █▄▄ █▀█ █▀▀ █░█░█
    █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
    {random.choices(dailymessage)}
    {normal}type "help" or "cmds" for commands
    {normal}type "tutorial" for a tutorial
""")

#| Console Function
#| what are u doing here

def doesfilexist(filePathAndName):
    return os.path.exists(filePathAndName)

if doesfilexist("username.txt"):
    pass
elif doesfilexist("password.txt"):
    pass
else:
    username = input("Username : ")
    usernamew = open("username.txt", "w")
    usernamew.write(username)
    password = input("Password : ")
    passwordw = open("password.txt", "w")
    passwordw.write(password)

def console():
    cmdinput = input("> ")

    # command table

    utilitycmds = ["reload", "compare"]
    funcmds = ["darkweb"]
    cmds = ["findip","checkip", "myip"]

    getvar = "g/"

    # commands

    if cmdinput.lower() == "cmds" or cmdinput.lower() == "help":
        os.system("cls")
        print(red + f"""         
            █▄▄ █▀█ █▀▀ █░█░█
            █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
            {random.choices(dailymessage)}
            Listing the commands;
            {normal}
        """)
        print(f"""
        {getvar} = {green}get/{normal}[{cyan}argument{normal}]
        ------------------------------------
        {green}{getvar}{normal}{cyan}soulshitters        {normal}
        {green}{getvar}{normal}{cyan}brewscript          {normal}
        {green}{getvar}{normal}{cyan}robloxnetless          {normal}
        ------------------------------------
        {red}{cmds[0]}{normal}: Find an IP Location.
        {red}{cmds[1]}{normal}: Give info on a website/ip
        {red}{cmds[2]}{normal}: If you don't know what your IP is..?
        ------------------------------------
        {red}{funcmds[0]}{normal}: prank ur friends
        ------------------------------------
        {red}{utilitycmds[0]}{normal}: reloads the program
        {red}{utilitycmds[1]}{normal}: compare texts lol
        """)
        console()
    elif cmdinput.lower() == "tutorial":
        wb.open("https://blxy.gitbook.io/soulshatters/")
        console()
    elif cmdinput.lower() == cmds[0]:
        os.system("cls")
        print(red + f"""         
    █▄▄ █▀█ █▀▀ █░█░█
    █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
    {random.choices(dailymessage)}
    {normal}Type in the ip or type "cancel" to end
            """)
        ip = input("> ")
        if ip.lower() == "cancel":
            print("-------------------")
            console()
        else:
            response = requests.get("http://ip-api.com/json/" + ip).json()
            print("[-------------------]")
            print(response["query"])
            print(response["status"])
            print("-------------------")
            print(response["country"])
            print(response["regionName"])
            print(response["city"])
            print(response["timezone"])
            print("-------------------")
            print(response["isp"])
            print(response["org"])
            print(response["as"])
            print("[-------------------]")
            console()
    elif cmdinput.lower() == cmds[1]:
        os.system("cls")
        print(red + f"""         
        █▄▄ █▀█ █▀▀ █░█░█
        █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
        {random.choices(dailymessage)}
        {normal}Type in the ip or website "cancel" to end
                """)
        ip = input("> ")
        if ip == "cancel":
            print(red + f"""         
    █▄▄ █▀█ █▀▀ █░█░█
    █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
    {random.choices(dailymessage)}
            """)
            console()
        else:
            os.system(f"ping {ip} -a")
        console()
    elif cmdinput.lower() == cmds[2]:
        ip = get('https://api64.ipify.org?format=jsonp&callback=getip').text
        print('Public IP Address > ' + green + "{}".format(ip))
        print(f'{normal}')
        console()
    elif cmdinput.lower() == utilitycmds[0]:
        os.system("cls")
        print(red + f"""         
    █▄▄ █▀█ █▀▀ █░█░█
    █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
    {random.choices(dailymessage)}
    {normal}type "help" or "cmds" for commands
        """)
        console()
    elif cmdinput.lower() == utilitycmds[1]:
        os.system("cls")
        print(red + f"""         
        █▄▄ █▀█ █▀▀ █░█░█
        █▄█ █▀▄ ██▄ ▀▄▀▄▀ {version}
        {random.choices(dailymessage)}
        {normal}Type in your text
            """)
        txt1 = input("txt1 > ")
        txt2 = input("txt2 > ")
        if txt1 == txt2:
            print(green + "Messages are the same" + normal)
        else:
            print(red + "Messages aren't the same" + normal)
        console()
    elif cmdinput.lower() == funcmds[0]:
        os.system("cls")

        print(red + '''
    █▀▄ ▄▀█ █▀█ █▄▀ █▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█
    █▄▀ █▀█ █▀▄ █░█ ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█
    scare your friends ;)
        ''')

        firstname = input("Enter First Name : ")
        lastname = input("Enter Last Name : ")

        os.system("cls")

        print(red + '''

    █▀▄ ▄▀█ █▀█ █▄▀ █▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█
    █▄▀ █▀█ █▀▄ █░█ ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█

        ''')
        cinfo("We've searched around.")
        lastnames = ["Hutchinson", "Mejia", "Lambert", "Gonzalez", "Davis", "Mcgrath", "Valentine", "Mosley", "Rivers",
                     "Summers", "Leonard", "Benton", "Dominguez", "Henson", "Rivas", "Griffin", "Cohen", "Espinoza",
                     "Dillon", "Walton", "Clark", "Lucas", "Byrd", "Frank", "Shannon", "Leblanc", "Cox", "Rivas",
                     "Villarreal", "Reese", "Kirk", "Guerrero", "Hester", "Tanner", "Reilly", "Clayton"]
        wait(.9)
        cinfo("Displaying people found.")
        wait(.5)
        cinfo("Currently Up-to-date since November, 18th, 2021 | 9/18/21")
        time.sleep(1)
        print(f"{firstname}, ['{lastname}'] found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        wprint(f"{firstname}, {random.choices(lastnames)} found")
        time.sleep(2)
        console()
    elif cmdinput.lower() == getvar + "soulshatters":
        wb.open("https://discord.gg/STNfzkDXQC")
        console()
    elif cmdinput.lower() == getvar + "robloxnetless":
        wb.open("https://blxy.gitbook.io/netless/")
        console()
    elif cmdinput.lower() == "g/":
        cerror("Error: [2]")
        scerror("Arguments not specified.")
        console()
    else:
        cerror("Error: [1]")
        scerror("Command not found.")
        console()

#| last function
#| bruh

console()