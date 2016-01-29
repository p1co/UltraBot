async def main(t, t1, client):
        await client.send_message(t.channel, "You are running a development version.")
async def help(message, args, client):
        await client.send_message(message.channel,"Shows the version of the bot. Usuage: !version")
