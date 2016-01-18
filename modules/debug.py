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
				await client.send_message(message.channel, "No know issues at the moment.")

		elif args[1] == "run":
			if args[2] != None:
				modName = args[2]
				if sys.modules[modName] != None:
					newArgs = []
					newArgs = args
					newArgs.pop(0)
					newArgs.pop(0)
					try:
						await sys.modules[modName].main(message, newArgs, client)
					except Exception as ex:
						await client.send_message(message.channel, "That command gave an error: " + str(ex))