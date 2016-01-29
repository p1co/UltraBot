#definitelylink-generating module for the bot.

import log

async def main(t, t1, client):
        await client.send_message(t.channel, "http://www.d-e-f-i-n-i-t-e-l-y.com/")
async def help(message, args, client):
        await client.send_message(message.channel,"Someone spelt it wrong again? Usage: !definitely")
