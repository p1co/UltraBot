import log
async def main(t, t1, client):
        await client.send_message(t.channel, "Hello, world!")
async def help(message, args, client):
        await client.send_message(message.channel,"A nerdier ping. Usage: !hello")
