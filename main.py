import discord
import sys
import importlib
from os import listdir
from os.path import isfile, join

def loadAll():
    sys.path.append("modules")
    onlyfiles = listdir('modules')
    for module in onlyfiles:
        if module != ".gitignore":
            modName = module.split(".")
            obj = __import__(modName[0])
            globals()[modName[0]] = obj
            log("Loaded module: " + modName[0])

    #Login with details from file
    details = open("login.txt", "r")
    logins = details.read().split(",")
    details.close()
    client= discord.Client()
    client.login(logins[0], logins[1])
    return client

# Runs command
def runCommand(commTbl, message):
    if (commTbl[0] in sys.modules):
        print("hey!")
        prog = sys.modules[commTbl[0]]
        prog.main(message, commTbl, client)
    elif (commTbl[0] == "help"):
        if (commTbl[1] in sys.modules):
            prog = sys.modules[commTbl[1]]
            client.send_message(message.channel, "Help for " + commTbl[1] + ":")
            prog.help(message, commTbl, client)
        else:
            client.send_message(message.channel, "Help for the command specified could not be found. " + message.author.mention()) 
    else:
            client.send_message(message.channel, "The command specified could not be found. " + message.author.mention())

# Logs text to console.
def log(text):
    print("[LOG] " + text)

client = loadAll()

# Splits parameters.
@client.event
def on_message(message):
    if message.content.startswith("!"):
        comm = message.content[1:]
        comms = comm.split(" ")
        log("Attempting to run command: " + comms[0])
        runCommand(comms, message)
    else:
        auto.main(message, client)

@client.event
def on_ready():
    log("Logged in!")

client.run()
