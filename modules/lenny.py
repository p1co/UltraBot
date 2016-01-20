async def main(t, t1, client):
        await client.send_message(t.channel, "( ͡° ͜ʖ ͡°)")
async def help(message, args, client):
        await client.send_message(message.channel,"Inserts a lenny face. An all-purpose command for every conceivable situation. Usage: !lenny")
