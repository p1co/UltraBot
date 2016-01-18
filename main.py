import discord
import sys
import time
import importlib
from os import listdir
from os.path import isfile, join
userClocks = {'guy': time.clock()}


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
    client= discord.Client()
    return client, moduleList

# Runs command
async def runCommand(commTbl, message, moduleList):
    if (commTbl[0] == "debug"):
        prog = sys.modules[commTbl[0]]
        try:
            await prog.main(message, commTbl, client, moduleList, sys)
        except Exception:
            log("Error occured in " + commTbl[0])
    elif (commTbl[0] in sys.modules):
        log("Found module with name " + commTbl[0])
        prog = sys.modules[commTbl[0]]
        try:
            await prog.main(message, commTbl, client)
        except Exception:
            log("Error occured in " + commTbl[0])
    elif (commTbl[0] == "help"):
        if (commTbl[1] in sys.modules):
            try:
                prog = sys.modules[commTbl[1]]
            except Exception:
                log("Error occured in " + commTbl[0])
            await client.send_message(message.channel, "Help for " + commTbl[1] + ":")
            await prog.help(message, commTbl, client)
        else:
            await client.send_message(message.channel, "Help for the command specified could not be found. " + message.author.mention())
    else:
        await client.send_message(message.channel, "The command specified could not be found. ")
    

# Logs text to console.
def log(text):
    print("[LOG] " + text)

client, moduleList = loadAll()

# Splits parameters.

@client.event
async def on_message(message):
    justMade = False

    if message.author.id != client.user.id:
        if message.content.startswith("!"):
            try:
                clockCur = userClocks[message.author.id]
            except Exception:
                userClocks[message.author.id] = time.clock()
                justMade = True
            if userClocks[message.author.id] < time.clock() - 1 or justMade == True:
                justMade = False
                userClocks[message.author.id] = time.clock()
                comm = message.content[1:]
                comms = comm.split(" ")
                log("Attempting to run command: " + comms[0])
                await runCommand(comms, message, moduleList)
            else:
                log("Stopped spam from " + message.author.name)
        else:
            await auto.main(message, client)


@client.event
async def on_ready():
    log("Logged in!")




details = open("login.txt", "r")
logins = details.read().split(",")
details.close()
client.run(logins[0], logins[1])