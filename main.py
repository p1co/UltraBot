import discord
import sys
sys.path.append(r'D:\Documents\GitHub\GameMentionBot\modules')

import hello
import lenny
import mention
import auto
import pinn
import dankmeme
import help
import eightball

#Login with details from file
details = open("login.txt", "r")
logins = details.read().split(",")
details.close()
client= discord.Client()
client.login(logins[0], logins[1])

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
            client.send_message(message.channel, "The command specified does not exist. " + message.author.mention()) 
    else:
            client.send_message(message.channel, "Sorry, that command doesn't exist! " + message.author.mention())

# Logs text to console.
def log(text):
    print("[LOG] " + text)

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
