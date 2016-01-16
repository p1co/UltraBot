import discord
import sys
import hello
import lenny

client = discord.Client()
client.login("james@hurcomb.net", "ALongerPassword")

def runCommand(commTbl, message):
    if (commTbl[0] in sys.modules):
        print("hey!")
        prog = sys.modules[commTbl[0]]
        prog.main(message, commTbl, client)

def listContains(listMain, test):
    for a in listMain:
        if a.name.lower() == test:
            return True

def log(text):
    print("[LOG] " + text)

@client.event
def on_message(message):
    if message.content.startswith("!"):
        comm = message.content[1:]
        comms = comm.split(" ")
        log("Attempting to run command: " + comms[0])
        runCommand(comms, message)

@client.event
def on_ready():
    log("Logged in!")

client.run()