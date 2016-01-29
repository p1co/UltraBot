import log
#Debugging module for the bot.

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
						#if user.status == 'online':
							messTo = messTo + user.name + "; "
				await client.send_message(message.channel, messTo)

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
						log.log("The command gave an error:" + str(ex))
			else:
				client.send_message(message.channel, "No command was specified to run! " + message.author.mention)