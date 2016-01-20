import random

responses = [
	"It is certain",
	"It is decidedly so",
	"Without a doubt",
	"Yes, definitely",
	"You may rely on it",
	"As I see it, yes",
	"Most likely",
	"Outlook good",
	"Yes",
	"Signs point to yes",
	"Reply hazy try again",
	"Ask again later",
        "Better not tell you know",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
]

async def main(message, args, client):
	maxNum = len(responses) - 1
	rand = random.randint(0, maxNum)
	await client.send_message(message.channel, responses[rand])
async def help(message, args, client):
    await client.send_message(message.channel,"Inserts a repsonse to a question you ask. Usage: !8ball [Question]")
