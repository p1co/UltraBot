import random

responses = [
	"It is certain",
	"It is decidedly so",
	"Without a doubt",
	"Yes, definately",
	"You may rely on it",
	"As I see it, yes",
	"Most likley",
	"Outlook good",
	"Yes",
	"Signs point to yes",
	"Reply hazy try again",
	"Ask again later",
        "Better not tell you know",
        "Cannot perdict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
]

def main(message, args, client):
	maxNum = len(responses) - 1
	rand = random.randint(0, maxNum)
	client.send_message(message.channel, responses[rand])
def help(message, args, client):
        client.send_message(message.channel,"Inserts a repsonse to a question you ask. Usage: !8ball [Question]")
