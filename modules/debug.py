#Debugging module for the bot.

def main(message, args, client, modules, sys):
	if len(args) > 1:
		if args[1] == "list" and args[2] == "modules":
			moduleList = "Modules currently loaded"
			for mod in modules:
				moduleList = moduleList + "; " + mod
			client.send_message(message.channel, moduleList)

		elif args[1] == "run":
			if args[2] != None:
				modName = args[2]
				if sys.modules[modName] != None:
					newArgs = []
					newArgs = args
					newArgs.pop(0)
					newArgs.pop(0)
					try:
						sys.modules[modName].main(message, newArgs, client)
					except Exception as ex:
						client.send_message(message.channel, "That command gave an error: " + str(ex))