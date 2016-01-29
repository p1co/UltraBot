async def help(message, args, client):
        await client.send_message(message.channel, "Offers useful help on a command. Usage: !help <command name>")