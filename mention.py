class mention:
	def main():
                members = client.get_all_members()
                users = []
                toMessage = "Mentioning all members in " + args[1] + " : "
                for member in members:
                    print(member.name)
                    if listContains(member.roles, args[1].lower()):
                        toMessage = toMessage + " " + member.mention()
                client.send_message(message.channel, toMessage)
	def help():
