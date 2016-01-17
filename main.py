import discord
import sys
import importlib
from os import listdir
from os.path import isfile, join

def listContains(listMain, test):
    for a in listMain:
        if a == test:
            return True
    return False

def loadAll():
    sys.path.append("modules")
    onlyfiles = listdir('modules')
    moduleList = []
    dontLoad = [".gitignore", "__pycache__"]
    for module in onlyfiles:
        if not (listContains(dontLoad, module)):
            modName = module.split(".")
            obj = __import__(modName[0])
            globals()[modName[0]] = obj
            log("Loaded module: " + modName[0])
            moduleList.insert(0, modName[0])

    #Login with details from file
    details = open("login.txt", "r")
    logins = details.read().split(",")
    details.close()
    client= discord.Client()
    client.login(logins[0], logins[1])
    return client, moduleList

# Runs command
def runCommand(commTbl, message, moduleList):
    if (commTbl[0] == "debug"):
        prog = sys.modules[commTbl[0]]
        try:
            prog.main(message, commTbl, client, moduleList, sys)
        except Exception:
            log("Error occured in " + commTbl[0])
    elif (commTbl[0] in sys.modules):
        log("Found module with name " + commTbl[0])
        prog = sys.modules[commTbl[0]]
        try:
            prog.main(message, commTbl, client)
        except Exception:
            log("Error occured in " + commTbl[0])
    elif (commTbl[0] == "help"):
        if (commTbl[1] in sys.modules):
            try:
                prog = sys.modules[commTbl[1]]
            except Exception:
                log("Error occured in " + commTbl[0])
            client.send_message(message.channel, "Help for " + commTbl[1] + ":")
            prog.help(message, commTbl, client)
        else:
            client.send_message(message.channel, "Help for the command specified could not be found. " + message.author.mention())
    else:
            client.send_message(message.channel, "The command specified could not be found. " + message.author.mention())

# Logs text to console.
def log(text):
    print("[LOG] " + text)

client, moduleList = loadAll()

# Splits parameters.
@client.event
def on_message(message):
    if message.content.startswith("!"):
        comm = message.content[1:]
        comms = comm.split(" ")
        log("Attempting to run command: " + comms[0])
        runCommand(comms, message, moduleList)
    else:
        auto.main(message, client)

@client.event
def on_ready():
    log("Logged in!")

client.run()
