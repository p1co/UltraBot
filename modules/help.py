async def main(t, t1, client):
        await client.send_message(t.channel, "A help command will go here one day!")
async def help(message, args, client):
        await client.send_message(message.channel,"so meta. Usage: !help [command]")
