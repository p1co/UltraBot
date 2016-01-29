# Ability to add/remove yourself from a server-side role.
async def main(message, args, client):
    member = message.author
    if args[1] == "add":
        try:
            otherMember = args[2]
            newRank = args[3]
            if member.id == int(otherMember):
                await client.add_roles(member, [newRank])
                await client.send_message(message.channel, "User added to " + newRank + " role.")
            else:
                await client.send_message(message.channel, "Fuck.")
        except Exception:
            await client.send_message(message.channel, "Invalid usage of manuadd! Do !help manuadd for more info." + message.author.mention)
    elif args[1] == "remove":
        try:
            otherMember = args[2]
            rank = args[3]
            if member.id == int(otherMember):
                await client.remove_roles(member, [rank])
                await client.send_message(message.channel, "User removed from " + rank + " role.")
        except Exception:
            await client.send_message(message.channel, "Invalid usage of manuadd! Do !help manuadd for more info." + message.author.mention)
    elif args[1] == "getid":
        await client.send_message(message.channel, "Your user ID is: " + message.author.id)

async def help(message, args, client):
    await client.send_message(message.channel, "Usage for manuadd:")
    await client.send_message(message.channel, "!manuadd add <user> <role> (Adds a specific user to a specific group.)")
    await client.send_message(message.channel, "!manuadd getid (Returns your user-specific ID.)")