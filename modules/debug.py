#Debugging module for the bot.
import time, datetime, os

starttime = time.time()

async def help(message, args, client):
	await client.send_message("!debug get <version|modules|users|uptime|issues> version lists current version, modules lists all currently loaded modules, users lists all currently online users, uptime gets current bot uptime, issues gets any currently known issues.")
	await client.send_message("!debug run <command> <args> runs a specified command with any arguments, useful for finding errors.")

async def main(message, args, client, modules, sys):
	if len(args) > 1:
		if args[1] == "get":
			if args[2] == "modules":
				moduleList = "Modules currently loaded"
				for mod in modules:
					moduleList = moduleList + "; " + mod
				await client.send_message(message.channel, moduleList)

			elif args[2] == "issues":
				await client.send_message(message.channel, "Known issues:")
				await client.send_message(message.channel, "- Possible spelling errors")
				await client.send_message(message.channel, "- Manuadd <add> does not work.")

			elif args[2] == "users":
				messTo = "Users currently online: "
				for server in client.servers:
					for user in server.members:
						print(user.name + str(user.status))
						if str(user.status) == 'online':
							messTo = messTo + user.name + "; "
				await client.send_message(message.channel, messTo)
			elif args[2] == "version":
				await client.send_message(message.channel, sysVersion)
			elif args[2] == "uptime":
				uptime = time.time() - starttime
				uptime = datetime.timedelta(seconds=int(uptime))
				await client.send_message(message.channel, "Current uptime is: " + str(uptime))
			else:
				await client.send_message(message.channel, "Command not found within debug module.")

		elif args[1] == "run":
			if args[2] != None:
				modName = args[2]
				if sys.modules[modName] != None:
					newArgs = []
					newArgs = args
					newArgs.pop(0)
					newArgs.pop(0)
					await client.send_message(message.channel, "Attempting to run command: " + modName)
					try:
						await sys.modules[modName].main(message, newArgs, client)
					except Exception as ex:
						await client.send_message(message.channel, "That command gave an error: " + str(ex))
						log("Debug found an error in: " + modName + ". The error was: " + str(ex), level=3)
			else:
				await client.send_message(message.channel, "No command was specified to run! " + message.author.mention)

		elif args[1] == "load": #Attempt to force the main file to load a module
			if args[2] != None and args[3] != None:
				modName = args[2] 
				loadType = args[3]
				retTbl = {"op" : "loadModule", "loadType" : "local", "moduleID" : modName}
				return retTbl

		elif args[1] == "unload": #Attempt to force the main file to unload a module
			if args[2] != None:
				modName = args[2]
				retTbl = {"op": "unloadModule", "moduleID" : args[2]}
				return retTbl

		elif args[1] == "reload":
			if args[2] != None:
				modName = args[2]
				retTbl = {"op": "reloadModule", "moduleID": args[2]}
				return retTbl