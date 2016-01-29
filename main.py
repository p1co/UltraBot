# Import things that are needed.
import discord, sys, time, importlib, asyncio, log
from os import listdir
from os.path import isfile, join
# Create empty dictionaries for future use.
userClocks = {}
dontLoad = [".gitignore", "__pycache__"] # Don't load any modules that are in here! You can put any module you don;t want to be automatically loaded in here.

def listContains(listMain, test): # Checks if a list object contains a certain object.
    for a in listMain:
        if a == test:
            return True
    return False

def loadAll(): # Loads everything at the start.
    sys.path.append("modules")
    onlyfiles = listdir('modules')
    moduleList = [] # Create list to contain module names.
    for module in onlyfiles:
        if not (listContains(dontLoad, module)): # Check if it is meant to be loaded.
            modName = module.split(".") # Get the first part of the module name, excluding the extension .py
            obj = __import__(modName[0])
            globals()[modName[0]] = obj # Add module to the global variables.
            log.log("Loaded module: " + modName[0])
            moduleList.insert(0, modName[0])

    #Login with details from file
    client = discord.Client() # Ininitalise new Discord client.
    return client, moduleList

# Runs command
async def runCommand(commTbl, message, moduleList): # Define main command-processing function.
    if (commTbl[0] == "debug"): # Checks if command specified is special module 'debug'
        prog = sys.modules[commTbl[0]]

        try: # Attempt to run the debug command. If an error occurs, display that an error has occurred in the main console.
            await prog.main(message, commTbl, client, moduleList, sys)
        except Exception as error:
            log.log("Debug error: " + str(error))

    elif (commTbl[0] == "help"): # Checks if command specified is special module 'help'
        try: # Attempt to run help for a specified command. If help does not exist, or the command does not exist, or it errors, display that it has errored.
            prog = sys.modules[commTbl[1]]
            await client.send_message(message.channel, "Help for " + commTbl[1] + ":")
            await prog.help(message, commTbl, client)
        except Exception:
            log.log("Error occured in " + commTbl[0])
            await client.send_message(message.channel, "Help for the command specified could not be found. " + message.author.mention)

    elif (commTbl[0] in sys.modules): # Checks if command specified exists in modules loaded.
        log.log("Found module with name " + commTbl[0])
        prog = sys.modules[commTbl[0]]

        try: # Attempt to run the command specified. If an error occurs, display that an error has occurred.
            await prog.main(message, commTbl, client)
        except Exception as ex:
            log.log("Error occured in " + commTbl[0] + ": " + str(ex))
            await client.send_message(message.channel, "An error occoured.")
    else: # If the command couldn't be found, display error message.
        await client.send_message(message.channel, "The command specified could not be found. ")
    

client, moduleList = loadAll() # Run loadAll


@client.event
async def on_message(message): # On message. This tries to figure out if it is a command, and if so, uses runCommand on it. Else, runs auto module on it.
    justMade = False

    if message.author.id != client.user.id:
        if message.content.startswith("!"): # If it is a command
            try: # Attempt to figure out whether they already have a previous user-clock.
                clockCur = userClocks[message.author.id]
            except Exception:
                userClocks[message.author.id] = time.clock() # If they don't, create one.
                justMade = True
            if userClocks[message.author.id] < time.clock() - 1 or justMade == True: # If they haven't issued a command within the last second, let them run one now.
                justMade = False
                userClocks[message.author.id] = time.clock() # Set new clock.
                comm = message.content[1:] # Get rid of !
                comms = comm.split(" ") # Split the command into the parameters
                log.log(message.author.name + " attempted to run command: " + comms[0])
                await runCommand(comms, message, moduleList)
            else:
                log.log("Stopped spam from " + message.author.name)
        else:
            await auto.main(message, client) # Run auto module on the text that has been sent.


@client.event
async def on_ready(): # Print logged in, when logged in.
    log.log("Logged in!")

details = open("login.txt", "r") # Open the defined login details at /login.txt
logins = details.read().split(",") # Split them up into email and pass
details.close()
client.run(logins[0], logins[1]) # Run the client with the details