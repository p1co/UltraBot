import discord

client = discord.Client()
client.login("elephantsAndMail@gmail.com", "ALongerPassword")

def listContains(listMain, test):
    for a in listMain:
        if a.name == test:
            return True

@client.event
def on_message(message):
    
    if message.content.startswith('!GTA'):
        members = client.get_all_members()
        toSend = []
        users = []
        toMessage = ""
        for member in members:
            if listContains(member.roles, "gta"):
                toMessage = toMessage + " " + member.mention()
        client.send_message(message.channel, toMessage, mentions=True)
            
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
