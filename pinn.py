#Pinn-generating module for the bot.

import random
maxNum = 3
pinnLinks = [
	"http://i.imgur.com/4uBVAlv.jpg",
	"http://i.imgur.com/N7ZLdtD.jpg",
	"http://i.imgur.com/aTDVeFX.jpg",
	"http://i.imgur.com/SwIsGcW.jpg",
]

def main(message, comms, client):
	if (len(comms) == 1):
		ranNum = random.randint(0, maxNum)
		client.send_message(message.channel, pinnLinks[ranNum])
	else:
		if int(comms[1]) <= maxNum + 1:
			client.send_message(message.channel, pinnLinks[int(comms[1]) - 1])
	
def help(message, comms, client):
	client.send_message(message.channel, "Posts a random picture of you-know-who.")