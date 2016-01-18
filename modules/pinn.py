#Pinn-generating module for the bot.

import random
pinnLinks = [
	"http://i.imgur.com/4uBVAlv.jpg",
	"http://i.imgur.com/N7ZLdtD.jpg",
	"http://i.imgur.com/aTDVeFX.jpg",
	"http://i.imgur.com/SwIsGcW.jpg",
]

maxNum = len(pinnLinks) - 1

async def main(message, comms, client):
	if (len(comms) == 1):
		ranNum = random.randint(0, maxNum)
		await client.send_message(message.channel, pinnLinks[ranNum])
	else:
		if int(comms[1]) <= maxNum + 1:
			await client.send_message(message.channel, pinnLinks[int(comms[1]) - 1])
	
async def help(message, comms, client):
	await client.send_message(message.channel, "Posts a random picture of you-know-who.")