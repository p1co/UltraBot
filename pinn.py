#Pinn-generating module for the bot.

import random
pinnLinks = [
	"http://i.imgur.com/4uBVAlv.jpg",
	"http://i.imgur.com/N7ZLdtD.jpg",
	"http://i.imgur.com/aTDVeFX.jpg",
]

def main(message, comms, client):
	ranNum = random.randint(0, 2)
	client.send_message(message.channel, pinnLinks[ranNum])
	
def help(message, comms, client):
	client.send_message(message.channel, "Posts a random picture of you-know-who.")