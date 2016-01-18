def listContains(listMain, test):
    for a in listMain:
        if a.name.lower() == test:
            return True

async def main(message, args, client):
    members = client.get_all_members()
    users = []
    toMessage = "Mentioning all members in " + args[1] + ": "
    for member in members:
        print(member.name)
        if listContains(member.roles, args[1].lower()):
            toMessage = toMessage + " " + member.mention
    await client.send_message(message.channel, toMessage)

async def help(message, args, client):
	await client.send_message(message.channel, "Mentions all users in a specified group, usage: \"!mention <group name>\"")
	