import discord

client = discord.Client()
client.login("elephantsAndMail@gmail.com", "ALongerPassword")

def listContains(listMain, test):
    for a in listMain:
        if a.name == test:
            return True


class newCommands:
    def mention(message, args):
        if message.content.startswith('!mention'):
            members = client.get_all_members()
            toSend = []
            users = []
            toMessage = ""
            for member in members:
                if listContains(member.roles, args[1].lower()):
                    toMessage = toMessage + " " + member.mention()
        client.send_message(message.channel, toMessage)



commands_main = newCommands()

@client.event
def on_message(message):
    messCont = message.content[1:]
    commTbl = messCont.split(" ")
    try:
        toCall = getattr(newCommands, commTbl[0])
        toCall(message, commTbl)
    except AttributeError:
        print("fuck")

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()